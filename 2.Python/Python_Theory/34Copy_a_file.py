# copyfile() = copies contents of a file 
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

# shutil.copyfile('D:\\Study\\MyCode\\2.Python\\test1.txt', 'D:\\Study\\MyCode\\2.Python\\test2.txt') #src, dst
shutil.copy2('D:\\Study\\MyCode\\2.Python\\test1.txt', 'D:\\Study\\MyCode\\2.Python\\test2.txt')