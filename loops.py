#1. Print numbers from 1 to 10 using a for loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

#2. Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

#3. Print the multiplication table of a number.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#4. Find the sum of numbers from 1 to n.
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#5. Find the factorial of a number.
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)

#6. Print all even numbers between 1 and 100.
for i in range(2, 101, 2):
    print(i)

#7. Reverse a number using a loop.
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse =", reverse)

#8. Count the digits of a number.
n = int(input("Enter a number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits =", count)

#9. Check whether a number is prime.
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")

#10. Print Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b









