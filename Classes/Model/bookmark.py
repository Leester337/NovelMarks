from bookmarkfolder import BookmarkFolder
from datetime import datetime

class Bookmark(BookmarkFolder):
    
    def __init__(self, name = '', date = datetime.now(), clickCount = 0, url = ''):
        BookmarkFolder.__init__(self, name, date, clickCount)
        self.url = url
