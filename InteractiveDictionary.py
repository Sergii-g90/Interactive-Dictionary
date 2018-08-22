import json, difflib
from os import system, name

#loading data from json file to 'data' variable (dictionary type)
data = json.load(open("Data/data.json"))

#Search for the word function
def search_word (dictionary):
    word = input("Enter the search word: ")
    #making a word lowercase as in the file we have only lowercase values for the keys
    word = word.lower()
    if word in dictionary:
        #returns description of the found word
        print("Meaning(s) of the word {0}:\n{1}".format(word, possible_meaning(word,dictionary)))
    else:
        matches_check(word, dictionary)

def possible_meaning (word, dictionary):
    poss_meanings = ''
    for item in dictionary[word]:
        poss_meanings = poss_meanings + '-' + item + '\n'
    return poss_meanings


def matches_check (word, dictionary):
    #if word is not found we are checking for matching words, in case there was mistake in the word
    list_of_matches = difflib.get_close_matches(word, dictionary.keys())
    if list_of_matches != [] :
        matching_words = ''
        i = 1
        for item in list_of_matches:
            matching_words = matching_words + str(i) + '-' + item + '\n'
            i += 1
        word_number = input("Did you mean one of word(s):\n{}? \nIf yes type the number of the word if no type N\n".format(matching_words))
        try:
            if int(word_number) < len(list_of_matches):
                print("Meaning(s) of the word {0}:\n{1}".format((list_of_matches[int(word_number)-1]), possible_meaning(list_of_matches[int(word_number)-1],dictionary)))
            else:
                print("There is no such word in the list, please try new search\n")
                search_word(dictionary)
        except:
            if word_number.upper() == 'N':
                print("Please check search word and try again\n")
                search_word(dictionary)
            else:
                print("There is no such command, please try new search\n")
                search_word(dictionary)
    else:
        print(list_of_matches)
        print("There is no such word")

#Main menu
def main_menu():
    print("\nFill in 'search' to search for a word definition \nFill in 'exit' to exit the progrma")
    command = input("Please fill in a command: ")
    if command == 'search':
        search_word(data)
        print("\n\n")
    elif command == 'exit':
        return exit()
    else:
        print("\n\nIt's not correct command, try again.\n\n")
        main_menu()

while True:
    main_menu()
