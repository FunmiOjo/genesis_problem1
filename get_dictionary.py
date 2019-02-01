import os, urllib.request

def get_dictionary():
  url = 'https://raw.githubusercontent.com/jesstess/Scrabble/master/scrabble/sowpods.txt'
  with urllib.request.urlopen(url) as response:
    text = response.read().decode('utf-8')
    scrabble_dictionary = open('sowpods.txt', 'w+')
    scrabble_dictionary.write(text)
    scrabble_dictionary.close()