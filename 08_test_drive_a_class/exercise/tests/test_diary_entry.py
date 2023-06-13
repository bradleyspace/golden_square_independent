from lib import DiaryEntry

def test_reading_chunk():
    wpm = 100
    minutes = 2
    with open("files/passage_1.txt") as f:
        file_contents = f.read()
    words = file_contents.split(" ")
    diary = DiaryEntry("Test Entry", file_contents)
    chunk = diary.reading_chunk(wpm, minutes)

    expected_chunk_1 = " ".join(words[0:200])
    assert chunk == expected_chunk_1

    chunk = diary.reading_chunk(wpm, minutes)
    expected_chunk_2 = " ".join(words[200:400])

    assert chunk == expected_chunk_2

    chunk = diary.reading_chunk(wpm, minutes)
    expected_chunk_3 = " ".join(words[400:491])

    assert chunk == expected_chunk_3


    chunk = diary.reading_chunk(wpm, minutes)
    
    assert chunk == expected_chunk_1
