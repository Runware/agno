# Runware Cookbook

This cookbook demonstrates how to use Runware with the Agno framework. Runware exposes an
OpenAI-compatible chat completions API (`https://api.runware.ai/v1`) alongside its native
media-generation API.

> **Prerequisites**: Fork and clone this repository if needed

## Quick Start

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `RUNWARE_API_KEY`

Get an API key from the Runware dashboard (https://runware.ai).

```shell
export RUNWARE_API_KEY=***
```

### 3. Install libraries

```shell
uv pip install -U openai ddgs agno
```

### 4. Run basic Agent

```shell
python cookbook/90_models/runware/basic.py
```

### 5. Run Agent with Tools

```shell
python cookbook/90_models/runware/tool_use.py
```

### 6. Run Agent that returns structured output

```shell
python cookbook/90_models/runware/structured_output.py
```

## Model Ids

The examples use `openai-gpt-5-mini`. The endpoint lists the current models at
`GET /v1/models`, and the catalog is at https://runware.ai/docs/models-api/introduction.

The base URL can be overridden with the `RUNWARE_BASE_URL` environment variable, which is
useful when routing through a proxy:

```shell
export RUNWARE_BASE_URL=https://api.runware.ai/v1
```

## Resources & Support

### Official Links
- [Website](https://runware.ai)
- [Models API Introduction](https://runware.ai/docs/models-api/introduction)
- [Compatible APIs](https://runware.ai/docs/tools/compatible-apis)

### API Reference
- **Base URL**: `https://api.runware.ai/v1`
- **Models Endpoint**: `https://api.runware.ai/v1/models`
