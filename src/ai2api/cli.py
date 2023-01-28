import argparse

from . import generate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("AI2API project generator CLI")
    parser.add_argument("--model-url", type=str, help="Model URL")
    parser.add_argument("--project-name", type=str, help="Project name")
    parser.add_argument("--project-path", type=str, help="Project destination")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    generate.run(**vars(args))


if __name__ == "__main__":
    main()
