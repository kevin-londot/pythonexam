import curses
import sys
import time
import initmap
import player
import box

def main(stdscr):


    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    map = initmap.initialisationMap(sys.argv[1], stdscr)

    while True:
        entry = stdscr.getch()
        #print(player)
        player1.movePlayer(entry,stdscr)

        
        if entry == 3:
            raise KeyboardInterrupt


if __name__ == "__main__":
    # recuperer la carte
    if (len(sys.argv) != 2):
        sys.exit("Il faut charger une et une seule map.")

    
    # on cherche ou est le p (x y)
    # joueur = Joueur(x, y)
    player1 = player.Player(10,10)
    curses.wrapper(main)
