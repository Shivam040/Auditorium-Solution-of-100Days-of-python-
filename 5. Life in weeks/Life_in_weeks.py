# Creating a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.

age = input()
weeks_lived = int(age) * 52
weeks_left = 4680 - weeks_lived
print(f"You have {weeks_left} weeks left.")