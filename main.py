#Project Hangman
import random
import string
from words import words
def valid_word(words):
  word=random.choice(words)
  while('-' in word or ' ' in word):
    word=random.choice(words)
  return word

def hangman():
  word=valid_word(words)
  lives=7                #HANGMAN
  word_letters=set(word)

  
  alpha=set(string.ascii_lowercase)
  used_letter=set()

  
  #getting input from user
  while(len(word_letters)!=0 and lives!=0):
    #letter used print
    print(f'You have {lives} lives left and you have used these letters:',''.join(used_letter))

    word_list =[letter if letter in used_letter else '-' for letter in word]
    print('Current word:',' '.join(word_list))
    
    user_input=input('Type letter:')
    #checking whether a valid alphabet
    if (user_input in alpha and (user_input not in used_letter)):
      used_letter.add(user_input)
      if user_input in word_letters:
        word_letters.remove(user_input)
      else:
        print('Letter doesnt belong in the word,Try again!')
        print('\n')
        lives-=1
    elif user_input in used_letter:
      print('Already typed,enter a different letter')
      print('\n')
    else:
      print('invalid character')
      print('\n')
  if(lives==0):
    print(f'You died the word is {word}')
  else:
    print('Wonderful you got it right!!')
if __name__=='__main__':
  hangman()
  

