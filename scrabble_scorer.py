# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85
import string

old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

# I made this dict manually before reading the transform section. I'll keep it here so you can laugh at me.
new_point_structure = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
}

# This may seem like overkill, but I do appreciate the validation gained by using this dict.  Now, no spaces, special chars, or numbers are accidentally scored.
vowel_bonus_score_structure = {
    "A": 3,
    "B": 1,
    "C": 1,
    "D": 1,
    "E": 3,
    "F": 1,
    "G": 1,
    "H": 1,
    "I": 3,
    "J": 1,
    "K": 1,
    "L": 1,
    "M": 1,
    "N": 1,
    "O": 3,
    "P": 1,
    "Q": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 3,
    "V": 1,
    "W": 1,
    "X": 1,
    "Y": 1,
    "Z": 1
}

# Sorry I overwrote the old function, but in the end i'm using scrabble_scorer anyway....
def old_scrabble_scorer(word):
    letterPoints = 0

    for char in word.upper():
        if char in new_point_structure:
            letterPoints += new_point_structure[char]

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    print("Let's play some Scrabble!\n")

    user_input = input("Enter a word to be scored: ")
    return user_input


def simple_scorer(word):
    word = word.upper()
    points = 0

    for char in word:
        if char in string.ascii_uppercase:
            points += 1
    
    return points

def vowel_bonus_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:
        if char in vowel_bonus_score_structure:
             letterPoints += vowel_bonus_score_structure[char]
    return letterPoints

def scrabble_scorer(word):
    letterPoints = 0

    for char in word.upper():
        if char in new_new_point_structure:
            letterPoints += new_new_point_structure[char]

    return letterPoints

scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'The traditional scoring algorithm',
    'scoring_function': scrabble_scorer
}

vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'Each vowel is worth 3 points, consonants are worth 1',
    'scoring_function': vowel_bonus_scorer
}

simple_scorer_dict = {
    'name': 'Simple Score',
    'description': 'Each letter is worth 1 point',
    'scoring_function': simple_scorer
}

scoring_algorithms = (
    simple_scorer_dict, 
    vowel_bonus_scorer_dict, 
    scrabble_scorer_dict
    )

def scorer_prompt():

    print("Which scoring method would you like to use?\n")

    for index, algorithm in enumerate(scoring_algorithms):
        print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')

    user_selection = int(input("\nEnter 0, 1, or 2: "))
    scoring_algorithm_dict = scoring_algorithms[user_selection]

    return scoring_algorithm_dict

def transform(provided_dict):
    new_dict = {}

    for (key, value) in provided_dict.items():
        for letter in value:
            new_dict[letter] = key

    return new_dict

# again, new_new because I already manually typed out an entire dict with the name new_point_structure. I ended up using this one though to be compliant :)
new_new_point_structure = transform(old_point_structure)

def run_program():
    word = initial_prompt()

    scoring_algorithm_dict = scorer_prompt()

    score = scoring_algorithm_dict['scoring_function'](word)

    print(f"The score for '{word}' is: {score}")

