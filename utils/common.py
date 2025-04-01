import os
import json
import logging
import yaml

# Set up a module-level logger that can be used by all helper functions.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# You can adjust or configure handlers as needed.
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def create_directory(path: str) -> None:
    """
    Creates a directory if it does not exist.

    Parameters:
      path (str): Path of the directory to be created.

    Exceptions are logged.
    """
    try:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created or already exists: {path}")
    except Exception as e:
        logger.error(f"Error creating directory '{path}': {e}")
        raise


def write_text_to_file(file_path: str, text: str) -> str:
    """
    Writes the given text to the specified file.

    Parameters:
      file_path (str): Destination file path.
      text (str): Text content to be written.

    Returns:
      file_path (str)

    Exceptions are logged.
    """
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            create_directory(dir_path)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        logger.info(f"File written successfully: {file_path}")
    except Exception as e:
        logger.error(f"Error writing file '{file_path}': {e}")
        raise
    return file_path


def read_text_from_file(file_path: str) -> str:
    """
    Reads and returns the content of a file.

    Parameters:
      file_path (str): Path to the file.

    Returns:
      content (str)

    Exceptions are logged.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        logger.info(f"File read successfully: {file_path}")
        return content
    except Exception as e:
        logger.error(f"Error reading file '{file_path}': {e}")
        raise


def load_yaml_config(config_path: str) -> dict:
    """
    Loads a YAML configuration file and returns its contents as a dictionary.

    Parameters:
      config_path (str): Path to the YAML file.

    Returns:
      config (dict)

    Exceptions are logged.
    """
    if not os.path.exists(config_path):
        msg = f"Configuration file not found: {config_path}"
        logger.error(msg)
        raise FileNotFoundError(msg)
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        if config is None:
            msg = f"Configuration file '{config_path}' is empty or malformatted."
            logger.error(msg)
            raise ValueError(msg)
        logger.info(f"Configuration loaded successfully from: {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading YAML file '{config_path}': {e}")
        raise


def write_json_file(file_path: str, data: dict) -> str:
    """
    Writes a dictionary to a JSON file.

    Parameters:
      file_path (str): Destination file path.
      data (dict): Data to be written as JSON.

    Returns:
      file_path (str)

    Exceptions are logged.
    """
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            create_directory(dir_path)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"JSON file written successfully: {file_path}")
    except Exception as e:
        logger.error(f"Error writing JSON file '{file_path}': {e}")
        raise
    return file_path

def load_config(config_file):
    """Loads configuration from a JSON file."""
    with open(config_file, "r", encoding='utf-8') as f:
        config = json.load(f)
    return config