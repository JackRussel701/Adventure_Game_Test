import time
import random
villain = ["fairy", "pirate", "troll"]
weapons = []


def print_time(text):
    print(text)
    time.sleep(2)


monster = random.choice(villain)


def intro():
    print_time('Hello')
    print_time('You find yourself standing in an open field,')
    print_time('filled with grass and yellow wildflowers.')
    print_time('Rumor has it that a wicked ' + monster + ' is somewhere around here,')
    print_time('and has been terrifying the nearby village')
    print_time('You see a house and a cave.')
    print_time('In your hands you hold your blunt, rusty, ineffective dagger')


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for option in options:
            if option in response:
                return response


def game():
    choice = valid_input('Enter 1 to knock on the door of the house, enter 2 to look into the cave.', ['1', '2'])
    if choice == '1':
        print_time('You approach the door of the house')
        print_time('You are about to knock on the door, when the door opens and the ' + monster + ' steps out!')
        print_time('Yikes! This house belongs to the ' + monster + '!')
        print_time('The ' + monster + ' attacks you!')
        if 'Sword of Ogoroth' not in weapons:
            print_time('You feel totally unprepared for this, what with only your silly dagger....')
            fight_flight = valid_input('Would you like to fight (1) or run away (2)?', ['1', '2'])
            if fight_flight == '1':
                if 'Sword of Ogoroth' in weapons:
                    print_time('The mighty Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.')
                    print_time('But the ' + monster + ' takes one look at your weapon and runs away!')
                    print_time('You have rid the town of the '+ monster + ' and you are heralded as the victor!')
                else:
                    print_time('You do your best...\n but your silly dagger is no match for the ' + monster + ' !')
                    print_time('You have been defeated...!')
            elif fight_flight == '2':
                print_time('You run back into the field. Luckily, you are not followed.')
        else:
            print_time('The mighty Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.')
            print_time('But the ' + monster + ' takes one look at your weapon and runs away!')
            print_time('You have rid the town of the ' + monster + ' and you are heralded as the victor!')
    elif choice == '2':
        if 'Sword of Ogoroth' in weapons:
            print_time('You peer carefully into the cave.')
            print_time('You were here before and have taken all the useful stuff.')
            print_time('It is just an empty cave now.')
            print_time('You walk back into the field.')
        else:
            print_time('You peer carefully into the cave.')
            print_time('Your eye catches a glint of metal behind a rock.')
            print_time('Holy Moly! You have found the mythical Sword of Ogoroth!')
            print_time('You discard your silly dagger and take the sword  with you.')
            print_time('You walk back out to the field.')
            weapons.append('Sword of Ogoroth')


def full_game():
    intro()
    game()
    play_again()


def play_again():
    play = valid_input('Would you like to play again (y/n)?', ['y', 'n'])
    if play == 'n':
        print_time('Thanks for playing! See you next time!')
    elif play == 'y':
        print('Excellent! Restarting game....')
        full_game()


full_game()
