import tempfile
from pathlib import Path

from moralsluaus0c_kit.core import Moralsluaus0cTool


def test_plan_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        assert Moralsluaus0cTool(tmp).plan() == []


def test_category_of_known_and_unknown():
    sorter = Moralsluaus0cTool(".")
    assert sorter.category_of("a.png") == "images"
    assert sorter.category_of("a.unknown") == "other"


def test_apply_moves_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "note.md").write_text("hi", encoding="utf-8")
        moved = Moralsluaus0cTool(tmp).apply()
        assert moved == [("note.md", "docs")]
        assert Path(tmp, "docs", "note.md").is_file()
