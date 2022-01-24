import random

suits = ('\u2665', '\u2666', '\u2663', '\u2660')                                   # Defining suits of cards
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')         # Defining ranks of cards
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,                  # Definig values of cards
          '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

BUST = False            # For BUST check
BLACKJACK = False       # For Blackjack check

class Card:
# Defining Card class
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + self.suit

class Deck:
# Defining Deck class
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle_deck(self):
    # Function for shuffling deck
        random.shuffle(self.all_cards)

class Player:
# Defining Player class
    def __init__(self, name, chips):
        
        self.player_cards = []
        self.name = name
        self.chips = chips
        self.bet = []
        self.sum_cards = []

    def __str__(self):
        
        return self.name + self.chips + self.player_cards + self.bet

    def give_bet(self):
    # Function for betting chips in game
        print('BET')
        amount =100 # int(input())

        if self.chips - amount >= 0:        # Checking if amount of bet is avaliable(if you have enough chips)
            print('Bet accepted')
            self.bet.append(amount)
            self.chips -= amount

        else:                                                     
            print('You dont have enough chips for that bet, try again')
            Player.give_bet(self)                                           # Using recursion if amount of bet is not valid

    def hit_stand(self):
    # Function for hit or stand
        print('HIT (H) or STAND (S)')
        h_s = input()
        
        if h_s == 'h':
            self.player_cards.append(new_deck.all_cards.pop())
        elif h_s == 's':
            pass
        else:
            print(' ')
            print('Invalid input, pls type H or S')
            print(' ')
            Player.hit_stand(self)                      # Using recursion if invalid input

    def check_cards(self):
    # Function for checkig values of cards(Aces)
        self.sum_cards = []
        for i in self.player_cards:
            if i.value == 11 and sum(self.sum_cards) + 11 > 21:
                i.value = 1
            elif 11 in self.sum_cards and sum(self.sum_cards) + i.value > 21:
                a = [1 if x==11 else x for x in self.sum_cards]
                self.sum_cards = a
            self.sum_cards.append(i.value)

def check_status(sum_hand):
# Function for checking if there was a BUST or BLACKJACK
    global BUST
    global BLACKJACK

    if sum_hand > 21:

        print('BUST')
        BUST = True
        return BUST

    elif sum_hand == 21:
        BLACKJACK = True
        print('BLACKJACK ! ! !')

    else:
        player_move()

def table(comp_cards, sum_comp, table_bet, player_cards, player_chips, sum_player):
# Function for visual show of Blackjack table
    print('\n')
    print('\n')
    for card in comp_cards:
        print(card)
    print(str(sum_comp))
    print('\n')
    print('\t' + str(table_bet) + ' ')
    print('\n')
    for card in player_cards:
        print(card)
    print(str(sum_player) + '\t\t' + str(player_chips) + '    ')
    print('\n')
    print('\n')
    print('\n')
    print('\n')


def player_move():
# In this and next function is whole game logic
    if len(Player1.player_cards) == 0:                          # On start of new hand, dealing two cards to player
        Player1.player_cards.append(new_deck.all_cards.pop())
        Player1.player_cards.append(new_deck.all_cards.pop())
    Player1.check_cards()                                       # Checking values for Aces

    if sum(Player1.sum_cards) == 21:                            # Checking if player got Blackjack on first two cards
        print('BLACKJACK ! ! !')
        return

    # Display Table with table function
    table(Comp.player_cards, sum(Comp.sum_cards), sum(Player1.bet), Player1.player_cards, Player1.chips, sum(Player1.sum_cards))
    Player1.give_bet()                  # Give bet
    Player1.check_cards()               # Checking values of cards (Aces)
    num = len(Player1.sum_cards)        # Getting number of cards in players hand
    Player1.hit_stand()                 # Hit/Stand
    Player1.check_cards()               # If Player Hit, again checking values of cards(Aces)

    if BLACKJACK == True:               # If Blackjack, finish move
        return

    if len(Player1.sum_cards) == num:   # Checking if Player Stand
        return

    table(Comp.player_cards, sum(Comp.sum_cards), sum(Player1.bet), Player1.player_cards, Player1.chips, sum(Player1.sum_cards))
    check_status(sum(Player1.sum_cards))    # This function checks player hand and if player Hit, calling Player move func again


def comp_move():
# In this function is other part of game logic(Computer move logic)
    print(input('Press enter to procced to next round:'))
    Comp.check_cards()
    table(Comp.player_cards, sum(Comp.sum_cards), sum(Player1.bet), Player1.player_cards, Player1.chips, sum(Player1.sum_cards))

    # Computer always take card until it has more value of cards than Player or it Busts or in case 
    # Player had Blackjack, goes until Bust or Draw
    if sum(Player1.sum_cards) >= sum(Comp.sum_cards) and sum(Player1.sum_cards) != 21:
        Comp.player_cards.append(new_deck.all_cards.pop())
        print(input('Press enter to procced:'))
        comp_move()

    elif sum(Comp.sum_cards) > sum(Player1.sum_cards) and sum(Comp.sum_cards) <= 21:
        Player1.bet = []
        print('YOU LOSE')
        print(input('Press enter to procced to next round:'))


    elif sum(Player1.sum_cards) == 21 and sum(Player1.sum_cards) > sum(Comp.sum_cards):
        Comp.player_cards.append(new_deck.all_cards.pop())
        print(input('Press enter to procced:'))
        comp_move()
        

    elif sum(Comp.sum_cards) == 21 and sum(Player1.sum_cards) == 21:
        Player1.chips += Player1.bet[0]
        Player1.bet = []
        print('DRAW')
        print(input('Press enter to procced to next round:'))
        

    elif sum(Comp.sum_cards) > 21:
        num = sum(Player1.bet) * 2
        Player1.chips += sum(Player1.bet) * 2
        Player1.bet = []
        print('YOU WON ' + str(num) + ' CHIPS !')
        print(input('Press enter to procced to next round:'))
        
def collect_cards():
# Thus function is used when round is finished to collect all cards from Player and Computer back in deck
    new_deck.all_cards = Player1.player_cards + Comp.player_cards + new_deck.all_cards
    Player1.player_cards = []
    Comp.player_cards = []

# MAIN

# Create Deck
new_deck = Deck()

# Shuffle Deck
new_deck.shuffle_deck()

# Create Player using Player Class
name = input('Pls enter your name: ')
Player1 = Player(name, 1000)

# Create Computer using Player Class
Comp = Player('Computer', 1000000)

# Game starts
while Player1.chips != 0:

    Comp.player_cards.append(new_deck.all_cards.pop())              # Dealing one card to computer for display
    Comp.check_cards()
    player_move()
    if BUST == True:                # When Player move finished checking if there was BUST
        BUST = False                # Returning BUST bool to False
        Player1.bet = []            # Clearing Player Bet
        print(input('Press enter to procced'))
        collect_cards()             # Collecting all cards back to Deck
        continue
    Comp.player_cards.append(new_deck.all_cards.pop())           # Dealing second card to computer
    BLACKJACK = False                                              
    comp_move()
    collect_cards()
    print('If you want to procced to next rount press ENTER or if you want to QUIT type in Q')
    quit = input()
    if quit == 'q':
        break
    else:
        pass

print('GAME OVER !')