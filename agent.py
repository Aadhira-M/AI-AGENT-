
from ollama import chat, ChatResponse
import datetime
import os
import platform
import json
import ast
import operator


# --- Tool Definitions ---

def get_current_time(timezone: str = "local") -> str:
    """Get the current date and time."""

    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely."""

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        elif isinstance(node, ast.BinOp):
            op = allowed_operators.get(type(node.op))
            if op is None:
                raise ValueError("Operator not allowed")
            return op(evaluate(node.left), evaluate(node.right))

        elif isinstance(node, ast.UnaryOp):
            op = allowed_operators.get(type(node.op))
            if op is None:
                raise ValueError("Operator not allowed")
            return op(evaluate(node.operand))

        else:
            raise ValueError("Invalid mathematical expression")

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)
        return str(result)

    except Exception as e:
        return f"Error: {e}"


def read_file(filepath: str) -> str:
    """Read the contents of a file."""

    try:
        with open(filepath, "r") as f:
            content = f.read()

        if len(content) > 3000:
            return content[:3000] + "\n... (truncated)"

        return content

    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."

    except PermissionError:
        return f"Error: Permission denied reading '{filepath}'."

    except Exception as e:
        return f"Error: {e}"


def get_system_info() -> str:
    """Get information about the current system."""

    info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "hostname": platform.node(),
        "working_directory": os.getcwd(),
    }

    return json.dumps(info, indent=2)
# --- Tool Registry ---

TOOLS = [get_current_time, calculate, read_file, get_system_info]

TOOL_REGISTRY = {
    "get_current_time": get_current_time,
    "calculate": calculate,
    "read_file": read_file,
    "get_system_info": get_system_info,
}

# --- System Prompt ---

SYSTEM_PROMPT = """You are a helpful AI assistant with access to tools. 
When a user asks a question, decide whether you need to use a tool to answer it.
You can call multiple tools if needed, and you can call tools multiple times.
Always provide a clear, helpful final answer after using tools."""

# --- Agent Loop ---


# --- Agent Loop ---


def run_agent(user_input: str, messages: list) -> str:
    """Run the agent loop for a single user turn."""
    messages.append({"role": "user", "content": user_input})

    while True:
        response: ChatResponse = chat(
            model="qwen3",
            messages=messages,
            tools=TOOLS,
            think=False,
        )

        messages.append(response.message)

        if not response.message.tool_calls:
            return response.message.content

        # Fixed: Aligned to 8 spaces of indentation
        for tool_call in response.message.tool_calls:
            func_name = tool_call.function.name
            func_args = tool_call.function.arguments

            if func_name in TOOL_REGISTRY:
                print(f" [Tool] Calling {func_name}({func_args})")
                result = TOOL_REGISTRY[func_name](**func_args)
            else:
                result = f"Error: Unknown tool '{func_name}'"

            messages.append({
                "role": "tool",
                "tool_name": func_name,
                "content": str(result),
            })

# --- Interactive Chat ---


def main():
    print("[AI] Agent (type 'quit' to exit)")
    print("   Tools: get_current_time, calculate, read_file, get_system_info")
    print("-" * 50)

    # Initialise conversation with the system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        # Skip empty input
        if not user_input:
            continue
        # Allow the user to quit gracefully
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        # Run the agent and print the response
        response = run_agent(user_input, messages)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    main()
