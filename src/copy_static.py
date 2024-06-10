import os
import shutil

def copy_directory(src, dest):
    # Copy the contents of the source directory to the destination directory
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            if os.path.exists(d) == False:
                os.mkdir(d)
            
            copy_directory(s, d)
        else:
            shutil.copyfile(s, d)