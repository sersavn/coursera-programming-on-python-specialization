# Write and define class FileReader
# __init__ takes argument and contains path to the file
# class should have method read
# read returns file contents
# exception IOError should be handled

'''
reader = FileReader("example.txt")
print(reader.read())
'''

class FileReader:
    def __init__(self, name):
        self.name = name

    def read(filepath):
        try:
            with open(filepath.name) as f:
                return f.read()
        except IOError:
            return ""

#reader = FileReader("example1.txt")
#print(reader.read())
