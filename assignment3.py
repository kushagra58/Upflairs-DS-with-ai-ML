# Question:- 1

def calculate_bill(price, quantity, discount):
    total = price * quantity
    discountAmount = total * discount / 100
    finalAmount = total - discountAmount
    return finalAmount


price = int(input('Enter Price:')) 
quantity = int(input('Enter Quantity:'))
discount = int(input('Enter discount:'))

total = calculate_bill(price,quantity,discount)
print(f'Final bill for price {price} after applying dicount of {discount}$ is :',total)

# Question:- 2

def calculate_salary(basic, bonus=2000, tax=10):
    grossSalary = basic + bonus
    taxAmount = grossSalary * (tax / 100)
    netSalary = grossSalary - taxAmount
    return netSalary

basic = int(input('Enter Basic Pay:'))
bonus = int(input('Enter Bonus Amount:'))
tax = float(input('Enter Tax Percent:'))


print('Using Only Basic Pay:',calculate_salary(basic=basic))
print('Using All Three Parameters:',calculate_salary(basic=basic,bonus=bonus,tax=tax))

# Question:- 3


def find_max(*numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

result = find_max(10, 45, 23, 67, 12,87)
print("Largest number:", result)

# Question:- 4

def student_details(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

student_details(
    Name="Kushagra",
    Age=2,
    Course="Python",
    City="Jaipur"
)

# Question:- 5

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter number of terms: "))
fib_list = []
for i in range(n):
    fib_list.append(fibonacci(i))
print(fib_list)

# Question:- 6

numbers = [5, 12, 17, 18, 24, 15,120]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x ** 2, even_numbers))

print("Even Numbers:", even_numbers)
print("Squares:", squares)
    

