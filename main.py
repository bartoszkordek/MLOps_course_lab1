import yaml
import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def load_secret_file():
    with open("secrets.yaml", "r") as file:
        return yaml.safe_load(file)


def export_secret_envs():
    secrets = load_secret_file()
    os.environ["API_KEY"] = str(secrets["API_KEY"])


def export_envs(environment: str = "dev") -> None:
    file_path = "config/.env.{environment}".format(environment=environment)
    if os.path.exists(file_path):
        load_dotenv(file_path)
    else:
        raise FileNotFoundError(f"Config file .env.{environment} not exists")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    export_secret_envs()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
