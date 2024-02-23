import os

class Student:
  def __init__(self, name, id, year_old, gender):
    self.name = name
    self.id = id
    self.year_old = year_old 
    self.gender = gender

  def delete_Student(self):
    self.name = None
    self.id = None
    self.year_old = None
    self.gender = None
    print("Student has been deleted")

  # def print_Student(self):
  #   print(self.name)
  #   print(self.id)
  #   print(self.year_old)
  #   print(self.gender)

  def __str__(self):
    return f"Name: {self.name}, ID: {self.id}, Age: {self.year_old}, Gender: {self.gender}"

students = []

def add_Student(num_Student):
  for i in range(num_Student):
    name = input("Enter your name: ")
    id = input("Enter your id: ")
    year_old = int(input("Enter your year old: "))
    gender = input("Enter your gender: ")
    tmp = Student(id=id, name=name, year_old=year_old, gender=gender)
    students.append(tmp) # Tại sao lệnh append có thể dùng như này 
    print("\n\n")


def main():
  num_Student = int(input("Enter the number of Student: "))
  add_Student(num_Student)
  for i in range(num_Student):
    print(students[i])
  
main()