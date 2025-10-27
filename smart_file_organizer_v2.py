import os # os module helps to interact with the operating system it's self . it will look on the files if they are there
import shutil # shutil module helps move files around or copying them it helps with file operations
import magic # magic module reads the insides of a file and says what type is it even if the file name lies
from datetime import datetime # gives us the current datetime 

# configuration ---- we will point out scripts here 
SOURCE_DIR = r"The path of the folder you want to organize" # use your own file path here . i used mine while testing 
DEST_DIR = os.path.join(SOURCE_DIR, 'Organized') # this will move all the files in a folder called Organized 

# if Organized file doesn't exists make it . if exists then do nothing
os.makedirs(DEST_DIR, exist_ok=True) # this will create the Organized folder if the folder doesn't exist and then move the files there 

