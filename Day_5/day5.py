student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

maxmin = 0

for score in student_scores:
    if score > maxmin:
        maxmin = score
print(maxmin)


total_score = sum(student_scores)
#
# print(total_score)
# sum_of = 0
# for score in student_scores:
#     sum_of += score
#     print(sum_of)
# print(sum_of)



for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
        
        
        
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# password = ""
#
# for i in range(0 , nr_numbers):
#     password += random.choice(numbers)
#
#
# for i in range(0 , nr_letters):
#     password += random.choice(letters)
#
#
# for i in range(0 , nr_symbols):
#     password += random.choice(symbols)
#
# print("Your password is: " + password)


password = []

for i in range(0 , nr_numbers):
    password += random.choice(numbers)


for i in range(0 , nr_letters):
    password += random.choice(letters)


for i in range(0 , nr_symbols):
    password += random.choice(symbols)

print(password)
random.shuffle(password)
result = ""

for i in password:
    result += i


print(f"Your password is : {result}")
