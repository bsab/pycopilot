from utils.common import load_config, write_text_to_file
from utils.repo_content_aggregator import RepositoryContentAggregator
from agents.pythoncode_agent import PythonCodeAgent
from agents.drwaio_agent import DrawioCodeAgent


def select_agent(agent_name, config_section, agent_config_path):
    """Selects and returns the agent based on the agent_name parameter."""
    if agent_name.lower() == "drawiocode":
        return DrawioCodeAgent(config_section=config_section, config_path=agent_config_path)
    return PythonCodeAgent(config_section=config_section, config_path=agent_config_path)


def main():
    # Load configuration from an external file (e.g., config.json)
    config = load_config('config.json')

    # Extract configuration parameters with default values if not present
    repo_path = config.get("repo_path", ".")
    excluded_dirs = config.get("excluded_dirs", [])
    excluded_files = config.get("excluded_files", [])
    output_path = config.get("output_path", "output.txt")
    agent_name = config.get("agent_name", "PythonCode")
    agent_prompt = config.get("agent_prompt", "")
    config_section = config.get("config_section", "test_agent")
    agent_config_path = config.get("agent_config_path", "/Users/sab/PycharmProjects/pycopilot/config.yaml")

    # Aggregate the content of the repository
    aggregator = RepositoryContentAggregator(repo_path, excluded_dirs, excluded_files)
    aggregated_content = aggregator.aggregate()

    # Select and configure the agent based on the configuration
    agent = select_agent(agent_name, config_section, agent_config_path)

    # Run the agent on the aggregated content with the custom prompt
    results = agent.run(code=aggregated_content, custom_prompt=agent_prompt)

    # Write the result to the output file
    write_text_to_file(output_path, results)

    print("completed!")


if __name__ == '__main__':
    main()