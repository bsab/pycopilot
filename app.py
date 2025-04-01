from utils.common import load_config, write_text_to_file
from utils.repo_content_aggregator import RepositoryContentAggregator

from agents.pythoncode_agent import PythonCodeAgent
from agents.drwaio_agent import DrawioCodeAgent

if __name__ == '__main__':
    # Load configuration from an external file (e.g., config.json)
    config = load_config('config.json')

    repo_path = config.get("repo_path", ".")
    excluded_dirs = config.get("excluded_dirs", [])
    excluded_files = config.get("excluded_files", [])
    output_path = config.get("output_path", "output.txt")
    agent_name = config.get("agent_name", ".")
    agent_prompt = config.get("agent_prompt", "")

    aggregator = RepositoryContentAggregator(repo_path, excluded_dirs, excluded_files)
    content = aggregator.aggregate()

    config_section = "test_agent"

    if agent_name == "DrawioCode":
        agent = DrawioCodeAgent(config_section=config_section,
                                config_path="/Users/sab/PycharmProjects/pycopilot/config.yaml")
    else:
        agent = PythonCodeAgent(config_section=config_section,
                                config_path="/Users/sab/PycharmProjects/pycopilot/config.yaml")

    results = agent.run_agent(code=content, custom_prompt=agent_prompt)

    write_text_to_file(output_path, results)

    print("completed!")





