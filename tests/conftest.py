import pytest

from app import app
from main import export_envs, export_secret_envs
from fastapi.testclient import TestClient


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    export_envs("test")
    export_secret_envs()


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
