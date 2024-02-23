class Employee:
    def __init__(self, value): # Này là một thuộc tính
        self.salary = value
    # Sau khi hàm khởi tạo được hoạt động value sẽ nhận giá trị là 2000
    # Self bây giờ tương đương với Test
    # self.salary = Test.salary
    # Và thuộc tính self.salary(Test.salary) = value tương đương với việc thuộc tính salary của Test đã mang giá trị là 2000
        
    def print_salary(self): # Này là một phương thức
        print(self.salary)

Test = Employee(2000) # Khởi tạo biến e là một lớp (tương đương struct của c)
# Truyền giá trị vào lớp 

Test.print_salary()

