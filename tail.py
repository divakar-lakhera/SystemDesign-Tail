import os
import args

class tailn:
    def __init__(self,n_lines=1,filename="NA") -> None:
        self.n_lines = n_lines
        self.filename = filename

    def get_tail(self):
        try:
            self.file_object = open(self.filename,"r+")
            print("File Opened")
        except Exception as e:
            print("Failed to Open File: {}".format(e))
            return
        lines_as_string = ""
        self.file_object.seek(0,2)
        current_pointer = self.file_object.tell()
        print(current_pointer)
        lines = 0
        while(lines < self.n_lines and current_pointer>=0):
            self.file_object.seek(current_pointer)
            currChar = self.file_object.read(1)
            if(currChar == '\n' and len(lines_as_string)==0):
                current_pointer -=1
                continue
            if(currChar == '\n'):
                lines += 1
            lines_as_string += currChar
            current_pointer -=1
        if len(lines_as_string) >0  and lines_as_string[len(lines_as_string)-1] == '\n':
            lines_as_string = lines_as_string[:-1]
        print(lines_as_string)
        self.file_object.close()
        return lines_as_string[::-1]

