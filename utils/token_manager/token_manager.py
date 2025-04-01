import re
import tiktoken

from utils.token_manager.costs import cost_map
from datetime import datetime

from tokencost import calculate_prompt_cost, calculate_completion_cost

from utils.common import logger

class TokenManager:
    """
    Si occupa di:
    - Mappare il nome del modello personalizzato in uno ufficiale (per tiktoken),
    - Contare i token di system_prompt, user_prompt e completion,
    - Calcolare i costi stimati,
    - Accumulare i totali (prompt_tokens, response_tokens, cost) e registrare
    ogni operazione per generare un report dettagliato.
    """
    def __init__(self):
        self.total_prompt_tokens = 0
        self.total_response_tokens = 0
        self.total_cost = 0
        # Conserva i dettagli delle operazioni per il report.
        self.report_entries = []

    def _map_model_name_to_official(self, custom_model_name: str) -> str:
        """
        Mappa il nome del modello personalizzato a un nome ufficiale riconoscibile da tiktoken
        (o definisce eventuali fallback se necessario).
        """
        model_mapping = {
            "gpt-4o-super": "azure/gpt-4o-2024-08-06",
            "gpt-4o-mini-super": "azure/gpt-4o-mini",
            # Aggiungi altre eventuali mappature se necessario.
        }
        # Usa una regex per controllare se il nome del modello contiene 'claude-3.5'
        if re.search(r'claude-3-5', custom_model_name):
            return "eu.anthropic.claude-3-5-sonnet-20240620-v1:0"

        if re.search(r'claude-3-7', custom_model_name): #ATTENZIONE: non ancora presente 3.7
            return "eu.anthropic.claude-3-5-sonnet-20240620-v1:0"

        return model_mapping.get(custom_model_name, custom_model_name)

    def _get_encoding(self, model_name: str):
        """
        Tenta di ottenere l'encoding corretto per il modello;
        se non disponibile, usa l'encoding di fallback (cl100k_base).
        """
        try:
            return tiktoken.encoding_for_model(model_name)
        except KeyError:
            return tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, model_name: str, text: str) -> int:
        """
        Conta il numero di token in una stringa di testo secondo l'encoding del modello.
        """

        _model_name = self._map_model_name_to_official(model_name)
        encoding = self._get_encoding(_model_name)
        return len(encoding.encode(text))

    #DA RIMUOVERE - USO LA LIB TOKENCOST
    def calculate_and_apply_cost_v0(self, model_name: str, system_prompt: str, user_prompt: str, completion: str) -> tuple:
        """
        Calcola il costo stimato (prompt + completion), aggiorna i contatori interni
        e ritorna (costo, numero_token_prompt, numero_token_completion).

        I costi sono puramente indicativi, ad esempio per GPT-3.5/GPT-4.
        """

        official_model_name = self._map_model_name_to_official(model_name)

        # Conta i token del prompt (system + user) e della completion.
        prompt_text = system_prompt + user_prompt
        prompt_tokens = self.count_tokens(official_model_name, prompt_text)
        completion_tokens = self.count_tokens(official_model_name, completion)

        try:
            selected_costs = cost_map[official_model_name]
        except KeyError:
            # Se non esiste una configurazione di costi per il modello, segnala un errore.
            raise ValueError(f"Non esistono costi definiti per il modello: {official_model_name}")

        total_cost = (
            (prompt_tokens * selected_costs["prompt"] / 1000) +
            (completion_tokens * selected_costs["completion"] / 1000)
        )

        # Aggiorna i totali.
        self.total_prompt_tokens += prompt_tokens
        self.total_response_tokens += completion_tokens
        self.total_cost += total_cost

        # Crea una entry per il report.
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "model": official_model_name,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_cost": total_cost,
            # Puoi includere anche altri dettagli se necessario:
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "completion": completion
        }
        self.report_entries.append(entry)

        # Stampa un riepilogo nel terminale.
        # print(f"-----------------{official_model_name}---------------------------------")
        # print(f"Total cost = {total_cost:.4f} - Prompt tokens = {prompt_tokens} - Completion tokens = {completion_tokens}")
        # print("--------------------------------------------------")

        return total_cost, prompt_tokens, completion_tokens

    def calculate_and_apply_cost(self, model_name: str, system_prompt: str, user_prompt: str, completion: str) -> tuple:

        try:
            official_model_name = self._map_model_name_to_official(model_name)
            #print("official_model_name=", official_model_name)

            prompt_text = system_prompt + user_prompt
            prompt_cost = calculate_prompt_cost(prompt_text, official_model_name)

            completion_cost = calculate_completion_cost(completion, official_model_name)

            # Conta i token del prompt (system + user) e della completion.
            prompt_text = system_prompt + user_prompt
            prompt_tokens = self.count_tokens(official_model_name, prompt_text)
            completion_tokens = self.count_tokens(official_model_name, completion)

            total_cost = prompt_cost + completion_cost

            # Aggiorna i totali.
            self.total_prompt_tokens += prompt_tokens
            self.total_response_tokens += completion_tokens
            self.total_cost += total_cost

            # Crea una entry per il report.
            entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "model": official_model_name,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_cost": total_cost,
                # Puoi includere anche altri dettagli se necessario:
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "completion": completion
            }
        except Exception as e:
            logger.error(f"Errore nel calcolo dei costi del token: {e}")
            entry = {}
            total_cost = prompt_tokens = completion_tokens = -1

        self.report_entries.append(entry)

        return total_cost, prompt_tokens, completion_tokens


    def get_stats(self) -> dict:
        """
        Restituisce un dizionario con i totali accumulati di token e costi.
        """
        return {
            "total_prompt_tokens": self.total_prompt_tokens,
            "total_response_tokens": self.total_response_tokens,
            "total_cost": self.total_cost
        }

    def reset_stats(self):
        """Azzera i contatori interni e la history del report."""
        self.total_prompt_tokens = 0
        self.total_response_tokens = 0
        self.total_cost = 0
        self.report_entries = []

    def save_report_to_file(self, file_path: str):
        """
        Genera un report dettagliato e lo salva su file.
        Il report contiene una entry per ogni operazione ed un riepilogo finale.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                # Intestazione del report.
                f.write("# Report Token Manager\n\n")
                f.write(f"**Data e ora:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                f.write("## Dettaglio operazioni\n")
                for i, entry in enumerate(self.report_entries, 1):
                    f.write(f"### Operazione {i} - {entry['timestamp']}\n")
                    f.write(f"- **Modello:** {entry['model']}\n")
                    f.write(f"- **Prompt tokens:** {entry['prompt_tokens']}\n")
                    f.write(f"- **Completion tokens:** {entry['completion_tokens']}\n")
                    f.write(f"- **Costo:** {entry['total_cost']:.4f}\n")
                    # Se vuoi includere i testi delle richieste puoi decommentare le seguenti righe:
                    # f.write(f"- **System prompt:** {entry['system_prompt']}\n")
                    # f.write(f"- **User prompt:** {entry['user_prompt']}\n")
                    # f.write(f"- **Completion:** {entry['completion']}\n")
                    f.write("\n")

                    # Riepilogo totale.
                f.write("## Riepilogo finale\n")
                stats = self.get_stats()
                f.write(f"- **Total prompt tokens:** {stats['total_prompt_tokens']}\n")
                f.write(f"- **Total response tokens:** {stats['total_response_tokens']}\n")
                f.write(f"- **Total cost:** {stats['total_cost']:.4f}\n")

            logger.info(f"Report salvato in '{file_path}'")
        except Exception as e:
            logger.error(f"Errore nel salvataggio del report: {e}")