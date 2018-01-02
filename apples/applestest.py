import load
import random

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
    def __init__(self, name):
        self.name = name

    def deal_hand(self, cards):
        self.cards = cards

    def give_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def get_hand(self):
        return self.cards

    def get_name(self):
        return self.name

class ApplesToApples:
    def __init__(self):
        green_cards = load.loadCards('GAPPLE')
        red_cards = load.loadCards('RAPPLE')
        self.green_deck = []
        self.red_deck = []

        for g in green_cards:
            self.green_deck.append(Apple(g, None, red=False))

        for r in red_cards:
            self.red_deck.append(Apple(r, None))

        self.play_game()


    def start(self):
        print("Apples To Apples") #render begin screen
        self.players = input("Give player names, separated by comma: ").strip().split(',') #initialize players
        self.num_players = len(self.players)
        self.scores = collections.Counter()

        for player in self.players: #deal hands
            hand = []
            for i in range(0, 7):
                hand.append(self.red_deck.pop(random.randint(0,len(self.red_deck)-1)))
            player.deal_hand(hand)

    def play_game(self):
        self.start()
        while len(self.green_deck > 0):
            judge = self.players[random.randint(0,num_players-1)]
            play_round(self, judge)

        print("Game over! Your score is " + str(score))


    def win_round(self, judge):
        winner = input("Select a winner: ")
        
        #
        win = random.randint(0, self.num_players-1)
        print("Player " + str(win) +" you win this round! your score is " + str(score))
        print("")
        print("--------------------------------")

    def play_round(self, judge):
        round_players = self.players[:]
        round_players.remove(judge) 

        for player in round_players: 
            print("Player " + str(j) + " here are your cards: " + str(hands[j])) #render each player's cards

        green_card = self.green_deck.pop() 
        print("The green apple is: " + green_card) #render green card

        for player in round_players:
            submission = input("Player " + str(j) + " Submit a card: ") #wait for every player to submit a card
            while submission not in player.get_hand(): #we don't need this with the GUI
                print("This word is not in your hand")
            player.remove_card(submission)

        self.win_round(judge)

        for player in round_players: #give each player a new card
            new_card = self.red_deck.pop()
            player.give_card(new_card)
            print("Player " + player.name() + " here is your new card: " + new_card)


a = ApplesToApples()

