## Capability-First Governance

We do not select models by vendor; we select them by **Intelligence Ranking**. If a vendor (e.g., Google) releases a model that beats GitHub's current offering, it MUST move to the top of the `omni-1` chain.

### 1. The "Source of Truth" (Ranking)
To know which model is "better," we rely on the **[LMSYS Chatbot Arena Leaderboard](https://chat.lmsys.org/?leaderboard)**.
- **Rule**: Every month, check the "Overall" and "Coding" rankings.
- **Action**: If a new model (e.g., "DeepSeek-V4") overtakes GPT-4o on the leaderboard, move it to the **Primary** position in `config.yaml`.

### 2. Intent-Based Routing
Instead of hardcoding providers, the gateway uses **Capability Groups**. You can send requests to these intents:

| Intent (Alias) | Goal | Logic |
|---|---|---|
| **`omni-reasoning`** | Maximum Intelligence | Maps to the #1 ranked model on LMSYS. |
| **`omni-creative`** | Nuance & Style | Maps to the #1 ranked "Creative" model (e.g., Claude). |
| **`omni-fast`** | Lowest Latency | Maps to the highest ranked "Small" model (e.g., Llama 8B). |

### 3. Updating the Chain
When a model retirements or a new king emerges:
1. Identify the new "King" on LMSYS.
2. Check if you have access to it (GitHub, Google, or OpenRouter).
3. Update the `omni-1` fallback order:
```yaml
# Example: Moving Gemini to #1 if it beats GPT
- model_name: omni-1
  litellm_params:
    model: gemini/gemini-new-version
    fallbacks: ["github/gpt-4o", ...]
```

## Robustness against "Disappearing" Vendors
The 7-layer chain in `config.yaml` is your **Survival Insurance**. 
- If a vendor disappears, LiteLLM detects the connection error and **instantly jumps to the next most capable model** in the list.
- **Your work never stops.** You simply remove the dead vendor from the config later that day.

