import argparse


def main():
    t = f"Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=t)
    # parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    parser.add_argument("-f", "--format", type=list, help="set format of output")
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.parse_args()


if __name__ == '__main__':
    main()
