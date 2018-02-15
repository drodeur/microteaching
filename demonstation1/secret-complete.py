from PIL import Image;
import os;

PRANK_FOLDER_PATH = "./secret/";

def isImage(path):
  try:
    Image.open(path);
    return True;
  except IOError:
    return False;

for fileName in os.listdir(PRANK_FOLDER_PATH):
  if isImage(PRANK_FOLDER_PATH + fileName):
    newName = ''.join(char for char in fileName if not char.isdigit());
    os.rename(PRANK_FOLDER_PATH + fileName, PRANK_FOLDER_PATH + newName);
