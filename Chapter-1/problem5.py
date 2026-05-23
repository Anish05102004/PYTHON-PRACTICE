# Label the program written in problem 4 with comments.


import os

# specify the directory path
path = "/"

# get list of files and folders
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)