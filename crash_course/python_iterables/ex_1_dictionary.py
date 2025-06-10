#Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this:
# {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).
list1= [("name", "Elie"), ("job", "Instructor")]
my_dict = dict(list1)
print(my_dict)

#Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"],
#return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
cap = ["CA", "NJ", "RI"]
city = ["California", "New Jersey", "Rhode Island"]
combined = dict(zip(cap, city))
print(combined)

combined2 = {}
cap_len = len(cap)
for i in range(cap_len):
    combined2[cap[i]] = city[i]
print()

# Create a dictionary where the keys are vowels in the alphabet and the values are 0.
# Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = {vowel: 0 for vowel in vowels}
print(vowel_dict)

for vowel in vowels:
    vowel_dict[vowel] = 0
print(vowel_dict)

#Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself.
# You should return something like this:

alphabet = {}
for i in range(65,65+26):
    alphabet[i-64] = chr(i)

print(alphabet)
