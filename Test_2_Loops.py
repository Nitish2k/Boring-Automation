# This program demonstrates a simple if statement.
password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else:
    print('Access denied.') 

# This program demonstrates a while statement.
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

#This program is an example of a while statement (break statement).
name = ''
while name != 'Nitish':
    print('Please type your name.')
    name = input()
    if name == 'Nitish':
        break
print('Thank you!')

#This program is an example of a while statement (continue statement).
spam = 0 
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

#This program is an example of a for statement.
total = 0
for num in range(101):
    total = total + num
print(total)

print('My name is')
i = 0
while i < 5:
    print('Nitish Five Times (' + str(i) + ')')
    i = i + 1