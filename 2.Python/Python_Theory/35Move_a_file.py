import os

source = "D:\\Study\\MyCode\\test.txt"
destination = "D:\\Study\\MyCode\\2.Python\\test1.txt"

try:
    if(os.path.exists(destination)):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source, "was moved")
except FileNotFoundError:
    print(source, "was not found")