# Recipe

## Class

```py

class SameSongError(Exception):

    def __init__(self, name, artist, message: str = "Song with name: {0} and artist: {1} already exists!") -> None:
        super().__init__(message.format(name, artist))

class MusicTracker:

    def __init__(self) -> None:
        """
        Init the class and create a instance variable that stores the tracks in a list of dictionaries
        Example:
        [{
            "artist": "me",
            "name": "challenge 06",
        }, ...]
        """
        pass

    def add_track(self, artist: str, name: str) -> None:
        """
        Add a track to the list
        Param:
            - Artist [str] -> The artist
            - Name [str] -> The name of the song
        Return:
            None
        """
        pass

    @property
    def tracks(self) -> list[dict]
        """
        Return the list of tracks
        Param:
            None
        Returns:
            List[Dict]
        """
        pass

```

## Tests

```py

# Assert that a added track is listed by MusicTracker.tracks
assert {"name": "MyTrack", "artist": "MyArtist"} in MusicTracker.tracks

# Assert that the same song can't be added twice and raises a SameSongError
assert error_message => "Song with name: MyTrack and artist: MyArtist already exists!"

# Assert that adding multiple tracks properly gets listed
my_tracks = [{...}, {...}, {...}, ...] # List of my tracks
assert my_tracks in MusicTracker.tracks

