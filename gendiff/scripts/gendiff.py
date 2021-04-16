"""Script for launch gendiff cli."""
from gendiff.cli import get_args
from gendiff.gendiff import generate_diff


def main():
    """Launch gendiff cli.
    Returns:
        Return cli.
    """
    return print(generate_diff(*get_args()))


if __name__ == '__main__':
    main()
