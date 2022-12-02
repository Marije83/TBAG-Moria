from random import randint

# begins the game
def start_game():
    print("""\nThis adventure follows Frodo and the rest of the fellowship through the mines of Moria.
They have just been defeated by the mountain Caradhras and have decided to cross the Mines of Moria 
in order to reach Lothlorien. They reach a strip of dry land between a lake and the cliffs of the 
mountains that house Moria. Close under the cliff there stand, still strong and living, two tall trees.
'Well, here we are at last' says Gandalf.\n""")

    input("\nPress enter to continue\n")
    gates_of_Moria()


# is called when the player looses anywhere in the game.
# Asks if they want to play again, if so back to start, if no exit
def game_over():
    valid_answers_y_n = ["y", "n", "yes", "no"]
    answer = ""
    while answer is not valid_answers_y_n:
        print("""\nYou have lost the game and did not manage to cross the mines of Moria safely.
Would you like to play again (y/n)?\n""")
        answer = input(">").lower()
    
        if "y" in answer:
            start_game()
        elif "n" in answer:
            print("\nThank you for playing!\n")
            exit()
        else:
            print("\nInvalid answer, please enter one of the following characters: 'y' or 'n'\n")


 # narrative brings them to the gates. Multiple choice question to open the gates.
def gates_of_Moria():
    # explanation of the story and prompts to answer a question
    print()

    print("""What do you do? (enter 1, 2 or 3)
    1) Cast an opening spell in elvish: 'Edro' 
    2) Say the elvish word for friend: 'Mellon'
    3) Knock on the doors with Pippin's head""")

    answer = ""
    while answer != "2":
        answer = input(">")
        if answer == "2":
            print("""\nSilently, a great door is outlined, though not a crack or joint was visible before.
Slowly it divides in the middle and swings outwards inch by inch, until both doors lay back against the wall.
You stare in wonder\n""")
            input("\nPress enter to continue\n")
            watcher_in_water()
        elif answer == "1" :
            # wrong answer, try again
            print("\nNothing happens and the gates will not budge. Try again!\n")  
        elif answer == "3":
            print("\nThis did not shatter them. I guess Gandalf needs a little peace from foolish questions and find some opening word. Try again ...\n")
        else:
            print("\nInvalid answer, please enter one of the following numbers 1, 2, or 3\n")
    


# simple battle sequence with fellowship beginning. Random points are deducted in turn, first from enemy and then from fellowship. If either f or e reaches 0 the game stops and either a win (1) or loose (0) value is passed to determine the next course of action.
def simple_battle_fellowship_start(life_fellowship, life_enemy, enemy):
    print(f"\nThe battle begins. You have {life_fellowship} life points and the {enemy} has {life_enemy} life points\n")
    while life_fellowship > 0 and life_enemy > 0:
        damage = randint(1,6)
        life_enemy -= damage
        input(f"You deal {damage} damage to the {enemy}. The {enemy} now has {life_enemy} life points remaining. \nPress enter to continue\n")
        if life_enemy < 1:
            print("\nYou win\n")
            return True
        damage = randint(1,6)
        life_fellowship -= damage
        input(f"The {enemy} deals {damage} damage to you and you now have {life_fellowship} life points remaining. \nPress enter to continue\n")
        if life_fellowship < 1:
            print("\nYou loose\n")
            return False

# simple battle sequence with enemy beginning. Random points are deducted in turn, first from enemy and then from fellowship. If either f or e reaches 0 the game stops and either a win (1) or loose (0) value is passed to determine the next course of action.
def simple_battle_enemy_start(life_fellowship, life_enemy, enemy):
    print(f"\nThe battle begins. You have {life_fellowship} life points and the {enemy} has {life_enemy} life points\n")
    while life_fellowship > 0 and life_enemy > 0:
        damage = randint(1,6)
        life_fellowship -= damage
        input(f"The {enemy} deals {damage} damage to you and you now have {life_fellowship} life points remaining.\n Press enter to continue\n")
        if life_fellowship < 1:
            print("\nYou loose\n")
            return False
        damage = randint(1,6)
        life_enemy -= damage
        input(f"You deal {damage} damage to the {enemy}. They now have {life_enemy} life points remaining.\n Press enter to continue\n")
        if life_enemy < 1:
            print("\nYou win\n")
            return True

