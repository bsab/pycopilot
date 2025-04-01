import os

from openai import AzureOpenAI, api_key
from abc import ABC, abstractmethod

from utils.common import load_yaml_config, logger
from utils.token_manager.token_manager import TokenManager

from langchain.text_splitter import RecursiveCharacterTextSplitter

# ~2000 caratteri corrispondono circa a 500 token ovvero dimensione ottimale superato il quale il LLM va in Lost-in-the-middle
DEFAULT_CHUNK_SIZE = 2000

class BaseAgent(ABC):
    def __init__(
            self,
            config_section: str,
            config_path: str = "config.yaml",
            external_token_manager: TokenManager = None,
    ):
        """
        Classe astratta base con configurazione YAML e client LLM.
        La sezione di configurazione (config_section) deve contenere una delle seguenti:

        • Per OpenAI:
            openai:
              model_name:  "nome_modello"
              api_key:     "chiave_api"
              api_version: "versione_api"
              base_url:    "endpoint_azure"

        • Per AnthropicBedrock:
            anthropic_bedrock:
              aws_access_key: "YOUR_AWS_ACCESS_KEY"
              aws_secret_key: "YOUR_AWS_SECRET_KEY"
              aws_region:     "eu-west-1"
              model_name:     "eu.anthropic.claude-3-7-sonnet-20250219-v1:0"
              max_tokens:     12000   # opzionale, default 12000

        • Per Bedrock (AWS):
            aws_bedrock:
              model_name:  "nome_modello"
              api_key:     "aws_api_key"
              api_secret:  "aws_api_secret"
              region:      "aws_region"

        Il provider viene scelto in automatico in base alle chiavi presenti.
        """

        self.config_section = config_section
        self._full_config = load_yaml_config(config_path)
        self.config = self._full_config.get(self.config_section, {})

        # Determinazione del provider in base alle chiavi esistenti:
        if "openai" in self.config:
            self.provider = "openai"
        elif "anthropic_bedrock" in self.config:
            self.provider = "anthropic-bedrock"
        elif "aws_bedrock" in self.config:
            self.provider = "bedrock"
        else:
            raise ValueError(
                "Configurazione non valida: Nessuna sezione 'openai', 'anthropic_bedrock' o 'aws_bedrock' trovata.")

            # Crea il client in base al provider determinato
        self.client = self._create_client()

        # Imposta il nome del modello in base al provider
        if self.provider == "openai":
            try:
                self.model_name = self.config["openai"]["model_name"]
            except KeyError as key_exc:
                raise KeyError(
                    f"[BaseAgent] Chiave 'model_name' mancante nella configurazione OpenAI: {key_exc}") from key_exc
        elif self.provider == "anthropic-bedrock":
            try:
                self.model_name = self.config["anthropic_bedrock"]["model_name"]
            except KeyError as key_exc:
                raise KeyError(
                    f"[BaseAgent] Chiave 'model_name' mancante nella configurazione AnthropicBedrock: {key_exc}") from key_exc
        elif self.provider == "bedrock":
            try:
                self.model_name = self.config["aws_bedrock"]["model_name"]
            except KeyError as key_exc:
                raise KeyError(
                    f"[BaseAgent] Chiave 'model_name' mancante nella configurazione AWS Bedrock: {key_exc}") from key_exc

        self.token_manager = external_token_manager

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=DEFAULT_CHUNK_SIZE,  # Valore migliore per il chunking
            chunk_overlap=10,  # Se vuoi sovrapposizione, imposta un valore > 0
            separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""]
        )

    def _create_client(self):
        if self.provider == "openai":
            try:
                openai_config = self.config["openai"]
                api_key_val = openai_config["api_key"]
                api_version = openai_config["api_version"]
                azure_endpoint = openai_config["base_url"]
                return AzureOpenAI(
                    api_key=api_key_val,
                    api_version=api_version,
                    azure_endpoint=azure_endpoint
                )
            except KeyError as key_exc:
                raise KeyError(f"[BaseAgent] Chiave mancante nella configurazione OpenAI: {key_exc}") from key_exc
            except Exception as exc:
                raise RuntimeError(f"[BaseAgent] Errore creazione client OpenAI: {exc}") from exc

        elif self.provider == "bedrock":
            try:
                from langchain_aws import ChatBedrock
                aws_config = self.config["aws_bedrock"]
                api_key_val = aws_config["api_key"]
                api_secret = aws_config["api_secret"]
                region = aws_config["region"]

                os.environ["AWS_ACCESS_KEY_ID"] = api_key_val
                os.environ["AWS_SECRET_ACCESS_KEY"] = api_secret
                os.environ["AWS_DEFAULT_REGION"] = region

                model_id = aws_config["model_name"]
                return ChatBedrock(model_id=model_id)
            except KeyError as key_exc:
                raise KeyError(f"[BaseAgent] Chiave mancante nella configurazione AWS Bedrock: {key_exc}") from key_exc
            except Exception as exc:
                raise RuntimeError(f"[BaseAgent] Errore creazione client Bedrock: {exc}") from exc

        elif self.provider == "anthropic-bedrock":
            try:
                from anthropic import AnthropicBedrock
                anthropic_config = self.config["anthropic_bedrock"]
                aws_access_key = anthropic_config["api_key"]
                aws_secret_key = anthropic_config["api_secret"]
                aws_region = anthropic_config["region"]

                return AnthropicBedrock(
                    aws_access_key=aws_access_key,
                    aws_secret_key=aws_secret_key,
                    aws_region=aws_region
                )
            except KeyError as key_exc:
                raise KeyError(
                    f"[BaseAgent] Chiave mancante nella configurazione AnthropicBedrock: {key_exc}") from key_exc
            except Exception as exc:
                raise RuntimeError(f"[BaseAgent] Errore creazione client AnthropicBedrock: {exc}") from exc

    def chat_completion(
            self,
            system_prompt: str = None,
            user_prompt: str = None,
            model_name: str = None,
            temperature: float = 0.0
    ) -> str:
        """
        Esegue la chiamata al modello LLM e delega la logica specifica del provider
        alle funzioni helper dedicate.
        """
        if self.client is None:
            raise ValueError("[BaseAgent] Errore: Client LLM non configurato correttamente.")

        if user_prompt is None:
            raise ValueError("[BaseAgent] user_prompt è vuoto!")

        if model_name is None:
            model_name = self.model_name

        if self.provider == "openai":
            return self._chat_completion_openai(system_prompt, user_prompt, model_name, temperature)
        elif self.provider == "bedrock":
            return self._chat_completion_bedrock(system_prompt, user_prompt, model_name)
        elif self.provider == "anthropic-bedrock":
            return self._chat_completion_anthropic_bedrock(system_prompt, user_prompt, model_name)
        else:
            raise NotImplementedError(f"[BaseAgent] Provider '{self.provider}' non supportato.")

    def _chat_completion_openai(self, system_prompt: str, user_prompt: str, model_name: str, temperature: float) -> str:
        """
        Gestisce la chiamata a OpenAI utilizzando il metodo chat completions.
        """
        if system_prompt is None:
            system_prompt = (
                "You are a specialized assistant that extracts specific information "
                "from a document. Provide concise and accurate answers."
            )
        try:
            if model_name in ["o1", "o1-mini", "o3-mini"]:
                response = self.client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ]
                )
            else:
                response = self.client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=temperature
                )
            extraction = response.choices[0].message.content.strip()
            if self.token_manager:
                self.token_manager.calculate_and_apply_cost(
                    model_name,
                    system_prompt,
                    user_prompt,
                    extraction
                )
            return extraction

        except Exception as exc:
            raise RuntimeError(f"[BaseAgent] Errore durante la chiamata OpenAI: {exc}") from exc

    def _chat_completion_bedrock(self, system_prompt: str, user_prompt: str, model_name: str) -> str:
        """
        Gestisce la chiamata al client Bedrock (AWS).
        """
        try:
            final_input = f"{system_prompt}\n{user_prompt}" if system_prompt else user_prompt

            prompt_template_str = "Domanda: {input}\nRisposta:"
            from langchain_core.prompts import PromptTemplate
            prompt_template = PromptTemplate.from_template(prompt_template_str)

            chain = prompt_template | self.client
            extraction = chain.invoke({"input": final_input})
            if hasattr(extraction, "content"):
                extraction = extraction.content.strip()

            if self.token_manager:
                self.token_manager.calculate_and_apply_cost(
                    model_name,
                    system_prompt or "",
                    user_prompt,
                    extraction
                )
            return extraction

        except Exception as exc:
            raise RuntimeError(f"[BaseAgent] Errore durante la chiamata Bedrock: {exc}") from exc

    def _chat_completion_anthropic_bedrock(self, system_prompt: str, user_prompt: str, model_name: str) -> str:
        """
        Gestisce la chiamata a AnthropicBedrock.
        """
        try:
            final_prompt = f"{system_prompt}\n{user_prompt}" if system_prompt else user_prompt
            messages = [{"role": "user", "content": final_prompt}]

            # Ottiene il max_tokens dalla configurazione (default 12000)
            max_tokens = self.config["anthropic_bedrock"].get("max_tokens", 12000)

            extraction = self.client.messages.create(
                model=model_name,
                max_tokens=max_tokens,
                messages=messages
            )

            if isinstance(extraction.content, list):
                extraction = " ".join(tb.text for tb in extraction.content)

            if self.token_manager:
                self.token_manager.calculate_and_apply_cost(
                    model_name,
                    system_prompt or "",
                    user_prompt,
                    extraction
                )
            return extraction

        except Exception as exc:
            raise RuntimeError(f"[BaseAgent] Errore durante la chiamata AnthropicBedrock: {exc}") from exc

    def count_tokens(self, text_to_count):
        if self.token_manager:
            return self.token_manager.count_tokens(self.model_name, text_to_count)
        else:
            logger.error("[BaseAgent] TokenManager non disponibile.")
            return None

    @abstractmethod
    def run(self, text: str, custom_prompt: str = None) -> str:
        """
        Metodo astratto che ogni classe derivata deve implementare.
        """
        pass