class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self._last_chunk_index = 0

    def count_words(self) -> int:
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm == 0 or self.contents == 0:
            return 1
        
        total_time = len(self.contents.split(" ")) / wpm

        if total_time < 1:
            return 1
        
        return round(total_time)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words = self.contents.split(" ")
        first_index = self._last_chunk_index
        last_index = (wpm * minutes) + first_index
        self._last_chunck_index = last_index

        if last_index > len(words):
            last_index = len(words)
            self._last_chunk_index = 0

        return " ".join(words[first_index:last_index])