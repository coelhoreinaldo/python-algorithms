from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt():
    invalid_key = "invalid"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", invalid_key)
    invalid_message = 7
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, invalid_message)
    message = "encrypted"
    assert encrypt_message(message, 10) == message[::-1]
    message = "encrypted"
    assert encrypt_message(message, 3) == "cne_detpyr"
    message = "encrypted"
    assert encrypt_message(message, 4) == "detpy_rcne"
