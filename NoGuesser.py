import random 
Number = random.randint(1,9)
chances = 0
while chances < 5:
	guess=int(input('Enter your guess: '))

	if guess == Number: 
		print("Congratulations You Won!!")
        

	elif guess>Number: 
		print('Your guess is high. Guess lower number') 

	elif guess<Number:
		print('Your guess is low. Guess higher number') 
	chances += 1

if not chances <5:
	print('You Loose !! The Number is:',Number) 
