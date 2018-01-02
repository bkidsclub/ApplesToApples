import load
import random
import collections

class Apple:
    '''An apple'''
    def __init__(self, name, flavor_text, red=True):
        self.name = name
        self.flavor_text = flavor_text
        self.red = red

    def get_name(self):
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
        for c in self.cards:
            if c.get_name() == card:
                self.cards.remove(c)

        #self.cards.remove(card)

    def play_card(self, card):
        self.played = card

    def get_played_card(self):
        return self.played

    def get_hand(self):
        return self.cards

    def render_hand(self):
        string_hand = []
        for c in self.cards:
            string_hand.append(c.get_name().replace(" ", ""))
        return string_hand

    def get_name(self):
        return self.name

class ApplesToApples:
    def __init__(self):
        green_cards = load.loadCards('GAPPLE')
        red_cards = load.loadCards('RAPPLE')
        self.green_deck = []
        self.red_deck = []

        for g in green_cards:
            self.green_deck.append(Apple(g, "", red=False))

        for r in red_cards:
            self.red_deck.append(Apple(r, ""))

        self.play_game()


    def start(self):
        print("Apples To Apples") #render begin screen
        players = input("Give player names, separated by comma: ").replace(" ", "").split(',') #initialize players
        self.players = []
        for p in players:
            self.players.append(Player(p))

        self.num_players = len(self.players)
        self.scores = collections.Counter()

        for player in self.players: #deal hands
            hand = []
            for i in range(0, 7):
                hand.append(self.red_deck.pop(random.randint(0,len(self.red_deck)-1)))
            player.deal_hand(hand)

    def play_game(self):
        self.start()
        while len(self.green_deck) > 0:
            judge = self.players[random.randint(0, self.num_players-1)]
            print("--------------------------")
            print("The judge for this round is: " + judge.get_name())
            self.play_round(judge)

        print("Game over! Your score is " + str(score))


    def win_round(self, judge, submitted):
        print(judge.get_name() + ", the submitted cards are: " + str(submitted))
        winner = input("Select a winner: ")
        while winner not in submitted:
            print("That is not one of the submitted cards")
            winner = input("Select a winner: ")

        print("The winning card is :" + winner)
        return winner


        #
        #win = random.randint(0, self.num_players-1)
        #print("Player " + str(win) +" you win this round! your score is " + str(score))
        #print("")
        #print("--------------------------------")

    def play_round(self, judge):
        round_players = self.players[:]
        round_players.remove(judge) 

        green_card = self.green_deck.pop() 
        print("The green apple is: " + str(green_card)) #render green card

        submitted = []
        for player in round_players:
            print("Player " + player.get_name() + " here are your cards: " + str(player.render_hand()))
            submission = input("Player " + player.get_name() + " Submit a card: ") #wait for every player to submit a card
            while submission not in player.render_hand(): #we don't need this with the GUI
                print("This word is not in your hand")
                submission = input("Player " + player.get_name() + " Submit a card: ")
            player.remove_card(submission)
            player.play_card(submission)
            submitted.append(submission)

        winner = self.win_round(judge, submitted)
        for player in round_players:
            if player.get_played_card() == winner:
                print("Congratulations Player " + player.get_name() + ", you win this round!")
                break


        for player in round_players: #give each player a new card
            new_card = self.red_deck.pop()
            player.give_card(new_card)
            print("Player " + player.get_name() + " here is your new card: " + str(new_card))



a = ApplesToApples()

