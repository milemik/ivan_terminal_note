from unittest import mock
from ..caller import ApiCaller
import pytest


@pytest.fixture
def email_pass():
    email = "test@test.com"
    password = "some_password"
    return email, password


def mocked_response_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://questions-api-ivan.herokuapp.com/users/api-token-auth/":
        return MockResponse({'token': '12345'}, 201)
    if args[0] == "https://questions-api-ivan.herokuapp.com/info/":
        return MockResponse({"title": "test title", "description": "test description"}, 201)


def mocked_response_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://questions-api-ivan.herokuapp.com/info/":
        return MockResponse({"title": "test title", "description": "test description"}, 201)


def test_get_token_call(email_pass):
    email, password = email_pass

    with mock.patch('ivan_terminal_note.caller.requests.post', side_effect=mocked_response_post) as response:
        ApiCaller(email, password).get_token()

    assert response.called_once


def test_add_info_call(email_pass):
    email, password = email_pass

    with mock.patch("ivan_terminal_note.caller.requests.post", side_effect=mocked_response_post) as response:
        ApiCaller(email, password).add_info()

    assert response.called_once


def test_list_info_call(email_pass):
    email, password = email_pass

    with mock.patch("ivan_terminal_note.caller.requests.get", side_effect=mocked_response_get) as response:
        ApiCaller(email, password).list_info()

    assert response.called_once
