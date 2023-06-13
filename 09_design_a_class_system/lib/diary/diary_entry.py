class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents

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