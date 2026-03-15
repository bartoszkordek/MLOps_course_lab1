import os
import argparse
from dotenv import load_dotenv
from settings import Settings


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

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
