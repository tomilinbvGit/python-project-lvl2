"""Function for launch cli-module."""
import argparse
import pathlib


def get_args():
    """Launch cli-module."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output',
    )
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    formatting = args.format
    return file_path1, file_path2, formatting
