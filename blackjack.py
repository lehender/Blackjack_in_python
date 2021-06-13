import random
from time import sleep


def main():
    global deck_count, dollars, dealerhand, playerhand
    num_decks = 4
    dollars = 500
    InGame = True
    print("Welcome! Ready for some blackjack?")

    while dollars > 0:
        print("\n$$  BLACKJACK  $$ ~ - Programe buy Levi H.")
        print("Total $" + str(dollars))
        while True:
            gO = input("\nDeal? y/n: ")
            if gO.lower() == 'y':
                # i think to keep each variable clean
                deck_count = {" A ": num_decks, " K ": num_decks, " Q ": num_decks, " J ": num_decks, "1 0": num_decks, " 9 ": num_decks, " 8 ": num_decks, " 7 ": num_decks, " 6 ": num_decks, " 5 ": num_decks, " 4 ": num_decks, " 3 ": num_decks, " 2 ": num_decks}
                total = 0
                dealerhand = []
                dealertotal = 0
                playerhand = []
                playertotal = 0

                stay = 0
                sleep(.5)

                for num in range(2): #need this to repeat for amount of cards, not a set number
                    dealerhand.append(deal_cards()) #set up the cards for the dealer
                for num in dealerhand:
                    dealertotal = dealertotal + get_card_value(num, dealertotal)

               # print("\nDEBUG",str(dealertotal),dealerhand)
                dealer_display(dealerhand, stay) #dealer display

                for num in range(2): #need this to repeat for amount of cards, not a set number
                    playerhand.append(deal_cards()) #for the player
                for num in playerhand:
                    playertotal = playertotal + get_card_value(num, playertotal)
                sleep(.5)
                display_cards(playerhand)

                while InGame:
                    print("Total:", playertotal)
                    wLC = 0
                    status = win_lose_continue(playertotal, wLC, stay)

                    if status == 'win':
                        stay = 1
                        results_print()
                        dealer_display(dealerhand, stay)
                        sleep(.5)
                        display_cards(playerhand)
                        sleep(.5)
                        dollars = dollars + 25
                        break
                    elif status == 'lose':
                        stay = 1
                        results_print()
                        dealer_display(dealerhand, stay)
                        sleep(.5)
                        display_cards(playerhand)
                        sleep(.5)
                        dollars = dollars - 25
                        break
                    wLC = 1
                    status = win_lose_continue(dealertotal, wLC, stay)
                    if status == 'win':
                        stay = 1
                        results_print()
                        dealer_display(dealerhand, stay)
                        sleep(.5)
                        display_cards(playerhand)
                        sleep(.5)
                        dollars = dollars - 25
                        break
                    elif status == 'lose':
                        stay = 1
                        results_print()
                        dealer_display(dealerhand, stay)
                        sleep(.5)
                        display_cards(playerhand)
                        sleep(.5)
                        dollars = dollars + 25
                        break

                    player_choice = playchoice()

                    if player_choice == 'hit':
                        playerhand = hit(playerhand)
                    elif player_choice == 'stay':
                        stay = 1

                    playertotal = 0
                    for num in playerhand:
                        playertotal = playertotal + get_card_value(num, playertotal)

                    dealer_choice = dealerlogic(dealertotal)
                    if dealer_choice == 'hit':
                        stay = 0
                        dealerhand = hit(dealerhand)
                    elif dealer_choice == 'stay':
                        if stay == 1:
                            print("Both stay. Let's see who wins!")
                            sleep(1)
                            results_print()
                            sleep(2)
                            print("The dealer...")
                            dealer_display(dealerhand, stay)
                            sleep(1)
                            print("AND THE PLAYER!")
                            display_cards(playerhand)
                            sleep(1)
                            print("Dealer total:", dealertotal)
                            sleep(1)
                            print("Player total:", playertotal)
                            sleep(1)
                            if playertotal > dealertotal:
                                print("Player wins!\n")
                                for num in range(3):
                                    print("Player wins 25 dollars!")
                                    sleep(.5)
                                dollars = dollars + 25
                                sleep(1)
                                break
                            else:
                                print("Dealer wins :(\n")
                                for num in range(3):
                                    print("\nYou Lose 25 dollars!")
                                    sleep(.5)
                                dollars = dollars - 25
                                sleep(1)
                                break
                    dealertotal = 0
                    for num in dealerhand:
                        dealertotal = dealertotal + get_card_value(num, dealertotal)
                    dealer_display(dealerhand, stay)
                    sleep(.5)
                    display_cards(playerhand)
            elif gO.lower() == 'n':
                print("Thank you so much for to be you to be playing my game. Bye!")
                sleep(3)
                exit()
            else:
                print("Please enter y or n")

