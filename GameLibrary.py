# GameLibrary.py
    #  option1: Text for option 1
    #  option2: Text for option 2
    #  result1: Text outcome for choosing option 1
    #  result2: Text outcome for choosing option 2
    #  next_step1: Function to call if option 1 is chosen
    #  next_step2: Function to call if option 2 is chosen
#
def make_choice(option1, option2, result1, result2, next_step1=None, next_step2=None):
    print("You have two options:")
    print("1. " + option1)
    print("2. " + option2)

    choice = input("What will you choose? (1/2): ")

    if choice == "1":
        print(result1)
        if next_step1:
            next_step1()  
    elif choice == "2":
        print(result2)
        if next_step2:
            next_step2()  
    else:
        print("Invalid choice, try again.")
        make_choice(option1, option2, result1, result2, next_step1, next_step2)  
        


def introduction():
    print("Welcome to 'The Enchanted Forest'!")
    print("You stand at the edge of the Enchanted Forest.")
    print("Will you step into the forest or turn back?")

    make_choice(
        "Enter the forest", 
        "Turn back", 
        "You enter the mysterious forest.", 
        "You turn back and leave the adventure.",
        enter_forest, 
        turn_back
    )


def enter_forest():
    print("\nYou walk deeper into the forest. The trees surround you.")
    make_choice(
        "Follow the path", 
        "Turn back", 
        "You follow the overgrown path deeper into the forest.", 
        "You decide to turn back.",
        follow_the_path, 
        turn_back
    )


def follow_the_path():
    print("\nYou come across a fork in the road.")
    make_choice(
        "Take the left path", 
        "Take the right path", 
        "You take the left path.", 
        "You take the right path.",
        left_path, 
        right_path
    )


def left_path():
    print("\nYou encounter a wise hermit.")
    make_choice(
        "Accept the hermit's help", 
        "Refuse the hermit's help", 
        "The hermit gives you a magical amulet.", 
        "You refuse the hermit’s help and continue alone.",
        hermit_help, 
        hermit_refuse
    )


def hermit_help():
    make_choice(
        "Use the amulet to take the Heart", 
        "Refuse the Heart", 
        "You gain the Heart's power but lose your humanity. Ending: The Forest Guardian", 
        "You refuse the Heart and return to the village. Ending: The Cursed Wanderer"
    )


def hermit_refuse():
    make_choice(
        "Take the Heart", 
        "Destroy the Heart", 
        "You become a feared ruler in the land. Ending: The Tyrant", 
        "You destroy the Heart and become a hero. Ending: The Forest’s Savior"
    )


def right_path():
    print("\nYou find a group of trapped forest creatures.")
    make_choice(
        "Help the creatures", 
        "Ignore the creatures", 
        "You free the creatures and they guide you.", 
        "You ignore their pleas and continue on your way. Ending: The Haunted One.",
        help_creatures
    )


def help_creatures():
    make_choice(
        "Take the Heart", 
        "Leave the Heart", 
        "The creatures warn you, but you take the Heart anyway. Ending: The Forest's Doom", 
        "You leave the Heart and the creatures guide you out. Ending: Friend of the Forest"
    )


def turn_back():
    print("\nYou turn back, but you hear a mysterious voice.")
    make_choice(
        "Ignore the voice", 
        "Follow the voice", 
        "You leave safely but always wonder what could have been. Ending: The Missed Adventure", 
        "You follow the voice into the forest.",
        None, 
        follow_the_voice
    )


def follow_the_voice():
    print("\nYou find a mysterious figure in the forest.")
    make_choice(
        "Trust the figure", 
        "Distrust the figure", 
        "The figure reveals itself as a forest spirit.", 
        "You suspect the figure is deceiving you.",
        trust_the_figure, 
        distrust_the_figure
    )


def trust_the_figure():
    make_choice(
        "Accept the spirit's guidance", 
        "Reject the spirit's offer", 
        "You use the Heart’s power for good. Ending: The Benevolent Ruler", 
        "The Heart overwhelms you. Ending: The Fallen Hero"
    )


def distrust_the_figure():
    make_choice(
        "Confront the figure", 
        "Flee", 
        "You defeat the trickster and break the curse. Ending: The Forest’s Liberator", 
        "You escape but are haunted by the encounter. Ending: The Paranoid Survivor"
    )
