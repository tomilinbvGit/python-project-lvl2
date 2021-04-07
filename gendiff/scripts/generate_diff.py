import json
from gendiff.scripts.path import abs_path
from gendiff.scripts.list_create import to_list
from gendiff.scripts.sort import sort
from gendiff.scripts.diff import diff


def generate_diff(first_file, second_file):
    file_1 = json.load(open(abs_path(first_file)))
    file_2 = json.load(open(abs_path(second_file)))
    old_keys = to_list(file_1)
    new_keys = to_list(file_2)
    shared_keys = sort(old_keys, new_keys)
    result = diff(shared_keys, file_1, file_2)
    return result
