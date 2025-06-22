#Write a function add_two_numbers that takes two numbers as parameters and returns their sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(3,5))
print(add_two_numbers(10,20))

#Write a function greet that takes one parameter, a person’s name, and prints a greeting message like “Hello, [name]!”.
def greet(name):
    print(f'Hello,{name}!')
greet("Alice")
greet("Bob")

#Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(4)
check_even_odd(7)

#Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.
def sum_list(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4]))
print(sum_list([5,5,5]))

#Write a function print_days that prints the days of the week (Sunday, Monday, Tuesday, etc.) using a loop.
import calendar
def print_days():
    days = list(calendar.day_name)
    days = days[-1:] + days[:-1]
    for day in days:
       print(day)
print_days()

#Write a function check_sign that takes a number and prints whether the number is positive, negative, or zero.
def check_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print ("Negative")
    else:
        print("Zero")
check_sign (10)
check_sign (-5)
check_sign (0)

#Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.

def repeat_word (word: str, number: int):
    for _ in range(number):
        print(word)
repeat_word("hello",3)
repeat_word("goodbye",2)