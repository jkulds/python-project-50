import argparse

from gendiff.cli import generate_diff


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


if __name__ == '__main__':
    main()
