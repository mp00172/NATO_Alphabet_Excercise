#TODO 1: Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

import pandas

file_contents = pandas.read_csv("nato_phonetic_alphabet.csv")

# nato_alphabet_dict = {new_key: new_value for (key, value) in dict}
nato_alphabet_dict = {row.letter: row.code for (index, row) in file_contents.iterrows()}
print(nato_alphabet_dict)

#TODO 2: Create a list of the phonetic code words from a word that the user inputs.

user_input = None
while not user_input:
	user_input = input("Enter a word: ")

user_input_list = list(user_input.upper())
print(user_input_list)
# nato_code_list = [item for item in list]
nato_code_list = [nato_alphabet_dict[letter] for letter in user_input_list]
print(nato_code_list)