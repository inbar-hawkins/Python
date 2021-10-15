# word = 'intelligence'
# tries = 0
# max_tries = 10
# create list that will look like: ['i','-','-','e','-','-','i','-','e','-','-','e']
# after every right guess print the new state of the word (list)
# tries should go up and be printed only when the guess is wrong
# alef_beith = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # till z
# we can delete the letters that the player already used and
# check this for him, or do it in other way, like
# keep a list of the guesses
#
# May be we need use word_l = list(word)
# abc = 'abcdefghijklmnopqrstuvwxyz'
# alef_beith = list(abc)


def replaceCharPerIndex(word, i, char):
    word = list(word)
    word[i] = char
    return word


def replaceMulti(word, letter, guess):
    i = word.find(letter)
    num_of_founds = word.count(letter)
    guess = replaceCharPerIndex(guess, i, letter)
    if num_of_founds > 1:
        for num in range(2, num_of_founds + 1):
            i = word.find(letter, i+1)
            guess = replaceCharPerIndex(guess, i, letter)
    return guess


def InitGuess(letter, guess):
    i = word.find(letter)
    guess = replaceMulti(word, letter, guess)
    abc.remove(letter)
    return guess


word = 'intelligence'
tries = 0
max_tries = 10
abc = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
length = len(word)
guess = (' - ' * length).split()
guess = InitGuess('i', guess)
guess = InitGuess('e', guess)
print(guess)

while tries < max_tries and guess != list(word):
    print(f"here are the letters you can choose from:{abc}")
    letter = input('Enter a letter:')
    num_of_founds = word.count(letter)
    if num_of_founds:
        abc.remove(letter)
        guess = replaceMulti(word, letter, guess)
        print(guess)

    else:
        tries += 1
        abc.remove(letter)
        print("WRONG!!")
        print(f"try number {tries} out of {max_tries}.")
        print(abc)

if list(word) == guess:
    print(f"You made it! the word is: {''.join(guess)}")
else:
    print("Maybe you should play backgamon.")
