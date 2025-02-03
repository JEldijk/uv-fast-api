from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app.main import app

client = TestClient(app)
mockSettings = Settings(admin_email="testing_admin@example.com")


def get_settings_override():
    return mockSettings


app.dependency_overrides[get_settings] = get_settings_override


def test_app():
    response = client.get("/info")
    data = response.json()
    expected = mockSettings.model_dump_json()

    assert data == expected
