#!/usr/bin/env python3
"""
Minimal dependency-free chat interface for LLM at localhost:1234
"""
import json
import sys
import urllib.request
import urllib.error
import os


def load_system_prompt():
    """Load system prompt from config file if it exists."""
    config_path = os.path.expanduser("~/.llmchat")

    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                return f.read().strip()
        except Exception as e:
            print(f"Warning: Could not read config file {config_path}: {e}")
            return None
    return None


def send_message(message, history):
    """Send a message to the LLM and return the response."""
    url = "http://localhost:1234/v1/chat/completions"

    # Build messages with history
    messages = history + [{"role": "user", "content": message}]

    data = {
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2048,
        "stream": False,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.3
    }

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']

    except urllib.error.URLError as e:
        return f"Error: Could not connect to LLM at {url}. Make sure it's running.\n{e}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"Error: Unexpected response format from LLM.\n{e}"


def main():
    """Main chat loop."""
    print("Chat Interface - Connected to localhost:1234")
    print("Type 'exit', 'quit', or press Ctrl+C to end the conversation.\n")

    # Load system prompt if configured
    history = []
    system_prompt = load_system_prompt()
    if system_prompt:
        history.append({"role": "system", "content": system_prompt})
        print(f"[System prompt loaded from ~/.llmchat]\n")

    try:
        while True:
            # Get user input
            try:
                user_input = input("You: ").strip()
            except EOFError:
                print("\nGoodbye!")
                break

            if not user_input:
                continue

            # Check for exit commands
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            # Send message and get response
            response = send_message(user_input, history)

            # Display response
            print(f"\nAssistant: {response}\n")

            # Update history
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": response})

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
