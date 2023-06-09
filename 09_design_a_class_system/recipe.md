# Recipe

## Project Requirements

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## Classes

```py

# File: lib/diary.py

@dataclass
class DiaryEntry:

    def __init__(self, title, contents, time) -> None:
        """
        Description:
            A class representing a entry in a diary.
        Parameters:
            title: str -> A string representing the title of the entry
            contents: str -> A string representing the description of the entry
            time: datetime.datetime -> A datetime object representing the time the entry was created
        """

    @property
    def title(self) -> str:
        # Returns the title of the DiaryEntry
        pass

    @property
    def contents(self) -> str:
        # Returns the title of the DiaryEntry

    @property
    def as_dict(self) -> dict:
        # Returns the DiaryEntry object as a dict which can
        # be serialized into a JSON object to add to the entries

# File: lib/diary.py

class Diary:

    def __init__(self) -> None:
        """
        Description:
            Construct the file and load all files
        """
        pass

    def list_entries(self) -> list[DiaryEntry]:
        """
        Description:
            Return a list of all the diary entries
        Parameters:
            None
        Returns:
            list[DiaryEntry]
        """
        pass

    def get_entry(self, time) -> DiaryEntry:
        """
        Description:
            Returns a DiaryEntry based on the time it was entered
        Parameters:
            None
        Returns:
            DiaryEntry
        """
        pass

    def get_readable_entries_wpm(self, wpm: int, time: int) -> list[DiaryEntry]:
        """
        Description:
            Returns a list of DiaryEntry instances based on if they can be read in time.
        Parameters:
            wpm: int - A integer representing the words per minute of the User
            time: int - A integer representing the time the user has to read.
        Returns:
            list[DiaryEntry]
        """
        pass

    def get_all_phone_numbers(self) -> list[str]:
        """Parses through each diary entry and grabs the phone numbers using regex"""
        pass


# File: lib/todo.py

@dataclass
class Todo:
    """
    A dataclass representing a single todo item
    """
    pass

    @property
    def id(self):
        return

    @property
    def item(self):
        return

    def delete(self):
        return

# File: lib/todo.py
class TodoList:
    """
    A class representing all the todos
    """
    
    def __init__(self) -> None:
        return

    def list_todos(self) -> list[Todo]:
        return

    def delete_todo(self, _id: int)
        return

# File: lib/user.py (Entry)

class User:
    """
    A class that represents the user its self, and the TodoList and Diary entries
    """

    def __init__(self) -> None:
        return

    
