# PyCopilot

PyCopilot is a Python-based tool that aggregates the content of a repository and uses specialized agents to analyze Python code, optimize it, and even generate Draw.io diagrams representing architecture. It leverages state-of-the-art large language models (LLMs) and provides detailed recommendations to improve code quality, style, and performance.

![logo](logo-pycopilot.png)

## Overview

- **Repository Aggregator:** Collects and aggregates content from the project files. Excludes specified directories and files to avoid redundant data (e.g., version control files, images, or unwanted extensions).
- **Agents:** 
  - **PythonCodeAgent:** Analyzes Python code for syntax and logical errors while suggesting improvements regarding style and performance.
  - **DrawioCodeAgent:** Generates a Draw.io XML diagram illustrating an AWS-based architecture based on the provided Python code.
- **LLM Backend:** Uses cloud-based LLM APIs (e.g., OpenAI, AWS Bedrock, or Anthropic Bedrock) to generate responses during code analysis.
- **TokenManager:** Keeps track of token usage and estimated costs when interacting with external LLM providers.

## Installation

1. **Clone the Repository**  
   Use Git to clone the repository:
   > git clone https://github.com/yourusername/pycopilot.git

2. **Create a Virtual Environment (Recommended)**  
   > python3 -m venv .venv  
   > source .venv/bin/activate  (Linux/Mac)  
   > .venv\Scripts\activate     (Windows)

3. **Install Dependencies**  
   The required packages are listed in `requirements.txt`. To install them, run:
   > pip install -r requirements.txt

## Configuration Files

- **config.json**  
  Contains settings such as the repository path, agent name, excluded directories/files, output file path, and agent prompt. Edit this file to suit your project needs.

- **config.yaml**  
  Provides agent-specific configuration details (for example, API credentials, endpoints, and model names for providers like OpenAI or AWS). Make sure your credentials and endpoints are correctly configured.

## Usage

To run the application, use the following command from the project root:

> python app.py

The process will:
• Load the configurations from `config.json` and `config.yaml`.
• Aggregate the repository content by skipping excluded directories and files.
• Select and run the appropriate agent (PythonCodeAgent by default) using a custom prompt (e.g., “provide a README file”).
• Write the resulting output to the specified output file (`pythoncode_output.txt` by default).

## Code Structure

- **requirements.txt:**  
  Lists all required third-party libraries (including langchain, transformers, torch, etc.).

- **config.json & config.yaml:**  
  Provide project-wide and agent-specific configurations, respectively.

- **app.py:**  
  Main entry point that loads configuration, aggregates code from the repository, selects the appropriate agent, and writes the analysis output to a file.

- **agents/**  
  Contains agent classes, including:
  - *base_agent.py:* Defines an abstract agent with common methods (client creation, chat completions, token counting, etc.).
  - *pythoncode_agent.py:* Specializes in analyzing Python code and offering optimization recommendations.
  - *drwaio_agent.py & drwaio_prompt.py:* Generate Draw.io diagrams to visually represent system architectures.

- **utils/**  
  Holds various helper functions for:
  - File I/O and directory creation (in *common.py*).
  - Aggregating repository content (in *repo_content_aggregator.py*).
  - Managing tokens and cost calculations (under *token_manager*).

## Contributing

Bug reports and pull requests are welcome. If you wish to contribute to the codebase:
1. Fork the repository.
2. Create a feature branch.
3. Write tests when applicable.
4. Submit a pull request with a detailed explanation of your changes.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

For issues, questions, or suggestions, please open an issue or contact the repository maintainer.