import os

BASE_DIR = os.getcwd() # get base directory info
MEDIA_DIR = 'static/media' # where we want to save info/files

SAVE_DIR = os.path.join(BASE_DIR,MEDIA_DIR)

def join_path(directory,filename):
    filepath = os.path.join(directory,filename)
    return filepath
