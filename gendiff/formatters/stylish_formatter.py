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
                old = get_value_string(value[1], indent)
                new = get_value_string(value[2], indent)
                line = TEMPLATES[state].format(blank=blank, key=key, old=old, new=new)
            case _:
                value_string = get_value_string(value[1], indent)
                line = TEMPLATES[state].format(blank=blank, key=key, value=value_string)

        result.append(line)

    return ''.join(result)


def get_value_string(param, indent: int):
    if not isinstance(param, dict):
        if isinstance(param, bool):
            return str(param).lower()

        if isinstance(param, int) or isinstance(param, float):
            return str(param)

        if param is None:
            return "null"

        return f"{param}"

    blank = " " * (indent + 6)
    lines = []
    for key, value in param.items():
        v = get_value_string(value, indent + 4) if isinstance(value, dict) else value
        line = f"{blank}{key}: {v}\n"
        lines.append(line)

    return "{\n" + "".join(lines) + " " * (indent + 2) + "}"
