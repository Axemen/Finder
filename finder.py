from glob import glob, iglob
from typing import List, Generator
import os

"""
A collection of common uses from the glob library wrapped in easy to use functions.
"""

def find_files(root:str, 
                file_name = '**', 
                file_extension = '*', 
                directory_in_path = '**', 
                recursive = False) -> List:
    """
    find files with the specified parameters. 

    Returns a list with complete paths to the files. 

    PARAMS:
        root: The top-level directory from which to start the search. 
        file_name: The name of the file(s) to search for. 
        directory_in_path: A directory that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child directories as well. 

    """

    if directory_in_path != '**':
        directory_in_path = '**/' + directory_in_path

    return glob(f"{root}{directory_in_path}/{file_name}.{file_extension}" , recursive = recursive)

def find_directories(root:str, 
                    directory_name = "*", 
                    directory_in_path = "**", 
                    recursive = False) -> List:
    """
    find files with the specified parameters. 

    Returns a list with complete paths to the directories.

    PARAMS:
        root: The top-level directory from which to start the search. 
        directory_name: The name of the directory(s) to search for. 
        directory_in_path: A directory that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child directories as well. 
    """
    return glob(f"{root}**/{directory_in_path}/**/{directory_name}/", recursive=recursive)

def ifind_files(root:str, 
                file_name = '**', 
                file_extension = '*', 
                directory_name = '**', 
                recursive = False) -> Generator:
    """
    find files with the specified parameters. 

    Returns a generator that produces the full paths to the files. 

    PARAMS:
        root: The top-level directory from which to start the search. 
        file_name: The name of the file(s) to search for. 
        directory_in_path: A directory that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child directories as well. 
    """
    if directory_in_path != '**':
        directory_in_path = '**/' + directory_in_path

    return iglob(f"{root}{directory_in_path}/{file_name}.{file_extension}" , recursive = recursive)

def ifind_directories(root:str, 
                    directory_name = "*", 
                    directory_in_path = "**", 
                    recursive = False) -> Generator:  
    """
    find files with the specified parameters. 

    Returns a generator that produces the full paths to the files. 

    PARAMS:
        root: The top-level directory from which to start the search. 
        directory_name: The name of the directory(s) to search for. 
        directory_in_path: A directory that appears at any point within the file's path. 
        recursive: Weather or not to perform the search within child directories as well. 
    """
    return iglob(f"{root}**/{directory_in_path}/**/{directory_name}/", recursive=recursive)
