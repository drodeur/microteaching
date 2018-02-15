# Microteaching: Making program is not so hard
## Get the project

- Download the source of the project on [https://github.com/drodeur/microteaching](https://github.com/drodeur/microteaching) via the button “Clone or Download” and select “Download ZIP”.
- [OPTIONAL] Install an IDE to benefit of syntax highlight, I personally use Sublime Text 3, but you could code in bloc note if you don’t want to install an IDE [https://www.sublimetext.com/3](https://www.sublimetext.com/3).

## Code the project

```python
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
```

## Run the project

- Verify that the images in the `C:\YOUR_PATH\microteaching\demonstation1\secret` are shuffle.
- Install python on your machine [https://www.python.org/downloads/](https://www.python.org/downloads/).
- Open a terminal (linux/mac) or type cmd + enter.
- Go in the folder of the project using `cd C:\YOUR_PATH\microteaching\demonstation1`.
- Run the command `python secret-complete.py`.
- Navigate through the folder secret, the secret message will be revealed.
- Use the `C:\YOUR_PATH\microteaching\demonstation1\secret.zip` to repeat the experience.

You can make your own secret message using PAINT and the font that you want. To do that create a copy of an empty sheet like `2chennai.jpg` and write the letter that you want. Compose your own unique message using only letters in the file name. Prefix with digits to shuffle the sequences of images. Show your new skills to a friend.
