import os
import json


class RepositoryContentAggregator:
    """Aggregates the content of files in a repository, excluding specified directories, files, and extensions.
    Each useful file is preceded by a comment with the relative path."""

    def __init__(self, repo_path, excluded_dirs=None, excluded_files=None, prompt_description=None):
        self.repo_path = repo_path
        self.excluded_dirs = excluded_dirs if excluded_dirs is not None else []
        self.excluded_files = excluded_files if excluded_files is not None else []
        self.excluded_extensions = {'.pyc', '.tmp', '.log'}
        self.prompt_description = prompt_description or (
            "The following is the code for an application that summarises and analyses tender specifications.\n"
            "The code is structured as follows:\n"
            "- The content of each file is preceded by a comment indicating the relative path of the file.\n"
        )

    def _is_useful_file(self, filename):
        # Exclude files that belong to specified directories
        if any(part in self.excluded_dirs for part in filename.split(os.sep)):
            return False
            # Exclude specific files
        if os.path.basename(filename) in self.excluded_files:
            return False
            # Exclude files with certain extensions
        if any(filename.endswith(ext) for ext in self.excluded_extensions):
            return False
        return True

    def gather_files_content(self):
        """Walks recursively through the repository and gathers the content of useful files,
        adding a comment with the relative path for each file. Returns a list of strings to write to the output file."""
        combined_content = []
        for root, dirs, files in os.walk(self.repo_path):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in self.excluded_dirs]
            for file in files:
                file_path = os.path.join(root, file)
                if self._is_useful_file(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            file_lines = f.readlines()
                    except Exception as e:
                        # Skip files that cause errors when opening
                        continue

                    relative_path = os.path.relpath(file_path, self.repo_path)
                    # Remove empty lines
                    non_empty_lines = [line for line in file_lines if line.strip()]
                    file_content = f"/* {relative_path} */\n" + ''.join(non_empty_lines)
                    combined_content.append(file_content)
        return combined_content

    def write_combined_content_to_file(self, output_path, combined_content):
        """Writes the prompt description followed by the aggregated content to output_path."""
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(self.prompt_description + "\n")
            output_file.write(''.join(combined_content))

    def aggregate(self):
        """Collects the useful content from the repository and writes it to a file."""
        content = self.gather_files_content()

        return content





