import json

#loading data from json file to 'data' variable (dictionary type)
data = json.load(open("Data/data.json"))

#Search for the word function
def search_word (dictionary):
    word = input("Enter the search word: ")
    if word in dictionary:
        #returns description of the found word
        print("Meaning of the word: ", dictionary[word])
    else:
        print("There is no such word")

while 1 == 1:
    search_word(data)
