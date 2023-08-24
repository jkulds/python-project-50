import argparse
import json


def main():
    t = f"Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=t)
    parser.add_argument("-f", "--format", type=list, help="set format of output")
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()

    diffs = generate_diff(args.first_file, args.second_file)

    print((diffs))


if __name__ == '__main__':
    main()


def generate_diff(path1: str, path2: str) -> str:
    j1: dict = json.load(open(path1))
    j2 = json.load(open(path2))
    j1 = sorted_dict(j1)
    j2 = sorted_dict(j2)
    print(j1, j2)
    diffs = []
    for (k, v) in j1.items():
        if k not in j2:
            diffs.append(f"- {k}: {str(v).lower()}")
        elif k in j2 and j2[k] == v:
            diffs.append(f"  {k}: {str(v).lower()}")
        elif k in j2 and j2[k] != v:
            diffs.append(f"- {k}: {str(v).lower()}")

    for (k, v) in j2.items():
        if k in j1 and j1[k] != v:
            diffs.append(f"+ {k}: {str(v).lower()}")
        if k not in j1:
            diffs.append(f"+ {k}: {str(v).lower()}")

    return '\n'.join(diffs)


def sorted_dict(d: dict):
    return dict(sorted(d.items(), key=lambda x: x[0]))
