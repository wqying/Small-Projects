import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []
game_number = 2
computer_plays = True
# There is no need to define a bunch of global-scale variables at the very top!
# A better way to handle this is to create a "gameflow" function with all these variables inside
# I actually already have the "gameflow" function - "sequence"


def card_picker(num_of_cards, whose_cards):
    """
    Indexes randomly from the cards list to simulate drawing cards
    :param num_of_cards: how many cards the player or computer should draw
    :param whose_cards: the player or the computer
    :return: a list of the cards the player or computer is holding
    """
    if whose_cards is player_cards:
        for i in range(num_of_cards):
            random_num = random.randint(0, 12)  # both 0 and 12 are included
            player_cards.append(cards[random_num])
        return player_cards
    elif whose_cards is computer_cards:
        if computer_plays:
            random_num = random.randint(0, 12)  # both 0 and 12 are included
            computer_cards.append(cards[random_num])
        return computer_cards


def scores(whose_score):
    """
    Calculates the total score of the player or computer from their respective list of cards
    :param whose_score: the player or computer
    :return: an integer representing the summed values of the cards they're holding
    """
    total_score = sum(whose_score)
    return total_score


def win_or_lose(player_final_score, computer_final_score):
    """
    Determines if the player wins or loses
    :param player_final_score: the final score of the player
    :param computer_final_score: the final score of the computer
    :return: nothing. Prints a bunch of statements instead
    """
    if player_final_score == 21:
        print("You win! You get BlackJack.")
    elif computer_final_score == 17 and player_final_score != 21:
        print("You lose xP. Computer gets BlackJack.")
    elif player_final_score > 21:
        print("You lose xP. You busted.")
    elif computer_final_score > 17:
        print("You win! Computer busted.")
    elif player_final_score == computer_final_score:
        print("Draw.")


def game_flow():
    """
    Determines the sequence of game logic.
    :return: nothing.
    """
    player_busted = False
    global computer_plays
    global game_number
    while not player_busted:
        print(f"Your cards: {card_picker(game_number, whose_cards=player_cards)}, current score: {scores(player_cards)}")
        print(f"Computer's first card: {card_picker(1, whose_cards=computer_cards)[0]}")
        if scores(player_cards) > 21:
            win_or_lose(scores(player_cards), scores(computer_cards))
            break
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        computer_plays = False
        game_number = 1
        if another_card == "n":
            computer_plays = True
            while scores(computer_cards) < 17:
                card_picker(1, computer_cards)
            print(f"Your final hand: {card_picker(0, whose_cards=player_cards)}, current score: {scores(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {scores(computer_cards)}")
            win_or_lose(scores(player_cards), scores(computer_cards))
            break


# This while loop asks if player wants to play the game. Exits the program if the answer is no.
while True:
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if play == "y":
        player_cards = []
        computer_cards = []
        game_number = 2
        computer_plays = True
        game_flow()
    elif play == "n":
        print("Goodbye~")
        break
