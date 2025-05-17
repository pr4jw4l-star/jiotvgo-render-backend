import argparse
import json
import subprocess

def generate_playlist(config_path, output_path):
    subprocess.run([
        "python3", "-m", "jiotvgo",
        "--config", config_path,
        "--output", output_path
    ], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    generate_playlist(args.config, args.output)
