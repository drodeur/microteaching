from PIL import Image;
import os;

SECRET_FOLDER_PATH = "./secret/";

def isImage(path):
  try:
    Image.open(path);
    return True;
  except IOError:
    return False;

for fileName in os.listdir(SECRET_FOLDER_PATH):
  if isImage(SECRET_FOLDER_PATH + fileName):
    newName = ''.join(char for char in fileName if not char.isdigit());
    os.rename(SECRET_FOLDER_PATH + fileName, SECRET_FOLDER_PATH + newName);
