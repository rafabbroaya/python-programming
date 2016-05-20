'''
Created on May 17, 2016

@author: rafael
'''
name = input('Enter your name\n')
if name == 'rafael':
    print('Hello rafael')
else:
    print('Hello '+name)

if name == 'erick':
    print('Hello erick')
elif name == 'jose':
    print('Hello jose')

'''If elif else'''
age = input('Enter his age!\n')
age = int(age)
if age < 10:
    print('You are a kiddo')
elif age < 20:
    print('You are young')
else:
    print('You are adult')
    
'''while loop'''
spam=0
while spam<5:
    print(spam)
    spam = spam +1

'''Break statement'''
while True:
    name = input('please type your name.')
    if name == 'rafa':
        break
print('thank you')

'''continue statement'''
while True:
    name = input('Enter your name\n')
    if name != 'rafa':
        continue
    password = input('Hello rafa. What is the password? (It is a name)\n')
    if password == 'password':
        break
print('Access granted')

'''truthy and falsey'''

namet = ''
while not namet:
    namet = input('enter your no name')
    