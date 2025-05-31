#Declare a variable called first and assign it to the value "Hello World".
first= "Hello World"
#Write a comment that says "This is a comment."
# This is a comment
#Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER")
#Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 and 4 > 2:
    print("Math is fun")
#Assign a variable called nope to an absence of value.
nope = None
print()
#Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
True and False
#Calculate the length of the string "What's my length?"
print(len("What's my length?"))
#Convert the string "i am shouting" to uppercase.
print(str.upper("i am shouting"))
#Convert the string "1000"to the number 1000.
int("1000")
print(int("1000"))
#Combine the number 4 with the string "real" to produce "4real".
new= str(4)+"real"
print(new)
#Record the output of the expression 3 * "cool".
output = 3 * "cool"
print(output)
#Record the output of the expression 1 / 0
try:
    div = 1/0
except Exception as e:
    print(e)
#Determine the type of [].
print(type([]))
#Ask the user for their name, and store it in a variable called name.
name = input(" What is your name? ")
print(f"My name is {name}")
#Ask the user for a number. If the number is negative, show a message that says
# "That number is less than 0!" If the number is positive,
# show a message that says "That number is greater than 0!" Otherwise,
# show a message that says "You picked 0!.
number = int(input("Give me your number:"))
if number < 0 :
    print("That number is less than 0"),
elif number > 0 :
    print("That number is greater than 0"),
else :
    print("That number is equal to 0")

#Find the index of "l" in "apple"
word = "apple"
index = word.index("l")
print(index)

#Check whether "y" is in "xylophone".
print ("y" in "xylophone")
#Check whether a string called my_string is all in lowercase.
string = "my_string"
print(string.islower())
