# ADK_AgentTesting

A collection of examples demonstrating how to build and test agents using the Google ADK.
https://google.github.io/adk-docs/

## Repository Structure

- **coding_agent/**  
  Example of a basic LLM-powered coding assistant.

- **Tutorial_agent_CN_EN/**  
  Example of an agent using multiple external tools.

- **test_agent/**  
  Collection of scripts to validate and benchmark agent behaviors.

- **Simple_agent/**  
  Example of a simple agent.

- **IMPORTANT.md**  
  Important notes about the ADK for using Local LLMs.

## Prerequisites

- Python 3.11

## Setup

1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install google-adk
   ```
## Usage

You need to move the file from the test_agent directory to the related directory. Then you can run an agent example:

- **coding_agent**  
  ```bash
  cd ADK_AgentTesting
  adk web
  (Choose the coding_agent at the top)
  ```

- **Tutorial_agent_CN_EN**  
  ```bash
  cd ADK_AgentTesting
  adk web
  (Choose the Tutorial_agent_CN_EN at the top)
  ```

- **Simple_agent**  
  ```bash
  cd ADK_AgentTesting
  adk web
  (Choose the Simple_agent at the top)
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the Apache 2.0 License.
