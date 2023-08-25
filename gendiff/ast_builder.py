from gendiff.enum.StateEnum import StateEnum


def generate_ast(dict1: dict, dict2: dict) -> dict:
    dict1_keys = set(dict1)
    dict2_keys = set(dict2)

    removed = dict1_keys - dict2_keys
    added = dict2_keys - dict1_keys

    result = {}

    for i in removed:
        result[i] = (StateEnum.Removed, dict1[i])

    for i in added:
        result[i] = (StateEnum.Added, dict2[i])

    equal_dict = process_equal_keys(dict1, dict2)
    result.update(equal_dict)

    return dict(sorted(result.items(), key=lambda x: x))


def process_equal_keys(dict1, dict2):
    result = {}
    equals = set(dict1) & set(dict2)
    for i in equals:
        if isinstance(dict1[i], dict) and isinstance(dict2[i], dict):
            result[i] = (StateEnum.Children, generate_ast(dict1[i], dict2[i]))
        elif dict1[i] == dict2[i]:
            result[i] = (StateEnum.Unchanged, dict1[i])
        else:
            result[i] = (StateEnum.Changed, dict1[i], dict2[i])
    return result
