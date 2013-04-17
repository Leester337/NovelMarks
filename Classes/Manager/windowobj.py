class WindowObjectType:
    BOOKMARK_OBJ = 1
    SEARCH = 2
    GO_UP = 3
    ADD = 4

class WindowObject:
    def __init__(self, obj_type, value=None):
        """Defines a window object and describes what was clicked

        Keyword Args:
        obj_type -- type of window object
        value -- optional information the window object should contain (default: None)
        """
        if obj_type is None:
            raise ValueError("Must define a valid window object type")
        self.obj_type = obj_type
        self.value = value

