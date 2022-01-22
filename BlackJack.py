import random

suits = ('\u2665', '\u2666', '\u2663', '\u2660')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
          '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

BUST = False
BLACKJACK = False



# DEFINING CARD CLASS

class Card:
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + self.suit


# DEFINING DECK CLASS

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle_deck(self):
        
        random.shuffle(self.all_cards)


# DEFINING PLAYER CLASS

class Player:
    
    def __init__(self, name, chips):
        
        self.player_cards = []
        self.name = name
        self.chips = chips
        self.bet = []
        self.sum_cards = []
        
            
    def __str__(self):
        
        return self.name + self.chips + self.player_cards + self.bet

    def give_bet(self):

        print('BET')
        amount = int(input())

        if self.chips - amount >= 0:
            print('Bet accepted')
            self.bet.append(amount)
            self.chips -= amount

        else:
            print('You dont have enough chips for that bet, try again')
            Player.give_bet(self)


    def hit_stand(self):

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
            Player.hit_stand(self)


    def check_cards(self):

        self.sum_cards = []
        for i in self.player_cards:
            if i.value == 11 and sum(self.sum_cards) + 11 > 21:
                i.value = 1
            elif 11 in self.sum_cards and sum(self.sum_cards) + i.value > 21:
                a = [1 if x==11 else x for x in self.sum_cards]
                self.sum_cards = a
            self.sum_cards.append(i.value)

                                                                                                      # - podela karata - prikaz - player move - comp move - win_lose

def check_status(sum_hand):

    global BUST
    global BACKJACK

    if sum_hand > 21:

        print('BUST')
        BUST = True
        return BUST

    elif sum_hand == 21:

        BLACKJACK = True
        print('BLACKJACK ! ! !')

    else:

        player_move()




def player_move():

    if len(Player1.player_cards) == 0:
        Player1.player_cards.append(new_deck.all_cards.pop())
        Player1.player_cards.append(new_deck.all_cards.pop())
    Player1.check_cards()
    if sum(Player1.sum_cards) == 21:
        print('BLACKJACK ! ! !')
        return
    table(Comp.player_cards, sum(Comp.sum_cards), sum(Player1.bet), Player1.player_cards, Player1.chips, sum(Player1.sum_cards))
    Player1.give_bet()
    Player1.check_cards()
    num = len(Player1.sum_cards)
    
    Player1.hit_stand()
    Player1.check_cards()
    if BLACKJACK == True:
        return
    if len(Player1.sum_cards) == num:
        return
    table(Comp.player_cards, sum(Comp.sum_cards), sum(Player1.bet), Player1.player_cards, Player1.chips, sum(Player1.sum_cards))
    check_status(sum(Player1.sum_cards))


def comp_move():

    print(input('Press enter to procced to next round:'))
    Comp.check_cards()
    table(Comp.player_cards, sum(Comp.sum_cards), sum(Player1.bet), Player1.player_cards, Player1.chips, sum(Player1.sum_cards))

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
        



def table(comp_cards, sum_comp, table_bet, player_cards, player_chips, sum_player):
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
  

    


def collect_cards():

    new_deck.all_cards = Player1.player_cards + Comp.player_cards + new_deck.all_cards
    Player1.player_cards = []
    Comp.player_cards = []


# MAIN

# Create Deck

new_deck = Deck()

# Shuffle Deck

new_deck.shuffle_deck()

# Create Player

#name = input('Pls enter your name: ')
Player1 = Player('Stefan', 1000)

# Create Computer

Comp = Player('Computer', 1000000)

# Game starts

while Player1.chips != 0:

    Comp.player_cards.append(new_deck.all_cards.pop())              # Dealing one card to computer for show
    Comp.check_cards()
    player_move()
    if BUST == True:
        BUST = False
        Player1.bet = []
        print(input('Press enter to procced'))
        collect_cards()
        continue
    Comp.player_cards.append(new_deck.all_cards.pop())
    BLACKJACK = False                                               # Dealing second card to computer
    comp_move()
    collect_cards()
    print('If you want to procced to next rount press ENTER or if you want to QUIT type in Q')
    quit = input()
    if quit == 'q':
        break
    else:
        pass

print('GAME OVER !')


