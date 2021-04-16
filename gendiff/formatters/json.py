"""Module with formatter stylish."""

import json


def render(diff):
    """Format dict with difference.
    Args:
        diff: dict
    Returns:
        Return formatting difference.
    """
    return json.dumps(diff)
