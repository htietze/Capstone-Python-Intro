# first inputs, asking for name and bday month
name = input('what is your name? ')
bday = input('what month were you born in? ')
# then the name is printed, easy, except remembering the formatting syntax to plug in the name variable
print(f'hello, {name}!')
# .lower() so it can be checked against the string, so AuGuST still works
if bday.lower() == 'august' :
    print('Happy birthday month!')

# applying the length command to the name variable, printed in the string.
print(f'your name is {len(name)} letters long')
