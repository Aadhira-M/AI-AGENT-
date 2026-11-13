# Python AI Agent Using Ollama

## Overview

This project is a **tool-enabled AI Agent** developed using Python and Ollama. It uses the **Qwen3 large language model (LLM)** to understand user queries, decide when tools are required, execute the appropriate functions, and generate meaningful responses.

Unlike a basic chatbot, this AI agent can interact with the local system and perform tasks such as mathematical calculations, retrieving the current date and time, reading files, and gathering system information.

## Features

The AI agent supports the following tools:

| Tool | Description |
|---|---|
| `get_current_time` | Retrieves the current date and time. |
| `calculate` | Performs mathematical calculations using safe expression evaluation. |
| `read_file` | Reads the contents of a specified file. |
| `get_system_info` | Retrieves operating system, architecture, Python version, hostname, and working directory. |

### Key Capabilities

- **LLM Integration:** Uses the Qwen3 model through Ollama.
- **Tool Calling:** Automatically identifies and invokes tools based on user queries.
- **Conversation Memory:** Maintains conversation history during an interactive session.
- **Safe Calculation:** Uses Python's AST module to restrict mathematical operations.
- **Error Handling:** Handles missing files, permission errors, and invalid expressions.
- **Interactive Chat:** Supports continuous conversations through the terminal.

## Technologies Used

- **Python** – Core programming language.
- **Ollama** – Runs the local language model.
- **Qwen3** – Language model used for reasoning and tool selection.
- **AST (Abstract Syntax Tree)** – Used for safe mathematical expression evaluation.
- **JSON** – Handles structured system information.
- **Python Libraries:** `datetime`, `os`, `platform`, `json`, `ast`, and `operator`.

## Project Architecture

The agent follows a tool-calling workflow:

```text
          User Input
               |
               v
       Python AI Agent
               |
               v
        Ollama (Qwen3)
               |
               v
       Analyze User Query
               |
               v
       Is a Tool Required?
          /         \
        Yes          No
         |            |
         v            v
   Tool Selection   Generate
         |          Response
         v
   Execute Python
       Function
         |
         v
   Return Tool Result
         |
         v
    Ollama (Qwen3)
         |
         v
    Final Response
         |
         v
        User
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.9 or later
- Ollama installed
- Qwen3 model downloaded
- Basic knowledge of Python

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Install Ollama

Download and install Ollama from:

https://ollama.com/

### 3. Download the Qwen3 Model

Open your terminal and execute:

```bash
ollama pull qwen3
```

### 4. Install Python Dependency

```bash
pip install ollama
```

### 5. Run the AI Agent

Save the Python code as `agent.py` and execute:

```bash
python agent.py
```

## Usage

Once the program starts, you can interact with the AI agent through the terminal.

**Example queries:**

| User Query | Expected Action |
|---|---|
| What time is it now? | Calls `get_current_time` |
| Calculate 25 * 4 + 10 | Calls `calculate` |
| Read the file test.txt | Calls `read_file` |
| Give me my system information | Calls `get_system_info` |
| Explain what an AI agent is | Responds using the LLM |

### Sample Output

```text
[AI] Agent (type 'quit' to exit)

Tools: get_current_time, calculate,
read_file, get_system_info

--------------------------------------------------

You: Calculate 25 * 4 + 10

[Tool] Calling calculate(...)

Agent: The result is 110.

You: What time is it?

[Tool] Calling get_current_time(...)

Agent: The current date and time is ...

You: quit

Goodbye!
```



## Project Structure

```text
Python-AI-Agent/
│
├── agent.py
└── README.md
```

## How It Works

1. The user enters a query through the terminal.
2. The query is sent to the Qwen3 model using Ollama.
3. The model determines whether an available tool is required.
4. If a tool is needed, the agent identifies the function and its arguments.
5. The corresponding Python function is executed.
6. The tool result is returned to the model.
7. The model generates a final response for the user.
8. The conversation continues until the user enters `quit` or `exit`.

## Learning Outcomes

Through this project, I explored:

- Building AI agents using Python.
- Integrating local LLMs using Ollama.
- Understanding function calling and tool execution.
- Implementing an agent loop.
- Managing conversation history.
- Using Python libraries for system-level operations.


## Author

**Aadhira M**

Computer Science and Engineering Student

---

*This project demonstrates how Python and locally hosted language models can be combined to build an AI agent capable of performing practical tasks through tool calling.*
