from finder import Finder
from pathlib import Path

finder = Finder(Path(r'testing_dir'))

"""
Test for the find_file_type function of the Finder class.

Expected output should be the file names and then their paths. 
"""
# print(finder.find_file_type('.pdf'))
# print(finder.find_file_type('.pdf', full_path=True))

"""
Test for the find_direcory funciton in the Finder class

Expected output should be the folder names, then the folder paths. 
"""
print('Test one: folder_name = ["LGL"], full_path = False \n')
print(finder.find_directory(
    folder_names = ['LGL']
))

print('Test two: folder_name = ["LGL", "HRM"], full_path = False \n')
print(finder.find_directory(
    folder_names = ['LGL', 'HRM']
))

print('Test three: folder_name = ["LGL"], full_path = True \n')
print(finder.find_directory(
    folder_names = ['LGL'],
    full_path=True
))

print('Test three: folder_name = ["LGL", "HRM"], full_path = True \n')
print(finder.find_directory(
    folder_names = ['LGL', 'HRM'],
    full_path=True
))
