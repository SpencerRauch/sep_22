import random

groups = [1,2,3,4,5,6,7,8]

while len(groups) > 1:
    random_choice = random.choice(groups)
    groups.remove(random_choice)
    print(random_choice)
    input("enter to select again")