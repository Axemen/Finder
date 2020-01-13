from glob import glob, iglob
from typing import List, Generator
import os
"""
A collection of common uses from the glob library wrapped in easy to use functions.
"""
# TODO All iglob functions as well.

def find_files(root:str, file_name = '**', file_extension = '*', folder_in_path = '**', recursive = False) -> List:
    """
    find files with the specified parameters. 

    Returns a list with complete paths to the files. 

    PARAMS:
        root: The top-level directory from which to start the search. 
        file_name: The name of the file(s) to search for. 
        folder_in_path: A folder that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child_directories as well. 

    """
    return glob(f"{root}**/{folder_in_path}/{file_name}.{file_extension}", recursive = recursive)

def find_directories(root:str, folder_name = "*", folder_in_path = "**", recursive = False) -> List:
    """
    find files with the specified parameters. 

    Returns a list with complete paths to the folders.

    PARAMS:
        root: The top-level directory from which to start the search. 
        folder_name: The name of the folder(s) to search for. 
        folder_in_path: A folder that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child_directories as well. 
    """
    return glob(f"{root}**/{folder_in_path}/**/{folder_name}/", recursive=recursive)

def ifind_files(root:str, file_name = '**', file_extension = '*', folder_name = '**', recursive = False) -> Generator:
    """
    find files with the specified parameters. 

    Returns a generator that produces the full paths to the files. 

    PARAMS:
        root: The top-level directory from which to start the search. 
        file_name: The name of the file(s) to search for. 
        folder_in_path: A folder that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child_directories as well. 
    """
    return iglob(f"{root}**/{folder_name}/{folder_name}.{file_extension}", recursive = recursive)

def ifind_directories(root:str, folder_name = "*", folder_in_path = "**", recursive = False) -> Generator:
    """
    find files with the specified parameters. 

    Returns a generator that produces the full paths to the files. 

    PARAMS:
        root: The top-level directory from which to start the search. 
        folder_name: The name of the folder(s) to search for. 
        folder_in_path: A folder that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child_directories as well. 
    """
    return iglob(f"{root}**/{folder_in_path}/**/{folder_name}/", recursive=recursive)
