"""Module with formatter stylish."""

TAB = '    '


def render(diff, depth=0):      # noqa: C901
    """Format dict with difference.
    Args:
        diff: dict
        depth: int
    Returns:
        Return formatting difference.
    """
    keys = sorted(diff.keys())
    format_diff = []
    for key in keys:
        if diff[key]['type'] == 'deleted':
            format_diff.append(join_line(
                depth,
                '  - ',
                key,
                format_unchanging(diff[key]['value'], depth + 1),
            ))
        if diff[key]['type'] == 'added':
            format_diff.append(join_line(
                depth,
                '  + ',
                key,
                format_unchanging(diff[key]['value'], depth + 1),
            ))
        elif diff[key]['type'] == 'unchanged':
            format_diff.append(join_line(
                depth,
                TAB,
                key,
                format_unchanging(diff[key]['value'], depth + 1),
            ))
        elif diff[key]['type'] == 'changed':
            format_diff.append(join_line(
                depth,
                '  - ',
                key,
                format_unchanging(diff[key]['value'], depth + 1),
            ))
            format_diff.append(join_line(
                depth,
                '  + ',
                key,
                format_unchanging(diff[key]['value_new'], depth + 1),
            ))
        elif diff[key]['type'] == 'nested':
            format_diff.append(join_line(
                depth,
                TAB,
                key,
                render(diff[key]['value'], depth + 1),
            ))
    return '\n'.join([
        '{',
        *format_diff,
        '{a}{b}'. format(a=TAB * depth, b='}'),
    ])


def join_line(depth, indent, key, mean):
    """Join words in line.
    Args:
        depth: int
        indent: str
        key: str
        mean: str
    Returns:
        Return join line.
    """
    indent_and_key = ''.join([depth * TAB, indent, key, ':'])
    return ' '.join([indent_and_key, str(mean)])


def format_unchanging(dict_unchanged, depth):
    """Format dict without changing.
    Args:
        dict_unchanged: dict
        depth: int
    Returns:
        Return formatting dict.
    """
    objects_to_json = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(dict_unchanged, dict):
        if str(dict_unchanged) in objects_to_json.keys():
            return objects_to_json[str(dict_unchanged)]
        return str(dict_unchanged)
    list_values = []
    for key in dict_unchanged.keys():
        list_values.append(''.join([
            TAB * (depth + 1),
            str(key),
            ': ',
            str(format_unchanging(
                dict_unchanged[key],
                depth=depth + 1,
            )),
        ]))
    return '\n'.join([
        '{',
        *list_values,
        '{a}{b}'.format(a=(TAB * depth), b='}'),
    ])
