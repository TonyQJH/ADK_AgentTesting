# ADK_AgentTesting

A collection of examples demonstrating how to build and test agents using the Google ADK.

## Repository Structure

- **coding_agent/**  
  Example of a basic LLM-powered coding assistant.

- **multi_tool_agent/**  
  Example of an agent using multiple external tools.

- **test_agent/**  
  Collection of scripts to validate and benchmark agent behaviors.

## Prerequisites

- Python 3.11

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/ADK_AgentTesting.git
   cd ADK_AgentTesting
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
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
