import os

class Finder():
    """
    The Dir_crawler class is a wrapper for scripts that will search 
    through directories and find the requested files and their paths. 
    """
    __version__ = '0.0.1'

    def __init__(self, starting_directory: str):
        
        assert os.access(starting_directory, 0), 'Starting Directory must be accessable.'
        self.starting_directory = starting_directory

    def find_file_type(self, file_extension = '.pdf', full_path = False) -> list:
        """
        Takes in the file extension and then walks the child directories from the starting point in order to find 
        the files with the ending extension.

        Parameters
        --------------------------------
        file_extension: a string of the file extension (ex '.pdf', '.csv', '.xls')
        full_path: a boolean value to determine weather to just find the file or return the full path 
            to the file from the starting_directory
        """

        results = []

        # Walk through the file tree for the given directory 
        for root, _, files in os.walk(self.starting_directory):
            # Check if current child directory is accessable, if not print that it is not then move on. 
            print(root)
            if not os.access(root, os.R_OK):
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


    def find_directory(self, folder_names: list, full_path = True) -> list:
        """
        Returns a list of the folders inside of the starting_directory that are inside of the folder_names list

        Parameters
        -----------------------
        folder_names: list of the folder names to check for in the directory
        full_path: a boolean value to determine weather to just find the file or return the full path 
            to the file from the starting_directory
        """

        results = []

        for root, dirs, _ in os.walk(self.starting_directory):
            # Iterate through the child directories checking if the folder names match.
            for ch in dirs:
                if ch in folder_names:
                    # Check for the full path argument and append to results accordingly
                    if full_path: 
                        results.append(root + '\\' + ch)
                    else: 
                        results.append(ch)
        return results


    def find_files(self, full_path = False) -> list:
        """
        Finds all files inside of the starting directory and returns them in a list. w
        """
        results = []
        for root, _, files in os.walk(self.starting_directory):
            for f in files:
                if full_path: 
                    results.append(root + '\\' + f)
                else: 
                    results.append(f)

        return results

    def set_starting_dir(self, starting_directory: str) -> None:
        self.starting_directory = starting_directory