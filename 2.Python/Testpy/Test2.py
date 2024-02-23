class Car:
  so_xe = 0
  tong_tieu_thu = 0

  def __init__(self, make, model, mpg):
    self.make = make
    self.model = model
    self.mpg = mpg
    Car.so_xe += 1
    Car.tong_tieu_thu += mpg

  @classmethod
  def tinh_tieu_thu_trung_binh(cls):
    if cls.so_xe == 0:
      return 0
    return cls.tong_tieu_thu / cls.so_xe

# Tạo các đối tượng xe
car1 = Car("Toyota", "Camry", 35)
car2 = Car("Honda", "Civic", 40)

# Tính toán mức tiêu hao nhiên liệu trung bình
tieu_thu_trung_binh = Car.tinh_tieu_thu_trung_binh()

# In thông tin
print(f"Mức tiêu hao nhiên liệu trung bình: {tieu_thu_trung_binh:.2f} mpg")
