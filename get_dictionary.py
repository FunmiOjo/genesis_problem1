import os, urllib.request

# retrieves Scrabble dictionary
def get_dictionary():
  url = 'https://raw.githubusercontent.com/jesstess/Scrabble/master/scrabble/sowpods.txt'
  with urllib.request.urlopen(url) as response:
    text = response.read().decode('utf-8')
    scrabble_dictionary = open('sowpods.txt', 'w+')
    scrabble_dictionary.write(text)
    scrabble_dictionary.close()

# adds additional strings to the dictionary
def write_lines(lines):
  scrabble_dictionary = open('sowpods.txt', 'a')
  for line in lines:
    scrabble_dictionary.write(line)
  scrabble_dictionary.close()

def create_complete_dictionary():
  get_dictionary()
  write_lines(['A\n', 'I\n', 'O\n'])