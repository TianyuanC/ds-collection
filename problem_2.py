import os


def find_files(suffix=".c", path="."):
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
    paths = []
    dirs = []
    try:
        dirs = os.listdir(path)
    except FileNotFoundError:
        return paths
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        if os.path.isfile(dir_path):
            if dir_path.endswith(suffix):
                paths.append(dir_path)
        else:
            paths.extend(find_files(suffix, dir_path))
    return paths


# list all c files under current dir
print(find_files())
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

# find file where folder doesn't exist
print(find_files(".c", "./test"))
# []

# find file where suffix doesn't exist
print(find_files("none", "./testdir"))
# []

# find correct files a.c
print(find_files("a.c", "./testdir"))
# ['./testdir/subdir5/a.c', './testdir/subdir1/a.c']
