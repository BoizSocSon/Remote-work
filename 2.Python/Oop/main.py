class Student:
    school = "UET"

    def __init__(self, order, name, id, year_old, classes):
        self.order = order + 1
        self.name = name
        self.id = id
        self.year_old = year_old
        self.classes = classes

    def change_Infor(self, infor_type, infor):
        if infor_type == "classes":
            self.classes = infor


    def show_Infor(self):
        print(self.order, end=" ")
        print(self.name, end=" ")
        print(self.id, end=" ")
        print(self.year_old, end=" ")
        print(self.classes, end=" ")

student_List = []
num_Student = int(input("Enter the number of students: "))
for i in range(num_Student):
    name = input("Enter student's name: ")
    id = input("Enter student's id: ")
    year_old = int(input("Enter student's year old: "))
    classes = input("Enter student's classes: ")
    print()

    tmp = Student(order=i, name=name, id=id, year_old=year_old, classes=classes)
    student_List.append(tmp)

# student_List[0].show_Infor()
student_List[1].change_Infor("classes", "k1")

for i in student_List:
    print(i.show_Infor())
