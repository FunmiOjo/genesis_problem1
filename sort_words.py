# sort words by length
def sort_words():
  text = open('sowpods.txt')
  words = []
  for line in text:
    line_without_newline = line[:-1]
    words.append(line_without_newline)
  words.sort(key=lambda word: len(word), reverse=True)
  return words