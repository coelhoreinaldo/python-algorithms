from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    invalid_key = "invalid"
    valid_message = "encrypted"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(valid_message, invalid_key)

    invalid_message = 7
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, 5)

    assert encrypt_message(valid_message, 10) == valid_message[::-1]
    assert encrypt_message(valid_message, 3) == "cne_detpyr"
    assert encrypt_message(valid_message, 4) == "detpy_rcne"
