# Initial list, outside the loop so it's not erased each time!
classes = []

# initial ask for input from the User, giving a range
totalClasses = int(input('How many classes are you taking this semester? '))

# Looping through that range and prompting n number of times to get classes
for n in range(totalClasses):
    entry = input('Enter class name: ')
    # each loop adds the entry to the list
    classes.append(entry)

# Then another for loop goes through the list and prints each entry out
print("\nThe classes you're taking are:")
for n in classes:
    print(n)
