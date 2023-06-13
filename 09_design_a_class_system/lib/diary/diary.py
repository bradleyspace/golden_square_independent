from .diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._entries.append(entry)

    def all(self) -> list[DiaryEntry]:
        # Returns:
        #   A list of instances of DiaryEntry
        return self._entries

    def count_words(self) -> int:
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        words = 0
        for entry in self._entries:
            words += entry.count_words()

        return words

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        words = self.count_words()

        if words <= 0 or wpm <= 0: # Check if either is 0 to prevent a ZeroDivisionError
            return 1

        total_reading_time = self.count_words() / wpm

        if total_reading_time < 1:
            return 1
        
        return round(total_reading_time)
        

    def find_best_entry_for_reading_time(self, wpm, minutes) -> DiaryEntry:
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        entries: list[DiaryEntry] = self._entries

        best_entry = None

        total_words = wpm * minutes 

        for entry in entries:
            reading_time = entry.reading_time(wpm)
            if reading_time <= total_words:
                if best_entry is None or abs(reading_time - total_words) < abs(best_entry.reading_time(wpm) - 500):
                    best_entry = entry
            
        return best_entry