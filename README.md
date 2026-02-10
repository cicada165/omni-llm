# Omni-LLM: Unified AI Gateway

A high-performance, cost-effective AI gateway optimized for M1 Max workstations. Consolidates multiple LLM providers into a single, intelligent endpoint.

**Repository**: [github.com/cicada165/omni-llm](https://github.com/cicada165/omni-llm)

## Features
- **Grand Unified Chain (`omni-1`)**: Automatically orchestrates 7 layers of falling back (GitHub Pro -> Perplexity -> Gemini -> Groq -> Mistral -> OpenRouter).
- **Intent-Based Routing**: Decouple apps from vendors using `omni-reasoning`, `omni-creative`, and `omni-fast`.
- **Infinite Context**: Auto-routes payloads > 128k to Gemini 1.5 Pro (2M token window).
- **Sub-Second Latency**: Leverages Groq LPU hardware and Redis semantic caching.
- **Cost Protection**: Global budget guards and primary use of pre-paid/free quotas.

## Getting Started

### 1. Requirements
- Docker & Docker Compose
- Python 3.9+
- Redis (included in compose)

### 2. Setup
1. Clone the repository.
2. Copy `.env.example` to `.env` and add your keys.
3. Start the gateway:
   ```bash
   docker compose up -d
   ```

### 3. Usage
Point your OpenAI-compatible SDKs to:
- **Base URL**: `http://localhost:4000/v1`
- **Model**: `omni-1`
- **Key**: Your master key from `.env`.

## Architecture
- **Proxy**: LiteLLM
- **Cache**: Redis (Semantic)
- **Monitoring**: Built-in health checks in `.agent/skills/verify-gateways/verify.py`

## Maintenance
See [MAINTENANCE.md](MAINTENANCE.md) for strategy on model retirements and capability-based ranking.
