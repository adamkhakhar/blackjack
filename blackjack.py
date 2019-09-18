import random
import os

#create full deck of cards
cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
]

#calculate hand value
def calc_hand(hand):
    sum = 0

    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']

    for card in non_aces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)
    
    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum


#shuffles cards
def shuffle_deck(deck):
    random.shuffle(deck)

#deal cards
def deal_cards():
    for _ in range(0, 2):
        player.append(cards.pop())
        dealer.append(cards.pop())
    
#clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#print hands
def print_hands(dscore, pscore, standing):
    if standing:
        print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dscore))
    else:
        print('Dealer Cards: [{}][?]'.format(dealer[0]))
    print('Your Cards: [{}] ({})'.format(']['.join(player), pscore))
    print('')

#determine outcome of match
def outcome(dscore, pscore):
    if dscore > 21:
        print('Dealer busted, you win!')
    elif pscore == dscore:
        print('Tie! Nobody wins or loses.')
    elif pscore > dscore:
        print('You beat the dealer, you win!')
    else:
        print('You lose')

#determine if player has blackjack
def blackjack(score, first_hand):
    return (first_hand and score == 21)
    
#shuffle deck and deal cards
def shuffle_deck_and_deal():
    shuffle_deck(cards)
    deal_cards()

def begin_game():
    #has the player stood?
    standing = False
    #is this the first hand?
    first_hand = True
    while True:  
        #clear screen
        clear_screen()

        #calculate scores
        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        #print hands
        print_hands(dealer_score, player_score, standing)

        #if standing, determine outcome
        if standing: 
            outcome(dealer_score, player_score)
            return True
        
        #determine if blackjack
        if blackjack(player_score, first_hand):
            print('Blackjack!')
            return True

        #set first_hand to false
        first_hand = False

        #check if player busted
        if player_score > 21:
            print('You busted!')
            return True

        #Ask for hit or stand
        print('What would you like to do?')
        print('  [1] Hit')
        print('  [2] Stand')
        choice = input("Your choice: ")

        #execute_hit_or_stay
        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())
            print('2 entered')


# play match
while True:
    #create empty dealer and player hand
    dealer = []
    player = []

    #shuffle deck and deal cards
    shuffle_deck_and_deal()

    #begin match
    begin_game()

    #detremine if user wants to play again
    print('--------------------------------')
    print('Do you want to play again?')
    print('[1]: Yes')
    print('[2]: No')
    response = input('Your response: ')
    if response == '2':
        break
