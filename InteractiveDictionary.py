import json

#loading data from json file to 'data' variable (dictionary type)
data = json.load(open("Data/data.json"))

#Search for the word function
def search_word (dictionary):
    word = input("Enter the search word: ")
    #making a word lowercase as in the file we have only lowercase values for the keys
    word = word.lower()
    if word in dictionary:
        #returns description of the found word
        print("Meaning of the word: ", dictionary[word])
    else:
        print("There is no such word")

#Main menu
def main_menu():
    print("Fill in 'search' to search for a word definition \nFill in 'exit' to exit the progrma")
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
