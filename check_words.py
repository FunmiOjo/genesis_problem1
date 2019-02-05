# For each word, take out a character and check if the word is in the dictionary
# If it is, take a another character from the new word and check if the new
# word is in the dictionary.
import os
from sort_words import sort_words 
from get_dictionary import create_dictionary_hash_table, create_complete_dictionary 

def setup():
  create_complete_dictionary()

# removes the character at the given index and returns the resulting word
def splice(word, index):
  if index == 0:
    return word[1:]
  if index == (len(word) - 1):
    return word[:-1]
  result = word[0:index] + word[index + 1:]
  return result

def is_in_dictionary(word):
  return word in dictionary_table

# recursively checks whether words and subwords are in dictionary
def check_word_permutations(word):
  if len(word) == 0:
    return True

  if not is_in_dictionary(word):
    return False
  else:
    for i in range(len(word)):
      word_with_one_char_removed = splice(word, i)
      if check_word_permutations(word_with_one_char_removed) == True:
        return True
    return False

# checks to find first word that satisfies requirements. this word will be the longest
# because the list of words is sorted from longest to shortest
def find_valid_word():
  for i in range(len(sorted_words)):
    print('Checking {0} (length: {1})'.format(sorted_words[i], len(sorted_words[i])))
    if check_word_permutations(sorted_words[i]) == True:
      return sorted_words[i]
  return 'No valid words'

# checks to see whether the Scrabble dictionary has already been downloaded
def dictionary_exists():
  for files in os.walk(os.getcwd()):
    if 'sowpods.txt' in files:
      return True
  return False

if not dictionary_exists():
  setup()
  
sorted_words = sort_words() # list of dictionary words sorted from longest to shortest
dictionary_table = create_dictionary_hash_table()
print(find_valid_word())