def deal_cards():
    choosing_card = True #loop primer
    deck = [' A ', ' K ', ' Q ', ' J ', '1 0', ' 9 ', ' 8 ', ' 7 ', ' 6 ', ' 5 ', ' 4 ', ' 3 ', ' 2 '] #str values in list

    while choosing_card:
        num = random.randint(0,12) #pick a random number correlating with # in list
        card = deck[num] #assign card 1 a str in the list
        choosing_card = num_of_card(card) #this checks if all 4 cards have been removed using num_of_card func

    return card

def dealer_display(cards, stay):
    print("-DEALER-------------->-")
    for num in range(len(cards) - 1):
        print(" ___ ", end="")
    print(" ___ ")
    if stay == 1:
        for num in range(len(cards) - 1):
            if num == 1:
                print("|"+str(cards[num])+"|", end="")
            else:
                print("|"+str(cards[num])+"|", end="")
        if len(cards) <= 2:
            print("|"+str(cards[-1])+"|")
        else:
            print("|"+str(cards[-1])+"|")
    else:
        for num in range(len(cards) - 1):
            if num == 1:
                print("|???|", end="")
            else:
                print("|"+str(cards[num])+"|", end="")
        if len(cards) <= 2:
            print("|???|")
        else:
            print("|"+str(cards[-1])+"|")

    for num in range(len(cards) - 1):
        print("|   |", end="")
    print("|   |")

    for num in range(len(cards) - 1):
        print(" --- ", end="")
    print(" --- ")
    print("-<--------------DEALER-")

def num_of_card(card):
    if deck_count[card] == 0: #if no cards in dict of card values is left, returns true to pick another card from choosing card
        return True
    else: #else means there are cards left. 1 number is removed from the dictionary of total cards and false is returned to move to next card or return both loc var cards
        deck_count[card] -= 1
        return False

def display_cards(cards):
    print("-PLAYER--------------\-")
    for num in range(len(cards) - 1):
        print(" ___ ", end="")
    print(" ___ ")

    for num in range(len(cards) - 1):
        print("|"+str(cards[num])+"|", end="")
    print("|"+str(cards[-1])+"|")

    for num in range(len(cards) - 1):
        print("|   |", end="")
    print("|   |")

    for num in range(len(cards) - 1):
        print(" --- ", end="")
    print(" --- ")
    print("-/--------------PLAYER-")

def get_card_value(card, total):
    if card in [' K ',' Q ',' J ','1 0']:
        cardvalue = 10
    elif card == ' A ':
        if total + 11 > 21:
            cardvalue = 1
        else:
            cardvalue = 11
    else:
        cardvalue = int(card)
    return cardvalue

def win_lose_continue(total, dealorplay, stay):
    if dealorplay == 0:
        if total > 21:
            for num in range(3):
                print("\nYou Lose 25 dollars!")
                sleep(.5)
            sleep(2)
            return 'lose'

        if total == 21:
            for num in range(3):
                print("21 you win 25 dollars!")
                sleep(.5)
            sleep(2)
            return 'win'
        if total < 21:
            return
    else:
        if total > 21:
            for num in range(3):
                print("Dealer busts! You win 25 dollars!")
                sleep(.5)
            sleep(2)
            return 'lose'

        if total == 21 and stay == 1:
            for num in range(3):
                print("21 Dealer Wins! You lose 25 dollars!")
                sleep(.5)
            sleep(2)
            return 'win'
        if total < 21:
            return

def playchoice():
    while True:
        choice = input("Player, Hit or Stay?: ")
        if choice.lower() == 'hit':
            print('Hit')
            return 'hit'
        elif choice.lower() == 'stay':
            print("Stay")
            return 'stay'
        else:
            print("ERROR: Please Hit or Stay!")
            sleep(1)

def hit(hand):
    hand.append(deal_cards())
    return hand

def dealerlogic(hand):
    print("Dealer, Hit or Stay?: ")
    sleep(1)
    if hand < 16:
        print("Hit")
        sleep(1)
        return 'hit'
    else:
        print("Stay")
        sleep(1)
        return 'stay'

