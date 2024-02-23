try:
    with open('D:\\Study\\MyCode\\2.Python\\test1.txt') as file:
        print(file.read())
except FileExistsError:
    print("That file was not found :(")