# stores all ridles as separate variables and then creates a list of all the riddle variables. 
# Also has a list of all riddle answers. Then generates random index number to pull random riddle
# + answer from the lists. User has 3 attempts to guess a riddle, if correct progress to next stage,
# if wrong user will be provided with answer, that riddle + asnwers is removed from list, and an attempt
# is subtracted from the total attempt numbers. Then the function starts again with one less attempt and
# one less riddle to avoid duplication of riddles. To allow for flexibility in the number of random riddles,
# I used the len() function to determin the length of the list and had that -1 to be the max value for the random
# number selection.
def riddle_game():
    riddle1 = """\nalive without breath
as cold as death
never thirsty, ever drinking
all in mail never clinking\n"""
    riddle2 = """\nit cannot be seen, cannot be felt
cannot be heard, cannot be smelt
it lies behind stars and under hills
and empty holes it fills
it comes out first and follows after
ends life, kills laughter\n"""
    riddle3 = """\nvoiceless it cries
wingless flutters
toothless bites
mouthless mutters\n"""
    riddle4 = """\nwhat has roots as nobody sees
is taller than trees
up, up, up it goes
and yet never grows\n"""
    riddle5 = """\na thing that all things devours
birds, beasts, trees, flowers
gnaws iron, bites steel
grinds hard stones to meal
slays kind, ruins town
and beats mountains down\n"""
    riddle6 = """\nthirty white horses on a red hill
first they champ,
then they stamp,
then they stand still\n"""
    riddle7 = """\na box without hinges, key, or lid
yet golden treasure inside is hid\n"""
    
    riddles = [riddle1, riddle2, riddle3, riddle4, riddle5, riddle6, riddle7]
    riddle_answers = ["fish", "dark", "wind", "mountain", "time", "teeth", "egg"]
    
    attempts = 3
    while attempts > 0:

        random_end = len(riddles)
        random_riddle = randint(0,random_end-1)
    
        print(riddles[random_riddle])
        print("\nPlease type in your one-word answer:\n")
        riddle_user_answer = input("<").lower()

        if riddle_user_answer == riddle_answers[random_riddle]:
            print("\ncorrect\n")
            return True
        else:
            attempts -= 1
            if attempts == 0:
                print("\nYou loose\n")
                return False
            else:
                print(f"Sorry, the answer was {riddle_answers[random_riddle]}, you have {attempts} attempts at solving a riddle left. \n")
                riddles.pop(random_riddle)
                riddle_answers.pop(random_riddle)


def Gollum():
    print("""'\nI do not like the feel of the middle way' says Gandalf, 'but the ringbearer has decided,
so we will go ahead'. You make your way through the smooth, level, narrow passage way. However, the passage 
way has many side-turns and soon you find yourself utterly lost in the depths of Moria. Then, you start
hearing hissing and throaty noises and you see a pair of pale eyes in front of you. It's Gollum and he is
blocking your way. Knowing he is outnumbered, and remembering Gandalf, Aragorn and Legolas from his previous 
experiences of captivity, he decides to help you find way out in return for his freedom, but only if you 
know the answer to one of his riddles. Gollum asks you your first riddle: \n""")

    wins_riddle_game = riddle_game()
    if wins_riddle_game == True:
        print("""\nYou beat Gollum at a game of riddles, and he starts to lead you to the eastern gate. While following
Golllum, you express your doubts about giving him his freedom. 'It's a pity Bilbo didn't kill him when he had
the chance' you say. 'Pity? It was pity that stayed Bilbo's hand. Many that live deserve death, and some that
die deserve life. Can you give it to them? Do not be too eager to deal out death and judgement. Even the very
wise cannot see all ends'.

Do you show pity and give Gollum his freedom? (enter y for 'yes' or n for 'no')\n""")
        valid_answers = ["y", "n", "yes", "no"]
        answer_gollum = ""
        
        while answer_gollum is not valid_answers:

            answer_gollum = input("<").lower()
            if "y" in answer_gollum:
                print("""\nGollum overhears you, and while you are not looking, slips into a side-passage and
diasappears from sight. You have no choice but to carry on the path he set you.\n""")
                input("\nPress enter to continue\n")
                chamber_of_Mazarbul()
            elif "n" in answer_gollum:
                print("""\nGollum overhears you, and while you are not looking, slips into a side-passage and 
dissapears from sight, leaving you stranded to slowly starve to death in the Mines of Moria.\n""")
                game_over()
            else:
                print("\nInvalid answer, please enter one of the following characters: 'y' or 'n'\n")


    else:
        print("""\nWhile you are busy trying to think of the answers to Gollum's riddles, he snatches the ring from
Frodo's neck, puts it on and disappears, leaving you stranded to slowly starve to death in the Mines of Moria.\n""")
        input("\nPress enter to continue\n")
        game_over()


