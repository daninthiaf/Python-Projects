##imported libraries
import itertools
import random
import copy

##values of cards in a standard deck
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
##faces of cards in a standard deck
faces = ['clubs', 'diamonds', 'hearts', 'spades']
##list created to create 52 cards in deck (4 faces per value)
deck = list(itertools.product(values, faces))

##get length of the deck
length = len(deck)
##split the deck in half
splitdeck = len(deck) // 2

#first half of eck
half1 = deck[:splitdeck]
##second half of deck
half2 = deck[splitdeck:]

##stores the result returned from the function (inshuffles the cards)
result = []
def func():
    num = 0
    while num < splitdeck:
        if len(half1) >= num:
            result.append(half1[num])
            result.append(half2[num])
        num += 1

    if len(deck) % 2 != 0:
        result.append(half2[num])
    return result

#Infshuffled deck
print ('Inshuffled deck:  ')
for values, faces in func():
        print('The %s of %s' % (values, faces))

## assigns indices to each card (0-51)
x = list(enumerate(result))
##copy of x to prevent mistakes
xcopy = copy.copy(x)
##for loop loops 7 times until the position of the first card is given
for i in range(7):
   random.shuffle(xcopy)
   
##print deck on the 7th iteration
print('Cards shuffled on the 7th time: ')
print(xcopy)
##Position of first card on the 7th iteration
print('Position of first card after 7th shuffle: ')
indices, result = zip(*xcopy)
print (indices.index(0))

## copy x again for each loop task
xcopy1 = copy.copy(x)
##count for how many times then loop is executed
count = 0
##while loop executes until the top is in the bottom card's position
while True:
    indices1, result = zip(*xcopy1)
    if indices1.index(0) != 51:
        random.shuffle(xcopy1)
    else:
            break
    count = count + 1
##final count of loop
print('Shuffle was performed %s time(s) for the top card to become the bottom card. ' %(count))

##copy x for this loop task
xcopy2 = copy.copy(x)
## starts at the initial inshuffle deck
indices2, result = zip(*xcopy2)
## count for this loop
count1 = 0
##shuffle before entering the loop
random.shuffle(xcopy2)
## loop to determine when the top and bottom cards touch in deck or are side by side in a list
while True:
    ##keep track of the indices inside the loop for when shuffles occur
    indices2, result = zip(*xcopy2)
    ## conditional statement to break the loop when the first card and bottom card are in adjacent indices 
    if indices2.index(0) == i and indices2.index(51) == i + 1:
        break
    ## if the previous condiiton is not met, shuffle until it is
    else:
        random.shuffle(xcopy2)
count1 = count1 + 1
## final count
print('First and last cards touch after %s time(s).' %(count1))
