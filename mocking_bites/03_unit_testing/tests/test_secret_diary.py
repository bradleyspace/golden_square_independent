import pytest
from unittest.mock import Mock
from lib import SecretDiary


def test_init_with_mock():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)

    assert secret_diary.diary == fake_diary


def test_read_while_locked():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)

    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

def test_read_while_unlocked():
    fake_diary = Mock()
    fake_diary.read.return_value = "My Diary"
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()

    assert secret_diary.read() == "My Diary"
