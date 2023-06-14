import os
from lib import Diary, DiaryEntry


def test_add_item():
    diary = Diary()

    entry = DiaryEntry("12/06/2023", "Working through the golden square!")

    diary.add(entry)

    assert entry in diary.all()

def test_count_words():
    diary = Diary()

    desc_1 = "Working through the golden square!"
    desc_2 = "Still working on the golden square!"

    expected_count = 0
    expected_count += len(desc_1.split(" "))
    expected_count += len(desc_2.split(" "))

    entry_1 = DiaryEntry("12/06/2023", desc_1)
    entry_2 = DiaryEntry("13/06/2023", desc_2)

    diary.add(entry_1)
    diary.add(entry_2)

    word_count = diary.count_words()

    assert word_count == expected_count

def test_reading_time():
    diary = Diary()

    passage_contents = ""
    for i, filename in enumerate(os.listdir("./files")):
        with open(f"files/{filename}", "r") as f:
            text = f.read()
            passage_contents += (text + " ")
            entry = DiaryEntry(f"Diary Entry {i+1}", text)
            diary.add(entry)

    total_reading_time_100 = diary.reading_time(100)
    total_reading_time_200 = diary.reading_time(200)
    total_reading_time_500 = diary.reading_time(500)

    expected_reading_time_100 = 8
    expected_reading_time_200 = 4
    expected_reading_time_500 = 2

    assert total_reading_time_100 == expected_reading_time_100
    assert total_reading_time_200 == expected_reading_time_200
    assert total_reading_time_500 == expected_reading_time_500

def test_best_entry():
    diary = Diary()

    diaries = []
    for i, filename in enumerate(os.listdir("./files")):
        with open(f"files/{filename}", "r") as f:
            text = f.read()
            entry = DiaryEntry(f"Diary Entry {i+1}", text)
            diaries.append(entry)
            diary.add(entry)
            
    best_entry_1 = diary.find_best_entry_for_reading_time(100, 2)
    best_entry_2 = diary.find_best_entry_for_reading_time(200, 10)

    assert best_entry_1.title == "Diary Entry 4"
    assert best_entry_2.title == "Diary Entry 1"