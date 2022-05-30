import pytest


def test_get_modes(client):
    response = client.get("/api/modes")
    assert response.status_code == 200, response.json

    payload = response.json
    assert "modes" in payload

    modes = payload["modes"]
    assert {"name": "Youtube"} in modes


def test_get_actions(client):
    response = client.get("/api/actions")
    assert response.status_code == 200, response.json

    payload = response.json
    assert "actions" in payload

    actions = payload["actions"]
    assert {"name": "Pause", "mode": "Youtube"} in actions


def test_post_actions(client):
    response = client.post("/api/actions", json={"action": {"name": "Pause", "mode": "Youtube"}})
    assert response.status_code == 201, response.json

    payload = response.json
    assert "action" in payload

    action = payload["action"]
    assert action["mode"] == "Youtube"
    assert action["name"] == "Pause"
