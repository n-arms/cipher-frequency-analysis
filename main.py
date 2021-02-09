from queue import PriorityQueue
import json


lower_case = "abcdefghijklmnopqrstuvwxyz"
alphabet = {i for i in lower_case+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

with open("data.json") as json_file:
    with open("example.txt") as text:
        data = json.load(json_file)
        letters = {i: 0 for i in lower_case}
        for line in text:
            for char in line:
                if char in alphabet:
                    letters[char.lower()] += 1
        print(letters)
        
