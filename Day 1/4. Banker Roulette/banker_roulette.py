#Instructions:
#Sample Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

import random
name_string = input()
names = names_string.split(", ")
random_index = random.randint(0,len(names)-1)

print(f"{names[random_index]} is going to buy the meal today!")