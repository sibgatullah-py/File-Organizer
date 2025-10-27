import os # os module helps to interact with the operating system it's self . it will look on the files if they are there
import shutil # shutil module helps move files around or copying them it helps with file operations
import magic # magic module reads the insides of a file and says what type is it even if the file name lies
from datetime import datetime # gives us the current datetime 

# configuration ---- we will point out scripts here 
SOURCE_DIR = r"The path of the folder you want to organize" # use your own file path here . i used mine while testing 
DEST_DIR = os.path.join(SOURCE_DIR, 'Organized') # this will move all the files in a folder called Organized 

# if Organized file doesn't exists make it . if exists then do nothing
os.makedirs(DEST_DIR, exist_ok=True) # this will create the Organized folder if the folder doesn't exist and then move the files there 

# Category Mapping
'''Category is a dictionary. The left side(keys) are pieces of MIME types. The magic module will read their insides.
The right side(values) are foolder names we will crate inside Organized, like Images, Videos, Documents and Archives.
If the MIME file type matches then we will put the file to the designated folder.'''
CATEGORIES = { # MIME type are actually a string like 'image/png'
    'image': 'Images',
    'video': 'Videos',
    'audio': 'Audio',
    'text': 'Documents',
    'application/pdf': 'Documents',
    'application/msword': 'Documents',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'Documents',
    'application/vnd.ms-excel': 'Documents',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'Documents',
    'application/zip': 'Archives',
    'application/x-rar': 'Archives',
    'application/x-7z-compressed': 'Archives',
    'application/x-tar': 'Archives',
}# note: It will be better if you use ai to get the MIME file types .

# Helper function to detect category . This method works like a filter for the MIME types we will get from the files.
'''What is does: It loops through our CATEGORIES we made and checks if the mime type starts with any of those keys .
When the key matches it will put the file in designated folder .
If the key doesn't match then it will put the file in "Others" folder .'''
def detect_category(mime_type: str) -> str:
    """Return folder category name based on MIME type."""
    for key, folder in CATEGORIES.items():
        if mime_type.startswith(key):
            return folder
    return 'Others'