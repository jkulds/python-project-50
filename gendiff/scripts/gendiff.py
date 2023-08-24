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

    diffs = generate_diff(args.first_file, args.second_file)

    print(diffs)
    return diffs


if __name__ == '__main__':
    main()


def generate_diff(path1: str, path2: str) -> str:
    j1: dict = json.load(open(path1))
    j2 = json.load(open(path2))
    j1 = sorted_dict(j1)
    j2 = sorted_dict(j2)
    print(j1, j2)
    diffs = []
    fill_first(diffs, j1, j2)
    fill_second(diffs, j1, j2)

    return '{\n' + '\n'.join(diffs) + '\n}'


def fill_second(diffs, j1, j2):
    for (k, v) in j2.items():
        if k not in j1 or k in j1 and j1[k] != v:
            diffs.append(f"+ {k}: {str(v).lower()}")


def fill_first(diffs, j1, j2):
    for (k, v) in j1.items():
        s = ''
        if k not in j2 or k in j2 and j2[k] != v:
            s = '-'
        elif k in j2 and j2[k] == v:
            s = ' '
        diffs.append(f"{s} {k}: {str(v).lower()}")


def sorted_dict(d: dict):
    return dict(sorted(d.items(), key=lambda x: x[0]))
