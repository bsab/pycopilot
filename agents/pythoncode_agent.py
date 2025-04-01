from agents.base_agent import BaseAgent  # Adjust the import as needed
from utils.common import logger

class PythonCodeAgent(BaseAgent):
    def run(self, code: str, custom_prompt: str = None) -> str:
        # Define a system prompt tailored for analyzing Python code.
        system_prompt = (
            "You are a Python code optimization expert. Your task is to review the Python code provided, "
            "identify any potential syntax errors, logical issues, and suggest improvements regarding style and performance. "
            #"Generate an optimized Python script without changing function signatures and structures. "
            "Provide clear, detailed feedback and recommendations in the comments."
            #"Ensure that all code, comments, prompts, and method names are written in English."
        )


        user_prompt = f"{custom_prompt} within this code:\n\n" + "\n".join(code)

        # A slightly elevated temperature (e.g., 0.2) may allow for more creative analysis.
        logger.info("PythonCodeAgent is running... please wait!")
        return self.chat_completion(system_prompt=system_prompt,
                                    user_prompt=user_prompt)
