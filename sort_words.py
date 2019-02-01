def sort_words():
  text = open('sowpods.txt')
  words = []
  for line in text:
    words.append(line)
  words.sort(key=lambda word: len(word), reverse=True)
  return words

sort_words()