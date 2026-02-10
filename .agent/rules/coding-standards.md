# Coding Standards & "O(1) Request Logic"

## Principles
1. **Strict Mode Everywhere**: All TypeScript must be `strict: true`. All Python must be typed (mypy).
2. **O(1) Request Logic**:
   - Do not inspect token contents in the hot path.
   - Use Redis for all state lookups.
   - Fail fast if quota is exceeded.
3. **M1 Max Optimization**:
   - Prefer multiprocessing over threading for Python logic (GIL avoidance).
   - Use `uvloop` for asyncio where possible.

## Python
```python
# GOOD
def get_model_alias(model_name: str) -> str | None:
    return CACHE.get(model_name)

# BAD
def get_model_alias(model_name):
    # O(N) search
    for m in models:
        if m.name == model_name: return m.alias
```
