#!/usr/bin/env python3

from gendiff.scripts.generate_diff import generate_diff
import os.path


def test_diff():
    file_open = open(os.path.abspath('fixtures/test.txt'), 'r')
    result = file_open.read()
    assert result == generate_diff(os.path.abspath('fixtures/file1.json'), os.path.abspath('fixtures/file2.json'))
