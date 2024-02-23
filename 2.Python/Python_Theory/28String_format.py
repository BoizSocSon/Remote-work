# # str.format =    optional method that gives users
# #                 more control when displaying output

# animal = "cow"
# item = "moon"
# print("The", animal, "jumped over the", item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {1}".format(animal, item)) #positional argument
# print("The {item} jumped over the {animal}".format(animal = "cow", item = "moon")) #keyword argument
# text = "The {1} jumped over the {1}"
# print(text.format(animal, item))



# name = "Bro"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name)) # adding padding to value
# # Output is "Hello, my name is Bro       . Nice to meet you"

# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# # Output is "Hello, my name is Bro       . Nice to meet you"

# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# # Output is "Hello, my name is        Bro. Nice to meet you"

# print("Hello, my name is {:^10}. Nice to meet you".format(name))
# # Output is "Hello, my name is    Bro    . Nice to meet you"

# print("Hello, my name is {name:>10}. Nice to meet you".format(name = "Bro"))
# print("Hello, my name is {0:10}. Nice to meet you".format(name))


number = 1000000000000000

# print("The number pi is {:.2f}".format(number))
# print("The number pi is {:.2}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) # Binary
print("The number is {:o}".format(number)) # Octo
print("The number is {:x}".format(number)) # hex
print("The number is {:X}".format(number)) # HEX
print("The number is {:E}".format(number)) # Show scientific
