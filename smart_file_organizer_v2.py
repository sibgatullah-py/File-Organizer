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

# Helper function ti get date folder. you can skip this method as it's only for testing here not necessary for the application

def date_folder(file_path: str) -> str:
    """returns year-month-date folder name based on the file modification date. """
    mtime = os.path.getatime(file_path)# This grabs the last access time(last time the file was opened or read)
    date = datetime.fromtimestamp(mtime)# Turns that time stamp we got into a readable date/time object
    return date.strftime("%Y-%m-%d")# formates that date into a string like year-month-date

# Main working method : Organize_files()

def organize_files():
    print("Starting Smart Organization...\n")
    
    for filename in os.listdir(SOURCE_DIR): # this list every name(file or folder) inside the SOURCE_DIR.
        file_path = os.path.join(SOURCE_DIR, filename)# Build the full path for each name (so we can open or move it)
        
        # Skip directories
        if os.path.isdir(file_path): # if the name is a folder , skips it as we only want to organize files not some folders 
            continue
        
        
        try:
            # Detect file content type
            mime_type = magic.from_file(file_path, mime=True)# asking the magic module to read the file's content and say what it is and give me the MIME string
            category = detect_category(mime_type) # convert the MIME type string into a folder
        except Exception as e:
            # if anything goes wrong print a warning
            print(f"could not read {filename}: {e}")
            category = 'Unknown'
            
        # Create folder for category and date
        date_folder = date_folder(file_path)# find the file's year-month-date
        dst_folder = os.path.join(DEST_DIR, category, date_folder)# Build the final destination folder path 
        os.makedirs(dst_folder, exist_ok=True)# make the destination folder if it doesn't exists
        
        # Move file to destination folder
        dst_path = os.path.join(dst_folder, filename) # full path where the file will be moved
        shutil.move(file_path, dst_path) # moving the file to the full path with shutil module
        
        print(f"{filename} -> {category}/{date_folder}")# tells what i moved 
        
        
        
        
print("\n All files organized successfully")# success message after iterating over all the files
print(f"Organized structure saved under: {DEST_DIR}")





# This is standerd Python to run the file directly as we know we can use any python method as packages in other files by importing
if __name__ == '__main__':
    organize_files()