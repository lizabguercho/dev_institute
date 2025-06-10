#Given a list [1, 2, 3, 4], print out all the values in the list one by one.
nums = [1, 2, 3, 4]
for i in nums:
    print(i)

#Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.
nums2 = [1, 2, 3, 4]
for i in nums2:
    print(i*20)

#Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].
names = ["Elie", "Tim", "Matt"]
new_list_comp = [name[0] for name in names]

#Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].
nums3 = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in nums3 if num % 2 == 0]

#Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].
num4 = [1, 2, 3, 4]
num5 = [3, 4, 5, 6]
same_values_list = [num for num in num4 if num in num5]

#Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].
names1 = ["Elie", "Tim", "Matt"]
lowercased= [name[::-1].lower() for name in names1]

#Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].

s1 = "first"
s2 = "third"
letters = list (set("first").intersection(set('third')))

#For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].

division_by_twelve = [num for num in range(1,101) if num % 12 == 0]

#Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].
word = "amazing"
no_vowels = [letter for letter in word if letter not in "euiyao"]

#Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
small_matrix = [[0,1,2]] * 3

#Generate a list with the following structure:
big_matrix = [list(range(10))] * 10