# CLI Chat Interface

A minimal, dependency-free chat interface for LLMs running at localhost:1234.

## Features

- Zero dependencies (uses only Python standard library)
- Simple command-line interface
- Conversation history support
- User-configurable system prompt
- Clean and minimal design

## Requirements

- Python 3.x
- An LLM server running at `http://localhost:1234`

## Usage

### Option 1: Run directly from this directory

```bash
./llmchat
```

### Option 2: Add to your PATH

```bash
# Add this directory to your PATH
export PATH="$PATH:/path/to/cli-chat"

# Now you can run from anywhere
llmchat
```

### Option 3: Run the Python script directly

```bash
python3 chat.py
```

## Configuration

### System Prompt

You can set a custom system prompt by creating a `~/.llmchat` file with your desired prompt:

```bash
echo "You are a helpful assistant that responds concisely." > ~/.llmchat
```

The system prompt will be automatically loaded when you start the chat interface. If the file doesn't exist, no system prompt is used.

**Example system prompts:**

```bash
# Concise assistant
echo "You are a helpful assistant. Always respond concisely and to the point." > ~/.llmchat

# Code expert
echo "You are an expert programmer. Provide clear, well-documented code examples." > ~/.llmchat

# Creative writer
echo "You are a creative writing assistant. Help users craft engaging stories and content." > ~/.llmchat
```

To edit your system prompt:
```bash
nano ~/.llmchat
# or
vim ~/.llmchat
```

To remove the system prompt:
```bash
rm ~/.llmchat
```

## Commands

- Type your message and press Enter to chat
- Type `exit` or `quit` to end the conversation
- Press `Ctrl+C` to quit

## Example

```
Chat Interface - Connected to localhost:1234
Type 'exit', 'quit', or press Ctrl+C to end the conversation.

You: Hello!