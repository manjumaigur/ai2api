import argparse
import os
import subprocess


def parse_args(known: bool = False) -> argparse.Namespace:
    parser = argparse.ArgumentParser("AI2API project generator")
    parser.add_argument("--model-url", type=str, help="Model URL")
    parser.add_argument("--project-name", type=str, help="Project name")
    parser.add_argument("--project-path", type=str, help="Project destination")

    return parser.parse_known_args()[0] if known else parser.parse_args()


def main(args: argparse.Namespace) -> None:
    clone_skeleton_process = subprocess.Popen(
        [
            "git",
            "clone",
            "https://github.com/manjumaigur/fastapi-ai-skeleton.git",
            "--depth=1",
            args.project_name,
        ],
        cwd=args.project_path,
    )
    clone_skeleton_process.communicate()

    project_path = os.path.join(args.project_path, args.project_name)
    model_dir = os.path.join(project_path, "model")
    os.makedirs(model_dir, exist_ok=True)
    git_lfs_install_process = subprocess.Popen(["git", "lfs", "install"])
    git_lfs_install_process.communicate()
    model_clone_process = subprocess.Popen(
        [
            "git",
            "clone",
            args.model_url,
            os.path.basename(args.model_url),
        ],
        cwd=model_dir,
    )
    model_clone_process.communicate()


def run(**kwargs) -> None:
    args = parse_args(known=True)
    for k, v in kwargs.items():
        setattr(args, k, v)
    main(args)


if __name__ == "__main__":
    args = parse_args()
    main(args)
