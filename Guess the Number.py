import random
guess = int(input('Guess It'))

number = random.randint(0,100)
if guess != number:
    print('Keep Trying and ')

while guess != number:
    if guess < number:
        print("Go High")
        guess = int(input('Guess It'))
    else:
        print("Go low")
        guess = int(input('Guess It'))
print("yaa")

