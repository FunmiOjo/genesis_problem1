This application finds the longest word in a Scrabble dictionary where when one
letter at a time is removed from the word, each resulting word is also a valid
word in the dictionary.

To run the application, go the directory in which you wish to run it and type in
the command line
```
git clone https://github.com/FunmiOjo/genesis_problem1.git
cd genesis_problem1 
python3 check_words.py
```
# Extra credit
The asymptotic computational complexity of this approach, given a dictionary of
N words and with average length k,  is O(n * k).  In the worst-case scenario,
there may be no words in the dictionary that satisfy the requirements and we will
have to look at all of them; this will take O(n) time.  For each word, we will have
to check whether k subwords are in the dictionary; this will take O(k) time.  Because
in this approach the dictionary is stored in a hash table, the lookups take constant
time.