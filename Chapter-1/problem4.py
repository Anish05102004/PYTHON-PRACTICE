# Write a Python program to print the contents of a directory using the os module. Search online for the function which does that.(use  ai)

import os

# specify the directory path
path = "/"

# get list of files and folders
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)