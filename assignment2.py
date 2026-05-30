# question 1
correct_pin = 6023
pin=int(input("Enter PIN: "))
if pin != correct_pin:
    print("Incorrect PIN")
balance=float(input("Enter Account Balance: "))
withdraw=float(input("Enter Withdrawal Amount: "))
if withdraw % 100 != 0:
    print("Invalid amount. Amount must be multiple of 100.")
elif withdraw > balance:
    print("Insufficient balance")
else:
    balance -= withdraw
    print("Withdrawal Successful")

    print("Remaining Balance =", balance)


# question 2
year = int(input("Enter Year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
    leap = True
else:
    leap = False
    print(year, "is not a Leap Year")
month = int(input("Enter Month (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Total Days = 31")
elif month in [4, 6, 9, 11]:
    print("Total Days = 30")
elif month == 2:
    if leap:
        print("Total Days = 29")
    else:
        print("Total Days = 28")
else:
    print("Invalid Month")

# question 3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("addition:", num1 + num2)
print("subtraction:", num1 - num2)
print("multiplication:", num1 * num2)
if num2 != 0:
    print("division:", num1 / num2)
    print("modulus:", num1 % num2)
else:   
    print("Error: Division by zero")



# question 4
square=[x**2 for x in range(1, 21)]
print(square)
even_square=[x**2 for x in range(1, 21) if x % 2 == 0]
print(even_square)



# question 5
student={
    "kushagra":85,
    "nikhil":90,
    "OM":95,
    "anupam":80,
    "yogesh":88
}
print("name of students:")
for x in student.keys():
    print(x)
print(student["OM"])
print("Highest marks student:", max(student, key=student.get))
student["vishnu"]=92
print(student)




# question 6
student={
    "name": "kushagra",
    "age": 20,
    "courses":"DS with Python",
}
numbers={10,20,25,30,35}
num_str=input("Enter a number: ")
num=int(num_str)
print("Student details:")
for key, value in student.items():
    print(f"{key}: {value}")
print("Numbers in the set:",numbers)
print("original number in string:", num_str)
print("type of original number:", type(num_str))
print("converted number:", num)
print("type of converted number:", type(num))

