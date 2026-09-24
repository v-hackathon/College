#1. Perform addition, subtraction, multiplication, and division. 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


addition = a + b
subtraction = a - b
multiplication = a * b


if b != 0:
    division = a / b
else:
    division = "Cannot divide by zero"


print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

#2. Find the remainder and quotient of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


quotient = a // b
remainder = a % b


print("Quotient:", quotient)
print("Remainder:", remainder)

#3. Check whether a number is even or odd.

num = int(input("Enter a number: "))


if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
#4. Compare two numbers using relational operators.
   
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#5. Demonstrate logical operators (and, or, not).

a = True
b = False


print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)


#6. Demonstrate assignment operators (+=, -=, *=, /=).

a = 10


a += 5
print("After += 5:", a)

a -= 3
print("After -= 3:", a)

a *= 2
print("After *= 2:", a)

a /= 4
print("After /= 4:", a)




#7. Find the largest of two numbers using comparison operators.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number:", a)
else:
    print("Largest number:", b)

