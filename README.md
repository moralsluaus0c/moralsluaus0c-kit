# moralsluaus0c-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m moralsluaus0c_kit.cli --help
```

```python
from moralsluaus0c_kit.core import Moralsluaus0cTool

tool = Moralsluaus0cTool()
print(tool)
```

## Layout

```
moralsluaus0c_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 moralsluaus0c