def balrog_fight():
    balrog_intro = """\n'Look ahead!' calls Gandalf. 'The Bridge is near. It is dangerous and narrow.'
Suddenly, you see before you a great shadow, in the middle of which is a dark form, of man-shape maybe, 
yet greater; and a power and terror seem to be in it and to go before it.'Ai! ai!' wails Legoals. 'A Balrog!
A Balrog is come!' 'Over the bridge' cries Gandalf. 'Fly! This is a foe beyond any of you. I must hold the
bridge. Fly! Gandalf stands and faces the balrog, but must decide a strategy:\n """
    balrog_choices = """\n1) defensive
2) agressive
3) sneaky"""
    choice = "\nWhat does Gandalf choose: 1, 2, or 3?\n"
    balrog_win_speech = """\n'You cannot pass!' says Gandalf while he lifts his staff, and crying aloud, smites 
the bridge before him. The staff breaks asunder and falls from his hand. A blinding sheet of white flame springs
up. The bridge cracks and breaks right at the feet of the Balrog. With a terrible cry, the Balrog falls forward,
and its shadow plunges down and vanishes. But even as it falls it swings its whip, and the thongs lash and curl
around the wizard's knees, dragging him to the brink. He staggers and falls. 'Fly, you fools!', he cries, and is gone.
With a cry Aragorn rouses you. 'Come! I will lead you now!' he calls. 'We must obey his last command. Follow me!'
Out of the gates you run and spring down the hughe and age-worn steps, the threshold of Moria. Thus, at last, you
come beyond hope under the sky and feel the wind on your face.

You have succesfully navigated the Mines of Moria. Watch out for the fellowship's next adventures!\n"""
    balrog_loose_speech = """\n'You cannot pass!' says Gandalf while he lifts his staff, and crying aloud, attempts to smite 
the bridge before him. But the balrog swings its whip, and the thongs lash and curl
around the wizard's knees, pulling him from the bridge and throwing them into the abyss. He staggers and falls. 'Fly, you fools!', he cries, and is gone.
But you stand rooted, and without Gandalf to defend you, the Balrog seizes you and engulfs you in flame and shadow.\n"""
    
    print(balrog_intro)
        
    strategy_gandalf = ""
    strategy_balrog = ""
    
    life_gandalf = 3
    life_balrog = 3
    
    tie = "\nNothing happens\n"
    battle_turn_win = "\nGandalf deals a blow to the Balrog\n"
    battle_turn_loose = "\nThe Balrog deals a blow to Gandalf\n"
    strategy_balrog_str = ""
    strategy_gandalf_str = ""

    while life_gandalf and life_balrog != 0:
        print(f"{balrog_choices}\n\n{choice}")
        strategy_gandalf = int(input("<"))
        strategy_balrog = randint(1,3)

        if strategy_gandalf == 1:
            strategy_gandalf_str = "1) defensive"
        elif strategy_gandalf == 2:
            strategy_gandalf_str = "2) agressive"
        elif strategy_gandalf == 3:
            strategy_gandalf_str = "3) sneaky" 
    
    
        if strategy_balrog == 1:
            strategy_balrog_str = "1) defensive"
        elif strategy_balrog == 2:
            strategy_balrog_str = "2) agressive"
        elif strategy_balrog == 3:
            strategy_balrog_str = "3) sneaky"
    
        battle_turn_outcome = f"you chose {strategy_gandalf_str} and the Balrog chose {strategy_balrog_str}."
        print(battle_turn_outcome)

        if strategy_gandalf == strategy_balrog:
            life_display = f"You have {life_gandalf} life points and the balrog has {life_balrog} life points remaining"
            print(tie, life_display)        
        elif (strategy_gandalf == 2 and strategy_balrog == 1) or (strategy_gandalf == 3 and strategy_balrog == 1) or (strategy_gandalf == 2 and strategy_balrog == 3):
            life_balrog -= 1
            life_display = f"You have {life_gandalf} life points and the balrog has {life_balrog} life points remaining"
            print(battle_turn_win, life_display)   
        elif (strategy_gandalf == 1 and strategy_balrog == 2) or (strategy_gandalf == 3 and strategy_balrog == 2) or (strategy_gandalf == 1 and strategy_balrog == 3):
            life_gandalf -= 1
            life_display = f"You have {life_gandalf} life points and the balrog has {life_balrog} life points remaining"
            print(battle_turn_loose, life_display)   
        
    if life_gandalf > 0:
        print(balrog_win_speech)
    else:
        print(balrog_loose_speech)
        game_over()

