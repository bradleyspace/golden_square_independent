import random

class TodoNotFound(Exception):
    """
    A custom exception that raises if you try to delete a Todo
    with a ID that does not exist

    This is simply to create a more specific exception, instead of catching a broad Exception error.
    """

    def __init__(self, _id: int, message: str = "Todo with ID: {0} not found!") -> None:
        super().__init__(message.format(_id))

class TodoList:

    def __init__(self) -> None:
        """
        Create the todo list instance variable.
        This will be a list of dictionaries, each
        dictionary will look something like this:
        {
            "_id": "123",
            "todo": "Write the tests first!"
        }
        """
        self._todo_list: list[dict] = []

    def create(self, todo: str) -> int:
        """
        Create a todo and return an integer representing the ID tied to it.
        Parameters:
            - todo [str] -> The actual todo description
        Returns:
            - id [int] -> The id created for the todo item
        """
        
        todo_id = random.randint(100, 999)

        # Check the ID doesn't already exist so there isnt duplicates.
        all_ids = [item["_id"] for item in self._todo_list]
        while todo_id in all_ids:
            todo_id = random.randint(100, 999)

        new_todo = {
            "_id": todo_id,
            "todo": todo
        }

        self._todo_list.append(new_todo)
        return todo_id

    
    def get_all(self) -> list[tuple[int, str]]:
        """
        Return all the todos as a tuple, with the ID being first and the todo being last. Ex: [(123, "Todo!")]
        Param:
            None
        Returns:
            - List[Tuple[Int, Str]]
        """
        pass

    def get_by_id(self, id: int) -> str:
        """
        Get a todo by its ID
        Param:
            id [int] - The id for the todo item
        Returns:
            str - The todo, if the ID is found, else none.
        """
        pass

    def delete(self, id: int) -> None:
        """
        Delete a todo by its ID
        Param:
            id [int] - The id for the todo item:
        Returns:
            NoneType
        """
        pass