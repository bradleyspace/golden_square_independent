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
        self._track_list = []

    def add_track(self, name: str, artist: str) -> None:
        """
        Add a track to the list
        Param:
            - Artist [str] -> The artist
            - Name [str] -> The name of the song
        Return:
            None
        """
        new_track = {
            "name": name,
            "artist": artist
        }

        if new_track in self._track_list:
            raise SameSongError(name, artist)

        self._track_list.append(new_track)

    @property
    def tracks(self) -> list[dict]:
        """
        Return the list of tracks
        Param:
            None
        Returns:
            List[Dict]
        """
        return self._track_list