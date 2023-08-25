from gendiff.enum.StateEnum import StateEnum

TEMPLATES = {
    StateEnum.Added: "Property '{key}' was added with value: {value}",
    StateEnum.Removed: "Property '{key}' was removed",
    StateEnum.Changed: "Property '{key}' was updated. From {old} to {new}",
    StateEnum.Children: "Property '{key}' was added with value: [complex value]"
}


def process(ast: dict) -> str:
    result = get_plain_lines(ast, [], '')

    return '\n'.join(result)


def get_plain_lines(ast: dict, acc: list, parent: str) -> list:
    for key, value in ast.items():
        state = value[0]
        path = '.'.join([parent, key]) if parent != '' else key
        val = get_string_value(value[1])
        line = None
        match state:
            case StateEnum.Added:
                line = TEMPLATES[state].format(key=path, value=val)
            case StateEnum.Removed:
                line = TEMPLATES[state].format(key=path, value=val)
            case StateEnum.Changed:
                val2 = get_string_value(value[2])
                line = TEMPLATES[state].format(key=path, old=val, new=val2)
            case StateEnum.Children:
                get_plain_lines(value[1], acc, path)

        if line:
            acc.append(line)

    return acc


def get_string_value(value) -> str:
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, int) or isinstance(value, float):
        return str(value)

    if value is None:
        return "null"

    return f"'{value}'"
