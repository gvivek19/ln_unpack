import os
from file_parser import FileParser

filelist = os.listdir(".")

for eachfile in filelist:
    print eachfile
    fpObject = FileParser(eachfile)
