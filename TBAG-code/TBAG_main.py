from TBAG_start_finish import *
from TBAG_gates_of_moria import *

start_game()

gates_of_moria_scene = gates_of_moria_setup()
gates_of_moria_win = gates_of_moria_play(gates_of_moria_scene)
if gates_of_moria_win == True:
    print("You will go to scene Watcher in the Water")
else:
    print("Try again")


