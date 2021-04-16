"""Module of tests formatters."""
import pathlib
import json

import pytest

from gendiff import gendiff


@pytest.mark.parametrize('file1,file2,expected_file,formatter', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_file1_file2_stylish.txt',
     'stylish'
     ),
    ('tests/fixtures/file_nested1.json',
     'tests/fixtures/file_nested2.json',
     'tests/fixtures/expected_nested_files_stylish.txt',
     'stylish',
     ),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_file1_file2_plain.txt',
     'plain'
     ),
    ('tests/fixtures/file_nested1.json',
     'tests/fixtures/file_nested2.json',
     'tests/fixtures/expected_nested_files_plain.txt',
     'plain',
     ),
])
def test_generate_diff(file1, file2, expected_file, formatter):
    """Test formatters."""
    with open(expected_file) as infile:
        expected = infile.read()
    diff = gendiff.generate_diff(
        pathlib.Path(file1),
        pathlib.Path(file2),
        formatter=formatter
    )
    assert diff == expected


@pytest.mark.parametrize('file1,file2,expected_file', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_file1_file2.json',
     ),
    ('tests/fixtures/file_nested1.json',
     'tests/fixtures/file_nested2.json',
     'tests/fixtures/expected_nested_files.json',
     ),
])
def test_generate_diff_json(file1, file2, expected_file):
    """Test formatter json."""
    expected = json.loads(gendiff.read_file(pathlib.Path(expected_file)))
    diff = gendiff.generate_diff(
        pathlib.Path(file1),
        pathlib.Path(file2),
        formatter='json',
    )
    assert json.loads(diff) == expected
