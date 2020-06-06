Explanations on problem 2:

I applied recursive concept to find all the files with the suffix I am looking for.
I used a for loop to look through all the files in the target directory, and then
I used isdir to find out whether the file is a directory or not. If it is a directory,
then the function will be called to search for the file with that new directory.
This process will be repeated recursively until the base case, which is when a file
is indeed a file, is reached, then it will return value if the file's suffix is what
we are looking for.

Since I am using recursive method within a for loop. O(n) for run time could be
extremely long if there's layer of layer of file folders within the file folders.
The recursive will only end with in the last layer of folders, thus the time depends
on how many layer of folders one has. If there's 3 layers of folder and each folder
contains n folders/files(in last layer), then we should expect O(n^3) run time

Space complexity of file recursion will be: O(paths), since the output will only
be generated once the paths are found
