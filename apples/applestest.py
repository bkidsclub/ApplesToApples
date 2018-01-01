#import load
import random

print("small apples to apples")
players = input("Give player names, separated by comma: ").strip().split(',')
num_players = len(players)
#load.loadCards('file.txt')
green_deck = ['Spicy', 'Aromatic', 'Amazing']
red_deck = ['cow', 'dog', 'cat', 'fly', 'spice', 'word', 'creeper', 'minecraft', 'crepe', 
'Abraham Lincoln', 'cow', 'dog', 'cat', 'fly', 'spice', 'word', 'creeper', 'minecraft', 'crepe', 'Abraham Lincoln',
'cow', 'dog', 'cat', 'fly', 'spice', 'word', 'creeper', 'minecraft', 'crepe', 'Abraham Lincoln']

hands = []
for j in range(num_players):
    hand = []
    for i in range(0, 7):
        hand.append(red_deck.pop(random.randint(0,len(red_deck))))
    hands.append(hand)


score = 0
while len(green_deck) > 0:
    green_card = green_deck.pop()
    for j in range(num_players):
        print("Player " + str(j) + " here are your cards: " + str(hands[j]))
    print("The green apple is: " + green_card)

    for j in range(num_players):
        sub = input("Player " + str(j) + " Submit a card: ")
        while sub not in hands[j]:
            print("This word is not in your hand")
            sub = input("Submit a card: ")
        hands[j].remove(sub)
    score += 1

    win = random.randint(0, num_players-1)
    print("Player " + str(win) +" you win this round! your score is " + str(score))
    print("")
    print("--------------------------------")

    for j in range(num_players):

        new_card = red_deck.pop()
        hands[j].append(new_card)
        print("Player " + str(j) + " here is your new card: " + new_card)
print("Game over! Your score is " + str(score))