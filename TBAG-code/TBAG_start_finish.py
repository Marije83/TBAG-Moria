from TBAG_Classes import *  

# informs user they have lost the game and gives option to play again, making sure the user inputs a valid answer.
def game_over():
    game_over = Question("game_over")
    game_over.set_text("""\nYou have lost the game and did not manage to cross the mines of Moria!
    \nWould you like to play again! \n Please enter y for 'yes' or n for 'no'\n""")
    game_over.print_text()
    while game_over.validity == False:
        game_over.set_answer()
        game_over.validity = game_over.check_answer_validity(["y", "yes", "n", "no"])
        if game_over.validity == False:
            print("\nInvalid answer, please enter one of the following characters: y for 'yes' or n for 'no'\n")
        else:
            if "y" in game_over.answer:
                start_game()
            elif "n" in game_over.answer:
                print("\n Thank you for playing. Come back soon! \n")
                exit ()
            
        
def start_game():
    start = Scene("start")
    start.set_opener("""\nThis adventure follows Frodo and the rest of the fellowship through the mines of Moria.
They have just been defeated by the mountain Caradhras and have decided to cross the Mines of Moria 
in order to reach Lothlorien. They reach a strip of dry land between a lake and the cliffs of the 
mountains that house Moria. Close under the cliff there stand, still strong and living, two tall trees.
'Well, here we are at last' says Gandalf.\n""")
    start.print_opener()
    start.continue_enter()
