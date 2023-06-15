import pytest
from lib import Diary, SecretDiary


def test_init_locked():
    diary = Diary("My Diary!")
    secret_diary = SecretDiary(diary)

    assert secret_diary.locked is True

    with pytest.raises(Exception) as e:
        secret_diary.read()

    assert str(e.value) == "Go away!"


def test_unlock():
    diary = Diary("My Diary")
    secret_diary = SecretDiary(diary)

    secret_diary.unlock()

    assert secret_diary.read() == "My Diary"

def test_relock():
    diary = Diary("My Diary")
    secret_diary = SecretDiary(diary)

    secret_diary.unlock()

    unlocked_state = secret_diary.read()

    secret_diary.lock()

    with pytest.raises(Exception) as e:
        secret_diary.read()

    assert unlocked_state == "My Diary"
    assert str(e.value) == "Go away!"
