import random

guesses = 0
d = {1: 'R', 2: 'G', 3: 'B', 4: 'W'}
numbers = [random.randint(1,4) for _ in range(4)]
numbers = [d[n] for n in numbers]

while True:
    i = 0
    correct = 0
    correct_color = 0
    
    guess = input('Enter your guess (XXXX format): ')
    
    for n in numbers:
        if n == guess[i]:
            correct += 1
        if guess[i] in numbers:
            correct_color += 1
        i += 1
        
    if guess == 'quit':
        print('The code was',numbers)
        print('You took',guesses,'guesses')
        break
    
    guesses += 1
    
    if correct == 4:
        print('Congrats, you have cracked the code.')
        print('You took',guesses,'guesses')
        break
    else:
        print('You have guessed',str(correct),'correct pieces')
        print('You have guessed',str(correct_color),'correct colors')



