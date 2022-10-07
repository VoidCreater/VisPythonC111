import os
import shutil

# copying the Badminton.gif and renaming(badminton2.gif) it in desktop
os.getcwd()
path = "C:\\Users\\JOY\OneDrive\\Desktop\\img\Badminton2.gif"
path2 = "C:\\Users\JOY\\OneDrive\\Desktop\Badminton3.gif"
destination = shutil.copy(path, path2)

# completely moving(cutting) the Badminton.gif and renaming(badminton2.gif) it in desktop
os.getcwd()
path = "C:\\Users\\JOY\\OneDrive\\Desktop\\img\Badminton2.gif"
path2 = "C:\\Users\\JOY\\OneDrive\\Desktop\Badminton3.gif"
destination = shutil.move(path, path2)
