"""Function for determines the difference in files."""

from gendiff.parser import parse
from gendiff.formatters import json as json_format
from gendiff.formatters import plain, stylish

FORMATS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """Generate difference and formatting.

    Args:
        file_path1: path
        file_path2: path
        formatter: module

    Returns:
        Return formatting difference files.
    """
    return FORMATS[formatter].render(
        get_diff(
            parse(read_file(file_path1), get_format(file_path1)),
            parse(read_file(file_path2), get_format(file_path2)),
        ),
    )


def get_format(file_path):
    """Get format of file.

    Args:
        file_path: path

    Returns:
        Return suffix of file.
    """
    return str(file_path).rsplit('.', 1)[-1]


def read_file(file_path):
    """Open file.

    Args:
        file_path: path

    Returns:
        Return content of a file.
    """
    path = str(file_path)
    with open(path, 'r') as infile:
        content = infile.read()
    return content


def get_diff(file1, file2):
    """Determine the difference in files.

    Args:
        file1: dict
        file2: dict

    Returns:
        Return dict with difference.
    """
    tree_diff = {}
    keys = file1.keys() | file2.keys()
    for key in keys:
        node = {}
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key not in file2.keys():
            node['type'] = 'deleted'
            node['value'] = value1
        elif key not in file1.keys():
            node['type'] = 'added'
            node['value'] = value2
        elif value1 == value2:
            node['type'] = 'unchanged'
            node['value'] = value1
        elif all([
            value1 != value2,
            isinstance(value1, dict),
            isinstance(value2, dict),
        ]):
            node['value'] = get_diff(value1, value2)
            node['type'] = 'nested'
        else:
            node['type'] = 'changed'
            node['value'] = value1
            node['value_new'] = value2
        tree_diff[key] = node
    return tree_diff
