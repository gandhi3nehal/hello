# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Codebase Overview

This is a simple Python codebase with examples demonstrating how to use the Anthropic API with a local Ollama server. The repository contains:

1. Basic Python scripts showing API usage patterns
2. Examples of tool calling functionality with the Claude API

## Repository Structure

- `hello.py` - Simple "Hello World" script
- `first.py` - Basic example of calling the Anthropic API to generate code
- `weather.py` - Example of tool calling with the Anthropic API
- Python scripts connect to a local Ollama server at http://localhost:11434

## Development Commands

There are no specific build or test commands as this is a simple collection of Python scripts. To run any script:

```bash
python filename.py
```

For example:
```bash
python hello.py
python first.py
python weather.py
```

## Architecture Overview

The codebase demonstrates API integration patterns with the Anthropic SDK:

1. All scripts import the `anthropic` package
2. Client initialization uses a local Ollama server as the base URL
3. API key is set to 'ollama' (required but ignored for local Ollama)
4. Examples show:
   - Basic message creation
   - Tool calling patterns with input schemas
   - Processing API responses

## Common Patterns

- All API calls use `client.messages.create()` with similar parameter structures
- Tool calling follows the standard Anthropic pattern with name, description, and input_schema
- Response handling iterates through message.content blocks checking for tool_use types