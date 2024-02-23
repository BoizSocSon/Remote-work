import os
import shutil

path1 = "D:\\Study\\MyCode\\2.Python\\test1.txt"
path2 = "D:\\Study\\MyCode\\2.Python\\empty_folder"
path3 = "D:\\Study\\MyCode\\2.Python\\folder"

try:
    # os.remove(path1) # delete a file
    # os.rmdir(path2)   #delete an empty directory
    shutil.rmtree(path3)    #delete a directory containing files (all files and folders in that directory)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You can not delete that using that function")
else:
    print(path3, "was removed successfully!")