def chamber_of_Mazarbul():
    print("""\nAt last you have come to the habitable parts, and you are not far from the eastern exit. But it is
a long way down to the Gates that open on the world!, so you decide to rest a little. You see a light behind a door
in the northern part of the hall, and think that might be a good place to rest. You pass through the northern
arch and find yourself in a large square chamber. It is dimly lit by a wide shaft high in the further eastern wall, 
but to your eyes, after so long a time in the dark, it seems dazzilingly bright. The light of the shaft falls directly
on a talbe in the middle of the room. 'It looks like a tomb' you mutter and on it are engraved Dwarvish runes. They
read 'Here lies Balin, son of Fundin, Lord of Moria' says Gandalf. He has hardly spoken these words, when there comes
great noise: a rolling Boom that seems to come from the depths far below. The sound keeps coming nearer and nearer 
'Doom, Doom, Dooom' like a drum-beat. Heavy feet are heard in the corridor. There are Orcs, very many of them, but there
is something else there. A great cave-troll, I think, or more than one.\n""")

    print("""
    What do you do? (enter 1 or 2)
    
    1) stay and fight
    2) flee""")

    has_won = False
    answer = ""

    while answer != "1" or answer != "2":
        answer = input(">")
        if answer == "1":
            print("\nYour valour is rewarded and you may deal the first blow\n")
            input("\nPress enter to continue\n")  
            has_won = simple_battle_fellowship_start(15, 15, "Orcs and Cave trolls")
            break
        elif answer == "2":
            print("""\nYou try to run, but find all the ways are blcoked and the orcs and cave trolls have now
            entered the room you are in, ready to deal the first blow.\n""")
            input("\nPress enter to continue\n")  
            has_won = simple_battle_enemy_start(15,14,"Orcs and Cave trolls")
            break
        else:
            print("I\nnvalid answer, please enter one of the following numbers 1 or 2\n")

    if has_won == True:
       print("""\n'Well, well! That's over!' says the wizard struggling to his feet. 'But don't stand here! Go on!\n""")
       input("\nPress enter to continue\n")  
       balrog_fight()
    elif has_won == False:
       print("\nThe orcs overwhelm you and kill you, taking the ring from Frodo and delivering it to Sauron.\n")
       game_over()

