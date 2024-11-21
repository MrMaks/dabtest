from my_package.step1 import runstep
import yaml
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root_path",
        action="store",
        default=None,
        type=str,
        required=True,
    )

    args = parser.parse_args()
    print(args.root_path)

    runstep("cucumber")
