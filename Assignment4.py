# Question :- 1
def my_function(**myvar):
    print("Type: ", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("all data:", myvar)
my_function(name="John", age=36)


# Question :- 2
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number: "))
print("the factorial of", n, "is", fact(n))

# Question :- 3
try:
    f=open("demo.txt","w")
    try:
        f.write("Hello, world!\n")
    except:
        print("An error occurred while trying to write to the file")
    finally:
        f=open("demo.txt","r")
        print(f.read())
        f.close()
        print("File closed")

except:
    print("An error occurred while trying to open the file")


# Question :- 4
import json
student = {
    "name": "Kushagra Gupta",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Dictionary stored in student.json")
with open("student.json", "r") as file:
    data = json.load(file)
print("Data read from JSON file:")
print(data)

# Question :-  5
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
