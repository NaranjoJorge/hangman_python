import random
import os

def read_data():
	with open('./files/data.txt', 'r', encoding='utf-8') as f:
		data = [line.strip('\n') for line in f]
	return data

def normalize(s):
	replacements = (('á', 'a'),('é', 'e'),('í', 'i'),('ó', 'o'),('ú', 'u'))
	for a,b in replacements:
		s = s.replace(a, b)
	return s

def run():
	word = normalize(read_data()[random.randint(0, len(read_data()) - 1)])
	guess = '_' * len(word)
	print('Welcome to Hagman. Guess the word.')

	while word != guess:
		print (guess)
		letter = input('\nChoose a letter:')
		numbered_word = list(enumerate(word))
		guess = list(guess)
		for a, b in numbered_word:
			if letter == b:
				guess[a] = b
		guess = ''.join(guess)
		os.system('clear')
	print('You won!')

if __name__ == '__main__':
	run()
