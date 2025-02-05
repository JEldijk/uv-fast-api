from fastapi.testclient import TestClient
from src.config import Settings, get_settings
from src.main import app

client = TestClient(app)
mock_settings = Settings(admin_email="testing_admin@example.com")


def get_settings_override():
    return mock_settings


app.dependency_overrides[get_settings] = get_settings_override


def test_app():
    response = client.get("/info")
    data = response.json()
    expected = mock_settings.model_dump_json()

    if data != expected:
        raise AssertionError(f"Expected {expected}, but got {data}")
