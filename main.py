name = input("Enter your name: ")
age = int(input("Enter your age: "))
color = input("Enter your favorite color: ")
if age < 13:
	print("Hello,", name, "you are a child and your favorite color is", color, ".")
if 13 <= age <= 18:
	print("Hello,", name, "you are a teenager and your favorite color is", color, ".")
if age > 18:
	print("Hello,", name, "you are an adult and your favorite color is", color, ".")