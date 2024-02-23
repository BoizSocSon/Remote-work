text1 = "Yooooo\nThis is some text\nHave a good one!\n"
text2 = "\n\nAdded a new line\n\n"

with open('D:\\Study\\MyCode\\2.Python\\test1.txt', 'a') as file:
    file.write(text1)
    file.write(text2)

