import json


def process(ast: dict) -> str:
    return json.dumps(ast, indent=2)
