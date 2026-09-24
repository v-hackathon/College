# 11. Find the maximum of three numbers
def maximum_of_three(a, b, c):
    return max(a, b, c)


# 12. Count vowels in a string
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count


# 13. Reverse a string
def reverse_string(text):
    return text[::-1]


# 14. Check whether a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]


# 15. Find the sum of all elements in a list
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 16. Find the largest element in a list
def largest_element(numbers):
    return max(numbers)


# 17. Remove duplicate elements from a list
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


# 18. Count how many times an element appears in a list
def count_element(numbers, element):
    count = 0
    for num in numbers:
        if num == element:
            count += 1
    return count


# 19. Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# 20. Return all prime numbers between two numbers
def primes_between(start, end):
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    return primes


# 21. Calculate Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


# 22. Find the second-largest number in a list
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]


# 23. Sort a list without using sort()
def sort_list(numbers):
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result


# 24. Merge two lists and remove duplicates
def merge_and_remove_duplicates(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result


# 25. Accept any number of arguments using *args
def sum_args(*args):
    total = 0

    for num in args:
        total += num

    return total


# 26. Accept keyword arguments using **kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# 27. Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# 28. Recursive function to calculate sum from 1 to n
def sum_to_n(n):
    if n == 0:
        return 0

    return n + sum_to_n(n - 1)


# 29. Find the frequency of each word in a sentence
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# 30. Check whether two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == \
           sorted(str2.replace(" ", "").lower())
