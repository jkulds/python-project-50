import json
import yaml


def get_dicts_from_file(path1: str, path2: str):
    dict1 = get_sorted_dict_from_path(path1)
    dict2 = get_sorted_dict_from_path(path2)

    return dict1, dict2


def get_sorted_dict_from_path(path: str) -> dict:
    if path.endswith('.json'):
        result = json.load(open(path))
    else:
        result = yaml.safe_load(open(path))

    result = sorted_dict(result)

    return result


def sorted_dict(d: dict):
    return dict(sorted(d.items(), key=lambda x: x[0]))
