import json
import yaml


def load_dict_from_path(path: str) -> dict:
    with open(path) as file:
        if path.endswith('.json'):
            return json.load(file)
        else:
            return yaml.safe_load(file)
