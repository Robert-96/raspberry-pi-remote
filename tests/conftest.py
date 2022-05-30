import pytest

from remote import create_app
from remote.keyboard import KEYBOARD


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""

    app = create_app({"TESTING": True})
    KEYBOARD.debug()

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""

    return app.test_client()
