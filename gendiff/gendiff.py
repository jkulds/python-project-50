from gendiff.ast_builder import generate_ast
from gendiff.formatters import stylish_formatter, \
    json_formatter, plain_formatter
from gendiff.parser import load_dict_from_path

OUT_FORMATTER_BY_FORMAT = {
    'stylish': stylish_formatter,
    'json': json_formatter,
    'plain': plain_formatter
}


def generate_diff(path1: str, path2: str, out_format: str = "stylish") -> str:
    dict1 = load_dict_from_path(path1)
    dict2 = load_dict_from_path(path2)

    diffs = generate_ast(dict1, dict2)

    result = OUT_FORMATTER_BY_FORMAT[out_format].process(diffs)

    return result
