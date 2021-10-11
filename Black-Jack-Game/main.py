import random
import art as a
import clear as c


cards = [11,1,2,3,4,5,6,7,8,9,10.0,10.1,10.2]
card_art = [a.card_art[11],a.card_art[1],a.card_art[2],a.card_art[3],a.card_art[4],a.card_art[5],a.card_art[6],a.card_art[7],a.card_art[8],a.card_art[9],a.card_art[10.0],a.card_art[10.1],a.card_art[10.2]]


player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0
Ace = False

def new_game():
    c.clear()
    global player_cards, dealer_cards, player_score, dealer_score, Ace

    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    Ace = False
    blackjack()

def who_won(player_total,dealer_total):
    global Ace

    if player_total == 21:
        print(a.black_jack)
        print(a.win)
    elif player_total > 21:
        if Ace:
            player_total -= 10
            Ace = False
            who_won(player_total,dealer_score)

    elif dealer_total > 21:
        print(a.win)
    elif player_total > dealer_total:
        print(a.win)
    elif player_total < dealer_total:
        print(a.loose)
    else:
        print(a.draw)

def hit():
    c.clear()
    global player_score, Ace

    random_card = random.choice(cards)
    if random_card == 11:
        Ace = True
    player_cards.append(random_card)
    player_score += random_card

    if Ace:
        if player_score > 21:
            player_score -= 10
            Ace = False      
    print(f"Your cards.")
    for i in range(len(player_cards)):
        print(a.card_art[player_cards[i]])

    print(f"Your score {int(player_score)}")

    if Ace:
        if player_score > 21:
            player_score -= 10
            Ace = False

    while player_score < 21:
        player_choice = input("Hit(h) or Stand(s) : ")

        if player_choice == 'h':
            hit()
        else:
            stand()
    
    if player_score == 21:
        print(a.black_jack)
        print(a.win)
    else:
        print(a.loose)

    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again == 'y':
        new_game()
    else:
        print(a.game_over)
        return 

def stand():
    c.clear()
    global dealer_score,Ace

    print(f"\nPlayer cards:\n")
    for i in range(len(player_cards)):
        print(a.card_art[player_cards[i]])

    print(f"Your final score: {int(player_score)}")
    if player_score == 21:
        print(a.black_jack)
        print(a.win)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            new_game()
        else:
            print(a.game_over)
            return 
    
    while dealer_score < 17:
        random_card = random.choice(cards)
        dealer_cards.append(random_card)
        dealer_score += random_card

    print(f"Dealer Cards:\n")

    for j in range(len(dealer_cards)):  
        print(a.card_art[dealer_cards[j]])

    print(f"Dealer final score: {int(dealer_score)}\n")
            
    who_won(int(player_score),int(dealer_score))

    print("\n")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again == 'y':
        new_game()
    else:
        print(a.game_over)
        return 

def blackjack():
    global player_cards, dealer_cards, player_score, dealer_score, Ace   
    print(a.logo)
    for i in range(2):
        random_card = random.choice(cards)
        if random_card == 11:
            Ace = True
        player_cards.append(random_card)
        player_score += int(player_cards[i])
        dealer_cards.append(random_card)
        dealer_score += int(dealer_cards[i])

   

    print(f"Your cards")
    print(f"{a.card_art[player_cards[0]]} {a.card_art[player_cards[1]]}")
    if Ace:
        if player_score > 21:
            player_score -= 10
            Ace = False
    print(f"Your current score = {player_score}")

    if player_score == 21:
        print(a.black_jack)
        print(a.win)
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            new_game()
        else:
            print(a.game_over)
            return 

    elif dealer_score == 21:
        print(f"{a.dealers_blackjack}\n{a.loose}")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            new_game()
        else:
            print(a.game_over)
            return 

    print(f"Computer first card \n{a.card_art[dealer_cards[0]]}")

    player_choice = input("Hit(h) or Stand(s) : ")

    if player_choice == 'h':
        hit()
    else:
        stand()


blackjack()