def follow_your_nose():
    print("""\nThe fellowship has been going for several hours with only brief halts, when Gandalf comes 
to his first serious check. Before him stands a wide arch opening into three passages: all lead in
the same general direction, eastwards:
- but the left-hand passage plunges down;
- while the right hand climbs up;
- and the middle way seems to run on, smooth and level but narrow.\n""")

    print("""Which way do you choose? (enter 1, 2, or 3)
    1) left
    2) middle
    3) right""")

    answer = ""
    valid_input = ["1", "2", "3", "y", "n", "yes", "no"]

    while answer not in valid_input:
        answer = input(">")    
        if answer == "1":
            answer_mythril = ""
            while answer_mythril not in valid_input:
                print("'\nI do not like the smell of the left-hand way' says Gandalf 'are you sure'? (y/n)\n")
                answer_mythril = input("<").lower()
                if "y" in answer_mythril:
                    print("""\n'Well, if you're sure' says Gandalf. 'You are the ring-bearer.'You take the steep path down,
further and further into the depths of Moria. After several hours of walking, you see the familiar 
slender veins of silver running through the stone. 'Mythril' exclaims Gimli. 'The wealth of Moria was not in Gold and jewels
, the toys of the Dwarves, nor in iron: their servant. Here alone in the world was found Moria-silver, or true-silver as some
have called it: mithril is the Elvish name. Its worth was ten times that of gold and now it is beyond price, for little is
left above ground' says Gandalf.Your greed gets the better of you, and you decide to abandon your quest to mine the mythril. 
You become a wealthy merchant and live in luxury for a while, but eventually Sauron finds you, kills you and takes the ring from you.\n""")
                    game_over()
                elif "n" in answer_mythril:
                    print("'\nWise choice!' says Gandalf. 'If in doubt, always follows your nose'!\n")
                    input("\nPress enter to continue\n")  
                    follow_your_nose()
                else:
                    print("\nInvalid answer, please enter one of the following characters: 'y' or 'n'\n")
        elif answer == "2":
            Gollum()
        elif answer == "3":
            print("""\nYou have marched as far as you can endure without a rest, and you are thinking of a place to sleep, 
when suddenly the walls to the left and right vanish. You seem to have passed through some doorway into a black 
and empty space. Gandalf seems pleased 'I chose the right way', he says.\n""")
            input("\nPress enter to continue\n")  
            chamber_of_Mazarbul()
        else:
            print("\nInvalid answer, please enter one of the following numbers: 1, 2, or 3\n")

# Fight the watcher in the water. If choose to fight, player goes first. 
# If choose to flee, Watcher goes first.
def watcher_in_water():
    watcher_win_speech = """\n'Into the gateway! Up the stairs! Quick!' shouts Gandalf leaping back. You are just in time.
Sam and Frodo are only a few steps up, and Gandalf begins to climb, when the groping 
tentacles writhe across the narrow shore and finger the cliff-wall and the doors. If Gandalf is considering
what word will close the gate again from within, there is no need. Many coiling arms seize the door on either side,
and with horrible strength swing them around. With a shattering echo they slam, and all light is lost.
A noise of rending and crashing comes dully through the ponderous stone. 'Well, well!' says the wizard.
'The passage is blocked behind us now, and there is only one way out - on the other side of the mountains.'\n"""
    watcher_loose_speech = "\nThe Watcher in the Water grabs you and drags you under water. You are never seen or heard of again!\n"
    watcher_start = """\nBut then the water behind you starts boiling and out from the water a long sinuous tentacle crawls.
It is pale-green and luminious and wet.

What do you do? (enter 1 or 2)

    1) You stay and fight
    2) You flee!\n"""
    print(watcher_start)

    has_won = False
    answer = ""

    while answer != "1" and answer != "2":
        answer = input(">")
        if answer == "1":
            print("Your valour is rewarded and you may deal the first blow")
            input("Press enter to continue")  
            has_won = simple_battle_fellowship_start(15, 15, "Watcher in the Water")
        elif answer == "2":
            print("""Frodo is too slow and one of the tentacles grabs him by the ankle, 
            forcing the rest of the fellowship to stay and fight. 
            The watcher in the water deals the first blow""")
            input("Press enter to continue")  
            has_won = simple_battle_enemy_start(15,14,"Watcher in the Water")
        else:
            print("Invalid answer, please enter one of the following numbers 1 or 2")

    
    if has_won == True:
       print(watcher_win_speech)
       follow_your_nose()
    elif has_won == False:
       print(watcher_loose_speech)
       game_over()


start_game()