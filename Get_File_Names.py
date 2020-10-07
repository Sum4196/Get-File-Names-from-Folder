import os

for dirname, dirnames, filenames in os.walk("C:\\Users\\Michael\\Downloads"):

    # print path to all filenames.
    for dirname in dirnames:
        print(os.path.join(dirname))