import json

from gendiff.parser import get_dicts_from_file


def generate_diff(path1: str, path2: str) -> str:
    dict1, dict2 = get_dicts_from_file(path1, path2)
    diffs = {}
    fill_first(diffs, dict1, dict2)
    fill_second(diffs, dict1, dict2)

    result = json.dumps(diffs, indent=2).replace(",", "").replace("\"", "")
    return result


def fill_second(diffs, dict1, dict2):
    for (key, value) in dict2.items():
        if key not in dict1 or key in dict1 and dict1[key] != value:
            diffs[f"+ {key}"] = str(value).lower()


def fill_first(diffs: dict, dict1: dict, dict2: dict) -> None:
    for (key, value) in dict1.items():
        sign = ' '
        if key not in dict2 or key in dict2 and dict2[key] != value:
            sign = '-'

        diffs[f"{sign} {key}"] = str(value).lower()
