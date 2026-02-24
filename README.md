# Chain of Responsibility (Python)

Use Chain of Responsibility when:
- More than one object may handle a request, and the handler isn't known first.
- The receiver isn't known explicitly
- Set of objects that can handle a request should be specified dynamically.

## Setup

### Prerequisites

- [uv](https://docs.astral.sh/uv/)

### Install dependencies

With **uv** (from project root):

```bash
uv sync
```

### Run the example

From the project root:

```bash
uv run python simple_example/main.py
```

### Run tests

From the project root:

```bash
uv run pytest
```

Or with an activated venv:

```bash
pytest
```

### Lint

[Ruff](https://docs.astral.sh/ruff/) is used for linting and formatting all Python files. From the project root:

```bash
# Check lint and format
uv run ruff check .
uv run ruff format --check .

# Auto-fix lint issues and apply formatting
uv run ruff check . --fix
uv run ruff format .
```
