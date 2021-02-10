from queue import PriorityQueue
import json

lower_case = "abcdefghijklmnopqrstuvwxyz"
alphabet = {i for i in lower_case+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
upper_case = {i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


def caesar(file_name, shift):
    encodings = {lower_case[i]: lower_case[(shift+i)%26] for i in range(26)}
    
    with open(file_name) as text:
        for line in text:
            for char in line:
                if char in alphabet:
                    if char in upper_case:
                        print(encodings[char.lower()], end='')
                    else:
                        print(encodings[char], end='')
                else:
                    print(char, end='')

with open("data.json") as json_file:
    data = json.load(json_file)
    
with open("example.txt") as text:
    letters = {i: 0 for i in lower_case}
    for line in text:
        for char in line:
            if char in alphabet:
                letters[char.lower()] += 1
    ordering = PriorityQueue()
    for i in letters:
        ordering.put((-1*letters[i], i))
    decoded = {}
    i = 0
    while not ordering.empty():
        encoded = ordering.get()
        decoded[encoded[1]] = data["frequency-letters"][i]
        i += 1

with open("example.txt") as text:
    for line in text:
        for char in line:
            if char in alphabet:
                print(decoded[char.lower()], end='')
            else:
                print(char, end='')



    
    
        
