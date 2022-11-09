import os
#https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    # do something
