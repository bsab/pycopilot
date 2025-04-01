from agents.base_agent import BaseAgent  # Adjust the import as needed
from agents.drwaio_prompt import user_prompt, system_prompt


class DrawioCodeAgent(BaseAgent):
    def run(self, code: str, custom_prompt: str = None) -> str:

        if custom_prompt:
            prompt = custom_prompt + "Here is the code to analyze:\n" + "\n".join(code)
        else:
            prompt = user_prompt + "Here is the code to analyze:\n" + "\n".join(code)

        # A slightly elevated temperature (e.g., 0.2) may allow for more creative analysis.
        return self.chat_completion(system_prompt=system_prompt, user_prompt=prompt)

