import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(''' Bagels, a deductive logic game.
          
        I am thinking of a {}-digit number with no repeated digits. 
        Try to guess what it is. Here are some clues:
When I say:         That means:
          Pico      One digit is correct but in the wrong position
          Fermi     One digit is correct and in the right position
          Bagels    No digit is correct

          For example, if the secret number was 248 and your guess was 843, the
26. clues would be Fermi Pico.
          
          '''.format(NUM_DIGITS))
    
    while True: #this is the main game loop
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES



def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits"""
    number = list('0123456789') #this creates a list of digits 0-9
    random.shuffle(numbers) #shuffle them into random order

    #Get the first NUM_DIGITS digits in the lis for the secret number:

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels, clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')

        elif guess[i] in secretNum:
            #A correct digit in the wrong place
            clues.append['Pico']
    
    if 
