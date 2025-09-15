# create a program that can take in input of the users name
# save the name in variable
# pass the variable through a function and print "Hello ______"

name = str(input('please enter your name: '))

def function(name):
    print(f'Hello {name}')

function(name)
