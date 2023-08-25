from gendiff.enum.StateEnum import StateEnum

TEMPLATES = {
    StateEnum.Added: "{blank}+ {key}: {value}\n",
    StateEnum.Removed: "{blank}- {key}: {value}\n",
    StateEnum.Changed: "{blank}- {key}: {old}\n{blank}+ {key}: {new}\n",
    StateEnum.Children: "  {blank}{key}: {open}\n{value}{close}\n",
    StateEnum.Unchanged: "{blank}  {key}: {value}\n"
}


def process(ast: dict) -> str:
    result = get_lines_from_ast(ast, 2)
    return "{\n" + result + "}"


def get_lines_from_ast(ast: dict, indent) -> str:
    result = []
    blank = " " * indent

    for key, value in ast.items():
        state = value[0]
        match state:
            case StateEnum.Children:
                line = get_lines_from_ast(value[1], indent + 4)
                line = TEMPLATES[state].format(blank=blank,
                                               key=key,
                                               open="{",
                                               value=line,
                                               close=" " * (indent + 2) + "}")
            case StateEnum.Changed:
                old = process_value(value[1], indent)
                new = process_value(value[2], indent)
                line = TEMPLATES[state].format(blank=blank,
                                               key=key,
                                               old=old,
                                               new=new)
            case _:
                value_string = process_value(value[1], indent)
                line = TEMPLATES[state].format(blank=blank,
                                               key=key,
                                               value=value_string)

        result.append(line)

    return ''.join(result)


def process_value(param, indent: int):
    if not isinstance(param, dict):
        return get_string_value(param)

    blank = " " * (indent + 6)
    lines = []
    for key, value in param.items():
        if isinstance(value, dict):
            v = process_value(value, indent + 4)
        else:
            v = value
        line = f"{blank}{key}: {v}\n"
        lines.append(line)

    return "{\n" + "".join(lines) + " " * (indent + 2) + "}"


def get_string_value(value):
    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, int) or isinstance(value, float):
        return str(value)

    if value is None:
        return "null"

    return f"{value}"
