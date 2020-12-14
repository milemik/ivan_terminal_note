from unittest import mock
from ApiCaller.caller import ApiCaller
import pytest


@pytest.fixture
def email_pass():
    email = "test@test.com"
    password = "somepasss"
    return email, password


def test_get_token_call(email_pass):
    email, password = email_pass
    
    with mock.patch('ApiCaller.caller.ApiCaller.get_token') as get_token:
        ApiCaller(email, password).get_token()
    
    assert get_token.called_once


def test_add_info_call(email_pass):
    email, password = email_pass

    with mock.patch("ApiCaller.caller.ApiCaller.add_info") as add_info:
        ApiCaller(email, password).add_info()

    assert add_info.called_once


def test_list_info_call(email_pass):
    email, password = email_pass

    with mock.patch("ApiCaller.caller.ApiCaller.list_info") as list_info:
        ApiCaller(email, password).list_info()
    
    assert list_info.called_once