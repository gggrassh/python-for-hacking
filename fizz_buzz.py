# fizzbuzz
# if a number is divisible by 3, print fizz
# if a number is divisible by 5, print buzz
# if a number is divisible by both, print fizzbuzz

num = int(input('please enter a number: '))
if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
elif num % 5 == 0:
    print('buzz')
elif num % 3 == 0:
    print('fizz')
else:
    print('something went wrong')