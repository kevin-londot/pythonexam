import curses
import time
import player

def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    while True:
        entry = stdscr.getch()
        stdscr.clear()
        #print(player)
        player1.movePlayer(entry,stdscr)

        
        if entry == 3:
            raise KeyboardInterrupt


if __name__ == "__main__":
    # recuperer la carte
    # on cherche ou est le p (x y)
    # joueur = Joueur(x, y)
    player1 = player.Player(10,10)
    curses.wrapper(main)
