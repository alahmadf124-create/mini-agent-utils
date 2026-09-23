# mini-agent-utils

A lightweight, dependency-free Python utility toolkit for local AI agents and LLM wrappers.

## Overview

`mini-agent-utils` provides small, practical helpers for agent workflows where simplicity and portability matter.

## Features

- **Prompt formatting**: Convert chat-style role/content messages into a single continuous prompt string.
- **Structured logging**: Emit timestamped event logs for easier local debugging and traceability.
- **No external dependencies**: Built with Python standard library only.

## Included Module

- `mini_agent_utils.py`
  - `PromptFormatter`: Formats message dictionaries and optional system prompts.
  - `AgentLogger`: Prints consistent timestamped logs with event details.

## Quick Start

```python
from mini_agent_utils import PromptFormatter, AgentLogger

messages = [
    {"role": "user", "content": "Summarize this meeting."},
    {"role": "assistant", "content": "Sure, please share your notes."},
]

prompt = PromptFormatter.format_messages(messages, system_prompt="You are concise.")
AgentLogger.log_event("prompt_ready", {"length": len(prompt)})
```

## License

MIT License. See [LICENSE](LICENSE).
