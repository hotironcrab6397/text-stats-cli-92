"""
Utility functions for Text Stats.
"""
import json
from pathlib import Path
from datetime import datetime

def format_output(items, fmt="text"):
    """Format output data."""
    if fmt == "json":
        return json.dumps(items, indent=2, default=str)
    elif fmt == "csv":
        if isinstance(items, list):
            return "\n".join(str(item) for item in items)
        return str(items)
    return str(items)

def read_file(filepath):
    """Read file contents safely."""
    path = Path(filepath)
    if not path.exists():
        return None
    return path.read_text()

def write_file(filepath, content):
    """Write content to file."""
    Path(filepath).write_text(content)

def timestamp():
    """Return current timestamp string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_input(value, expected_type=str):
    """Validate input value."""
    if value is None:
        return False
    try:
        expected_type(value)
        return True
    except (ValueError, TypeError):
        return False
