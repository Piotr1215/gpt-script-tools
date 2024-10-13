# Script Orchestrator

## Overview

The Script Orchestrator is a tool designed to facilitate the creation, testing, and management of bash scripts. It leverages several sub-tools to streamline the process, ensuring scripts are created based on user input, verified for errors, and properly named and saved.

## Components

### 1. script_orchestrator

- **Description**: Orchestrates the creation and testing of bash scripts.
- **Tools Used**: shellcheck, script_creator, file_namer, content_getter, sessions_wiper.
- **Workflow**:
  1. Collects user input for script creation or modification.
  2. Uses `script_creator` to generate the script.
  3. Saves the script and runs `shellcheck` for verification.
  4. Asks the user if the script should be saved and made executable.

### 2. script_creator

- **Description**: Creates a script based on user input.
- **Usage**: Takes user instructions and generates a bash script using the `fabric` tool.

### 3. shellcheck

- **Description**: Verifies scripts for errors and warnings.
- **Usage**: Utilizes the `shellcheck` command-line tool to ensure script quality.

### 4. file_namer

- **Description**: Names and saves the script created by the scripter.
- **Usage**: Chooses a random file name that fits the script content.

### 5. content_getter

- **Description**: Asks the user for relevant input.
- **Usage**: Prompts the user to provide necessary details for script creation.

### 6. sessions_wiper

- **Description**: Wipes all fabric sessions.
- **Usage**: Ensures a clean state by clearing all active sessions in `fabric`.

## Additional Tools

### shellcheck

- **Description**: Provides help text for the `shellcheck` CLI.
- **Usage**: Displays help and usage information for verifying shell scripts.

### fabric

- **Description**: Provides help text for the `fabric` CLI and available prompts.
- **Usage**: Displays help and usage information for `fabric`, which is used in script creation.

## Getting Started

1. **Install Dependencies**: Ensure `shellcheck` and `fabric` are installed on your system.
2. **Run the Orchestrator**: Use the `script_orchestrator` to start creating and managing scripts.
3. **Verify Scripts**: Use `shellcheck` to check scripts for errors and warnings.
4. **Manage Sessions**: Use `sessions_wiper` to clear any active `fabric` sessions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
