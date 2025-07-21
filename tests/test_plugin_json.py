import json
from pathlib import Path


def test_plugin_json_valid():
    plugin_file = Path(__file__).resolve().parents[1] / "plugin.json"
    data = json.loads(plugin_file.read_text())
    assert isinstance(data, dict)
    for key in ("name", "version"):
        assert key in data

