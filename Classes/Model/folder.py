from bookmarkfolder import BookmarkFolder
from datetime import datetime

class Folder(BookmarkFolder):
    
    def __init__(self, name = '', date = datetime.now(), clickCount = 0, children = []):
        BookmarkFolder.__init__(self, name, date, clickCount)
        self.children = children
