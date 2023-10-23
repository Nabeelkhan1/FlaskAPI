"""Console script for project3."""
import argparse
import sys


def main():
    """Console script for project3."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "project3.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
