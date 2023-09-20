from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message_when_key_is_not_an_integer():
    invalid_key = "invalid"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", invalid_key)


def test_encrypt_message_when_message_is_not_an_string():
    invalid_message = 7
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, invalid_message)


def test_encrypt_message_successful_when_key_is_not_in_range():
    message = "encrypted"
    assert encrypt_message(message, 10) == message[::-1]


def test_encrypt_message_successful_when_key_is_odd():
    message = "encrypted"
    assert encrypt_message(message, 3) == "cne_detpyr"


def test_encrypt_message_successful_when_key_is_even():
    message = "encrypted"
    assert encrypt_message(message, 4) == "detpy_rcne"
