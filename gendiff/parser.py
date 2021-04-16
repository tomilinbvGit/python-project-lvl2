"""Module for open and parse of a file."""
import json

import yaml


def parse(content, suffix):
    """Parse content of a file.
    Args:
        content: content
        suffix: str
    Returns:
        Return content format dict.
    """
    content_of_file = {}
    if suffix == 'json':
        content_of_file = json.loads(content)
    elif suffix == 'yml':
        content_of_file = yaml.safe_load(content)
    if not content_of_file:
        return {}
    return content_of_file
