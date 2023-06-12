import pytest 
import string
import random
from lib.music_tracker import MusicTracker, SameSongError

def test_add_song():
    instance = MusicTracker()

    instance.add_track("Do I Wanna Know?", "Arctic Monkeys")

    expected = {
        "name": "Do I Wanna Know?",
        "artist": "Arctic Monkeys"
    }

    track_list = instance.tracks
    assert expected in track_list

def test_duplicate():
    instance = MusicTracker()

    name = "It Was A Good Day"
    artist = "Ice Cube"

    instance.add_track(name, artist)

    with pytest.raises(SameSongError) as e:
        instance.add_track(name, artist)

    error_message = str(e.value)
    expected = f"Song with name: {name} and artist: {artist} already exists!"
    assert error_message == expected

def test_multiple_tracks():
    instance = MusicTracker()
    expected_songs = []

    for _ in range(random.randint(9, 30)):
        k = random.randint(5, 11)
        new_dict = {
            "name": "".join(random.choices(string.ascii_lowercase, k=k)),
            "artist": "".join(random.choices(string.ascii_lowercase, k=k-3))
        }
        expected_songs.append(new_dict)

    for song in expected_songs:
        instance.add_track(song["name"], song["artist"])

    track_list = instance.tracks
    assert track_list == expected_songs


