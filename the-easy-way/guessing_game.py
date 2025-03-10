import random

secret_number = random.randint(1,10)

guess = 0

while guess != secret_number:
	guess = int(input("Guess a number: "))

	if guess < secret_number:
		print("Go higher, please ")
	elif guess>secret_number:
		print("Lower kiasi")
	else:
		print("Got it!")
