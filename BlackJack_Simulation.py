import random
from random import shuffle


#Function to create the card Deck Ace=11
def deck():
    deck = []
    #for loop to create 4 cards for each value
    for i in range(4):
        deck.append(2)
        deck.append(3)
        deck.append(4)
        deck.append(5)
        deck.append(6)
        deck.append(7)
        deck.append(8)
        deck.append(9)
        deck.append(10)
        deck.append('J')
        deck.append('Q')
        deck.append('K')
        deck.append(11)
    return deck

#Function to draw and return two random cards from the deck
def draw(deck):
    deck1 = deck
    #Empty 'hand' list to append cards to
    hand = []
    #loop to draw two random cards from deck
    for i in range(2):
        #pos resembles a random index to draw card from in deck
        pos = random.randint(0,len(deck1)-1)
        hand.append(deck1[pos])
    return hand


#create the deck
deck = deck()

#print 52 card deck
print(deck)

#Variable to count number of blackjacks in 5000 draws
probabilities = []

for j in range(10):
    blackjack_ct = 0
    #Simulation to repeat 5000 times
    for i in range(5000):
        hand = draw(deck)
    #Checks to see if first card is an ace and second is a royal or 10
        if (hand[0] == 11 and hand[1] == 10) or (hand[0] == 11 and hand[1] == 'J') or (hand[0] == 11 and hand[1] == 'Q') or (hand[0] == 11 and hand[1] == 'K'):
           blackjack_ct += 1
    #Checks to see if first card is a royal or 10 and second is an ace
        elif (hand[0] == 10 and hand[1] == 11) or (hand[0] == 'J' and hand[1] == 11) or (hand[0] == 'Q'  and hand[1] == 11) or (hand[0] == 'K'  and hand[1] == 11):
            blackjack_ct += 1
    #
    probabilities.append(blackjack_ct/5000)

#Prints out number of blackjacks in 5000 draws
print(sum(probabilities)/len(probabilities))



    



    




