import random
import collections
import load

class Deck:
    '''For testing, a computer Judge'''
    def __init__(self, apples):
        self.apples = apples 

    def deal_next(self):
        # Deal out the next card of the deck to a player
        pass 

    def select_winner(self):
        # Select the winning card
        pass


class RandomDeck(Deck):
    '''For testing, a computer Judge, randomly selects a winner'''
    def __init__(self, apples):
        Deck.__init__(self, apples)

    def select_winner(self):
        # Randomly pick a winner
        r = random.randint(0, len(self.apples))
        return apples[r]


class Apple:
    '''An apple'''
    def __init__(self, name, flavor_text, red=True):
        self.name = name
        self.flavor_text = flavor_text
        self.red = red

    def name(self):
        # Return the name of this card
        return self.name

    def type(self):
        # Is the type Red
        return self.type

    def render(self):
        # Render this apple in the window 
        pass

    def __str__(self):
        # Name : Flavor Text
        return self.name + ": " + self.flavor_text


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number #turn number


    def deal_hand(self, cards):

        # assert cards length = 7?
        self.cards = cards
    
    def play_card(self, card):
        # Plays card during this turn, assumes card in hand, returns card

        self.cards.remove(card)
        return self.card

    def select_winner(self, card):
        # Select this card as the winner of this round 

    def name(self):
        # Return this player's name
        return self.name

    def number(self):
        # Get this player's turn number
        return self.number 


class Game:

    def __init__(self):
        self.green_deck, self.red_deck = load_decks(self)


    def start(self, players):
        # Confirm players

        # Give each of the players 7 red cards
        for player in self.players:
            player_hand = []
            player_hand.append(self.red_deck.pop())

        # Number the players

        # Create a score counter for each player

        self.counter = collections.Counter() # finish this

        self.play()


    def load_decks(self, red_file, green_file):

        green_cards = load.loadCards(green_file)
        red_cards = load.loadCards(red_file)

        # Load the decks from their respective files

        green_deck = []
        red_deck = []

        for g in green_cards:
            green_deck.append(Apple(g, None, red=False))

        for r in red_cards:
            red_deck.append(Apple(r, None))

        return green_deck, red_deck

    def update_player_score(self, player):




    def play_round(self, judge):
        # Play a single round of this game 

        # Put down a green card
        card = self.green_deck.pop()
        card.render()

        # Wait for all players' cards be put in 


        # Once they are all put in, turn them over


        # Wait for player to select the winner 
        winning_word = input("Which word is the winner? ")


        # Update winner's score
        

    def play(self):
        # Play until there are no green cards
        turn = 0

        while len(self.green_deck > 0):
            # Put down the green card, start with player number 1
            judge_number = turn % len(self.players)
            judge = players[judge_number]
            self.play_round(judge)
            turn += 1

        print("Game over!")
        winner = counter.max # whatever this function is 
        print("The winner of this game is: " + winner.name())





