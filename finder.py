import glob
from typing import List, Tuple, Generator
from pathlib import Path
import os
"""
A collection of common uses from the glob library wrapped in easy to use functions.
"""

def find_file_by_extension(root: str, extension: str, recursive = False) -> List:
    """
    root: the root directory to search within.
    extension: the file extension to search for.
    recursive: Weather or not you wish to search sub-directories as well. 
    """
    return glob.glob(f"{root}**/*{extension}")

def find_file_by_name(root:str, file_name:str, recursive = False) -> List:
    """
    root: the root directory to search within.
    file_name: the name of the file you wish to search for. 
    recursive: Weather or not you wish to search sub-directories as well. 
    """
    return glob.glob(f"{root}**/{file_name}.*")

def find_all_files(root:str, recursive = False) -> List:
    """
    root: the root directory to search within.
    recursive: Weather or not you wish to search sub-directories as well. 
    """
    return glob.glob(f"{root}**/*.*")

def find_directory_by_name(root:str, directory_name: str, recursive = False) -> List:
    """
    root: the root directory to search within.
    directory_name: The name of the directory(ies) you wish to find
    recursive: Weather or not you wish to search sub-directories as well. 
    """
    return glob.glob(f"{root}**/{directory_name}/")

def find_all_directories(root:str, recursive = False) -> List:
    """
    root: the root directory to search within.
    recursive: Weather or not you wish to search sub-directories as well. 
    """
    return glob.glob(f"{root}**/")

def find_files_with_folder_in_path(root: str, folder_in_path:str, file_name:str):
    return glob.glob(f'{root}**/{folder_in_path}/**/{file_name}.*')