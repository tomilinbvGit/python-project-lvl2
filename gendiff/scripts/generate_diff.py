import json
import yaml
from gendiff.scripts.path import abs_path
from gendiff.scripts.sort import sort
from gendiff.scripts.diff import diff


def generate_diff(first_file, second_file):
    if first_file.endswith('.json') and second_file.endswith('.json'):
        file_1 = json.load(open(abs_path(first_file)))
        file_2 = json.load(open(abs_path(second_file)))
    else:
        file_1 = yaml.load(open(abs_path(first_file)), Loader=yaml.FullLoader)
        file_2 = yaml.load(open(abs_path(second_file)), Loader=yaml.FullLoader)
    old_keys = list(file_1.keys())
    new_keys = list(file_2.keys())
    shared_keys = sort(old_keys, new_keys)
    result = diff(shared_keys, file_1, file_2)
    return result
