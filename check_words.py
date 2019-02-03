# For each word, take out a character and check if the word is in the dictionary
# If it is, take a another character from the new word and check if the new
# word is in the dictionary.

from sort_words import sort_words 
from get_dictionary import create_dictionary_hash_table 

sorted_words = sort_words()

dictionary_table = create_dictionary_hash_table()

def splice(word, index):
  if index == 0:
    return word[1:]
  if index == (len(word) - 1):
    return word[:-1]
  result = word[0:index] + word[index + 1:]
  return result

def is_in_dictionary(word):
  return word in dictionary_table

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

def find_valid_word():
  for i in range(len(sorted_words)):
    print('Checking {0} (length: {1})'.format(sorted_words[i], len(sorted_words[i])))
    if check_word_permutations(sorted_words[i]) == True:
      return sorted_words[i]
  return 'No valid words'

print(find_valid_word())


