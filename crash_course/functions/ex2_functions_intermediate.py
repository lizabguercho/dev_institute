#Write a function find_largest that takes a list of numbers and returns the largest number in the list.
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_largest([1, 2, 3, 4]))
print(find_largest([10, 20, 5]))

#Write a function check_letter that takes a word and a letter as parameters and checks if the letter is in the word.
# It should return True if the letter is found and False if not.

def check_letter (word, letter):
    return letter in word
print(check_letter("apple", "a"))
print(check_letter("banana", "z"))

#Write a function count_to_number that takes a number as a parameter and prints all numbers from 1 to that number.
def count_to_number(number):
    for num in range(1, number + 1):
        print(num)
count_to_number(3)
count_to_number(5)

