import os

class watcher:
    def __init__(self,filename):
        self.previous_stamp = 0
        self.filename = filename
        self.ready = False
        try:
            self.previous_stamp = os.stat(self.filename).st_mtime
            self.ready = True
            print("File Ready")
        except:
            print("Failed to load file "+self.filename)
    
    def check(self):
        if not self.ready:
            print("File Not Open")
            return -1
        current_stamp = os.stat(self.filename).st_mtime
        if current_stamp != self.previous_stamp:
            self.previous_stamp = current_stamp
            return 1
        return 0


class watchdog:
    def __init__(self,filename) -> None:
        self.watcherOb = watcher(filename)
    
    def get_changes(self) -> str:
        if self.watcherOb.check() == 1:
            return "File Change Detected "+str(self.watcherOb.previous_stamp)
        else:
            return "NA"
