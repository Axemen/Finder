from os import walk, path, R_OK, access
from collections import Counter
from datetime import datetime
from typing import Generator

class Finder():
    """
    The Dir_crawler class is a wrapper for scripts that will search 
    through directories and find the requested files and their paths. 
    """
    __version__ = '0.0.1'

    def __init__(self, starting_directory:str = None):
        
        if starting_directory is not None:  
            assert access(starting_directory, 0), \
                                                        'Starting Directory must be accessable.'
            self.starting_directory = starting_directory
        else:
            self.starting_directory = None

    """
    FINDERS
    ======================================================================
    """

    def find_file_type(self, 
        file_extension = '.pdf', 
        full_path = False, 
        starting_directory:str = None) -> list:

        """
        Takes in the file extension and then walks the child directories from the starting point in order to find 
        the files with the ending extension.

        Parameters
        --------------------------------
        file_extension: a string of the file extension (ex '.pdf', '.csv', '.xls')
        full_path: a boolean value to determine weather to just find the file or return the full path 
            to the file from the starting_directory
        """
        if starting_directory is None: 
            starting_directory = self.starting_directory
        assert starting_directory is not None, "starting_directory must be set"

        results = []

        # Walk through the file tree for the given directory 
        for root, _, files in walk(self.starting_directory):

            # Check if current child directory is accessable, if not print that it is not then move on. 
            if not access(root, R_OK):
                print(f"{root} is not accessable... Skipping")
                pass

            # Iterate through the files in the current directory 
            for f in files:
                # Check the file extension of the file currently being iterated over
                if f.endswith(file_extension):
                    # Check weather or not to print out the full path. 
                    if full_path: 
                        results.append(root + '\\' + f)
                    else: 
                        results.append(f)

        return results

    def find_file_type_gen(self, 
        file_extension = '.pdf', 
        full_path = False, 
        starting_directory:str = None) -> Generator:

        for root, _, files in walk(self.starting_directory):

            # Check if current child directory is accessable, if not print that it is not then move on. 
            if not access(root, R_OK):
                print(f"{root} is not accessable... Skipping")
                pass

            # Iterate through the files in the current directory 
            for file_name in files:
                # Check the file extension of the file currently being iterated over
                if f.endswith(file_extension):
                    # Check weather or not to print out the full path. 
                    if full_path: 
                        yield root + '\\' + file_name
                    else: 
                        yield file_name
    
    def find_directories(self, folder_names:str, full_path = True, starting_directory:str = None) -> list:
        """
        Returns a list of the folders inside of the starting_directory that are inside of the folder_names list

        Parameters
        -----------------------
        folder_names: list of the folder names to check for in the directory
        full_path: a boolean value to determine weather to just find the file or return the full path 
            to the file from the starting_directory
        """
        if starting_directory is None: starting_directory = self.starting_directory
        assert starting_directory is not None, "starting_directory must be set"

        results = []

        for root, dirs, _ in walk(self.starting_directory):
            # Iterate through the child directories checking if the folder names match.
            for ch in dirs:
                if ch == folder_names:
                    # Check for the full path argument and append to results accordingly
                    if full_path: 
                        results.append(root + '\\' + ch)
                    else: 
                        results.append(ch)
        return results

    def find_files(self, full_path = False, starting_directory:str = None) -> list:
        """
        Finds all files inside of the starting directory and returns them in a list. 
        """
        if starting_directory is None: starting_directory = self.starting_directory
        assert starting_directory is not None, "starting_directory must be set"

        for root, _, files in walk(starting_directory):
            for f in files:
                if full_path: 
                    results.append(root + '\\' + f)
                else: 
                    results.append(f)
        
        print('')
        return results


    """
    COUTNERS
    ======================================================================
    """
    def count_file_types(self) -> dict:
        """
        Returns the number of files types inside of a directory
        """
        file_counter = Counter()
        
        for _, _, files in walk(self.starting_directory):
            for f in files:
                # returns the file extension by splitting on periods and then grabbing the last element in the returned list
                extension = f.split('.')[-1] 
                file_counter[extension] += 1

        return dict(file_counter)

    def count_files(self) -> int:
        """
        Returns the number of files inside of a directory and it's children. 
        """
        num_files = 0
        for _, _, files in walk(self.starting_directory):
            num_files += len(files)

        return num_files

    def count_directories(self) -> int:
        """
        Returns the number of directories nested inside of the 
        starting directory. 
        """

        num_dirs = 0
        for _, dirs, _ in walk(self.starting_directory):
            num_dirs += len(dirs)

        return num_dirs

    """
    GETTERS AND SETTERS
    ======================================================================
    """
    def set_starting_dir(self, starting_directory: str) -> None:
        self.starting_directory = starting_directory

    def get_starting_dir(self) -> str:
        return self.starting_directory