from TBAG_Classes import *

def gates_of_moria_setup():
    gates_of_moria = Scene("Moria")
    gates_of_moria.set_opener("""\nThe moon shines upon the grey face of rock, but you can see nothing.
Then slowly on the surface, where the wizard's hands passed, faint lines appear,
like slender veins of silver running in the stone, twinkling in the moonlight.
The lines read:

The Doors of Durin, Lord of Moria. Speak, friend, and enter\n""")

    gates_of_moria.set_win_closer("""\nSilently, a great door is outlined, though not a crack or joint was visible before.
Slowly it divides in the middle and swings outwards inch by inch, until both doors lay back against the wall.
You stare in wonder\n""")
    gates_of_moria.set_loose_closer("\nNothing happens and the gates will not budge. Try again!\n")
    gates_of_moria.set_alternative_closer("\nThis did not shatter them. I guess Gandalf needs a little peace from foolish questions and find some opening word. Try again ...\n")

    return gates_of_moria

def gates_of_moria_play(gates_of_moria):
    gates_of_moria.print_opener()

    gates_of_moria_question = Question("gates_of_moria")
    gates_of_moria_question.set_text("""What do you do (enter 1, 2 or 3)?
    1) Cast an opening spell in elvish: 'Edro'
    2) Say the elvish word for friend: 'Mellon'
    3) Knock on the doors with Pippin's head""")
    gates_of_moria_question.print_text()
    

    while gates_of_moria_question.validity == False or gates_of_moria_question.get_answer() != "2":
        gates_of_moria_question.set_answer()
        gates_of_moria_question.validity = gates_of_moria_question.check_answer_validity(["1", "2", "3"])
        if gates_of_moria_question.validity == False:
            print("\n Invalid answer, please enter one of the following numbers: 1, 2, or 3\n")
        else:
            if gates_of_moria_question.get_answer() == "1":
                gates_of_moria.print_loose_closer()
            elif gates_of_moria_question.get_answer() == "2":
                gates_of_moria.print_win_closer()
                return True
            elif gates_of_moria_question.get_answer() == "3":
                gates_of_moria.print_alternative_closer()




# end you win