def results_print():
    import random
    chv = random.randint(1, 9)

    if chv == 1:
        print(".------..------..------..------..------..------..------.")
        print("|R.--. ||E.--. ||S.--. ||U.--. ||L.--. ||T.--. ||S.--. |")
        print("| :(): || (\/) || :/\: || (\/) || :/\: || :/\: || :/\: |")
        print("| ()() || :\/: || :\/: || :\/: || (__) || (__) || :\/: |")
        print("| '--'R|| '--'E|| '--'S|| '--'U|| '--'L|| '--'T|| '--'S|")
        print("`------'`------'`------'`------'`------'`------'`------'")
    elif chv == 2:
        print(""" /$$$$$$$                                /$$   /$$             
    | $$__  $$                              | $$  | $$             
    | $$  \ $$  /$$$$$$   /$$$$$$$ /$$   /$$| $$ /$$$$$$   /$$$$$$$
    | $$$$$$$/ /$$__  $$ /$$_____/| $$  | $$| $$|_  $$_/  /$$_____/
    | $$__  $$| $$$$$$$$|  $$$$$$ | $$  | $$| $$  | $$   |  $$$$$$ 
    | $$  \ $$| $$_____/ \____  $$| $$  | $$| $$  | $$ /$$\____  $$
    | $$  | $$|  $$$$$$$ /$$$$$$$/|  $$$$$$/| $$  |  $$$$//$$$$$$$/
    |__/  |__/ \_______/|_______/  \______/ |__/   \___/ |_______/ """)

    elif chv == 3:
        print(""".-..-.   .-..--. .-..-. .-.   .-. .-.     .-..-..-. .-..-. 
    | | ~.-. | | ~~  | | ~  | |   | | | |      ~ | | ~  | | ~  
    | |.-.~  | | _    \|    | |   | | | |        | |     \|    
    | | ~.-. | |`-'     |\  | |   | | | |        | |       |\  
    | |  | | | | __   _ | | | | _ | | | | __     | |     _ | | 
    `-'  `-' `-'`--' `-'`-' `-'`-'`-' `-'`--'    `-'    `-'`-' """)

    elif chv == 4:
        print("""
    __________                    .__   __          
    \______   \ ____   ________ __|  |_/  |_  ______
     |       _// __ \ /  ___/  |  \  |\   __\/  ___/
     |    |   \  ___/ \___ \|  |  /  |_|  |  \___ \ 
     |____|_  /\___  >____  >____/|____/__| /____  >
            \/     \/     \/                     \/ 
    """)

    elif chv == 5:
        print("""                                    
     _|_|_|                                  _|    _|                
     _|    _|    _|_|      _|_|_|  _|    _|  _|  _|_|_|_|    _|_|_|  
     _|_|_|    _|_|_|_|  _|_|      _|    _|  _|    _|      _|_|      
     _|    _|  _|            _|_|  _|    _|  _|    _|          _|_|  
     _|    _|    _|_|_|  _|_|_|      _|_|_|  _|      _|_|  _|_|_|    

        """)

    elif chv == 6:
        print("""                                                   
    ,------.                       ,--.  ,--.          
    |  .--. ' ,---.  ,---. ,--.,--.|  |,-'  '-. ,---.  
    |  '--'.'| .-. :(  .-' |  ||  ||  |'-.  .-'(  .-'  
    |  |\  \ \   --..-'  `)'  ''  '|  |  |  |  .-'  `) 
    `--' '--' `----'`----'  `----' `--'  `--'  `----'  
                                                       """)

    elif chv == 7:
        print("""
     ______     ______     ______     __  __     __         ______   ______    
    /\  == \   /\  ___\   /\  ___\   /\ \/\ \   /\ \       /\__  _\ /\  ___\   
    \ \  __<   \ \  __\   \ \___  \  \ \ \_\ \  \ \ \____  \/_/\ \/ \ \___  \  
     \ \_\ \_\  \ \_____\  \/\_____\  \ \_____\  \ \_____\    \ \_\  \/\_____\ 
      \/_/ /_/   \/_____/   \/_____/   \/_____/   \/_____/     \/_/   \/_____/ 
                                                                               """)

    elif chv == 8:
        print("""
    ██████╗ ███████╗███████╗██╗   ██╗██╗  ████████╗███████╗
    ██╔══██╗██╔════╝██╔════╝██║   ██║██║  ╚══██╔══╝██╔════╝
    ██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ███████╗
    ██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ╚════██║
    ██║  ██║███████╗███████║╚██████╔╝███████╗██║   ███████║
    ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚══════╝
                                                           """)

    elif chv == 9:
        print("""
    '########::'########::'######::'##::::'##:'##:::::::'########::'######::
     ##.... ##: ##.....::'##... ##: ##:::: ##: ##:::::::... ##..::'##... ##:
     ##:::: ##: ##::::::: ##:::..:: ##:::: ##: ##:::::::::: ##:::: ##:::..::
     ########:: ######:::. ######:: ##:::: ##: ##:::::::::: ##::::. ######::
     ##.. ##::: ##...:::::..... ##: ##:::: ##: ##:::::::::: ##:::::..... ##:
     ##::. ##:: ##:::::::'##::: ##: ##:::: ##: ##:::::::::: ##::::'##::: ##:
     ##:::. ##: ########:. ######::. #######:: ########:::: ##::::. ######::
    ..:::::..::........:::......::::.......:::........:::::..::::::......:::""")

if __name__ == "__main__":
    main()