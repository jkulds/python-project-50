import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format",
                        type=list, help="set format of output")
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()

    dict1 = get_sorted_dict_from_json(args.first_file)
    dict2 = get_sorted_dict_from_json(args.second_file)

    diffs = generate_diff(dict1, dict2)

    return diffs


def get_sorted_dict_from_json(path: str) -> dict:
    result = json.load(open(path))
    result = sorted_dict(result)
    return result


def generate_diff(dict1: dict, dict2: dict) -> str:
    diffs = []
    fill_first(diffs, dict1, dict2)
    fill_second(diffs, dict1, dict2)

    return '\n'.join(diffs)


def fill_second(diffs, dict1, dict2):
    for (k, v) in dict2.items():
        if k not in dict1 or k in dict1 and dict1[k] != v:
            diffs.append(f"+ {k}: {str(v).lower()}")


def fill_first(diffs, dict1, dict2):
    for (k, v) in dict1.items():
        s = ''
        if k not in dict2 or k in dict2 and dict2[k] != v:
            s = '-'
        elif k in dict2 and dict2[k] == v:
            s = ' '

        diffs.append(f"{s} {k}: {str(v).lower()}")


def sorted_dict(d: dict):
    return dict(sorted(d.items(), key=lambda x: x[0]))


if __name__ == '__main__':
    main()