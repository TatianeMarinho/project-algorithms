import pytest
from challenges.challenge_encrypt_message import encrypt_message

message_crypt = 'buapau'


def test_encrypt_message():
    # caso message nao seja string
    with pytest.raises(TypeError):
        encrypt_message(234, 2)

    # caso o key nao seja um inteiro
    with pytest.raises(TypeError):
        encrypt_message(message_crypt, 'abc')

    # caso key nao seja indice posit valido message, retorna message invertida
    assert encrypt_message(message_crypt, 9) == 'uapaub'

    # caso o key seja impar
    assert encrypt_message(message_crypt, 3) == 'aub_uap'

    # caso o key seja par
    assert encrypt_message(message_crypt, 4) == 'ua_paub'
