from settings import Settings


def test_settings_load_test_env():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MLOps introduction"
    assert settings.API_KEY
