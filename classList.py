classes = []
totalClasses = int(input('How many classes are you taking this semester? '))

for n in range(totalClasses):
    entry = input('Enter class name: ')
    classes.append(entry)

print("\nThe classes you're taking are:")
for n in classes:
    print(n)
