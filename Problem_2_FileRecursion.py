## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))


def find_files(suffix, path):
#def find_files(path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "":
        print("Empty suffix")
        return

    for file in os.listdir(path):
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            find_files(suffix, new_path)

        elif os.path.isfile(new_path):
            if file.endswith(suffix):
                print(os.path.join(path, file))


# Edge Test cases
print("\nTest case 1:")
find_files("", ".")
print("\nTest case 2:")
find_files("", "")

# Test cases
print("\nTest case 3:")
find_files(".py", ".")
print("\nTest case 4:")
find_files(".wen", ".")
