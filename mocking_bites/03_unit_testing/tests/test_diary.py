from lib import Diary

def test_init_contents():
    diary = Diary("My Diary")

    assert diary.read() == "My Diary"
