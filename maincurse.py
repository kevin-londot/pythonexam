import curses
import sys
import time
import init
import player
import box
import switch
import collision

def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()

    gameMap, player1, boxes, switches = init.reset(sys.argv[1], stdscr)

    while True:
        entry = stdscr.getch()

        if (entry == ord(" ")):
            gameMap, player1, boxes, switches = init.reset(sys.argv[1], stdscr)

        if (entry == curses.KEY_UP or entry == curses.KEY_RIGHT or entry == curses.KEY_DOWN or entry == curses.KEY_LEFT):
            player1.movePlayer(entry,gameMap,boxes,switches,stdscr)

        if entry == 3:
            raise KeyboardInterrupt

if __name__ == "__main__":
    # recuperer la carte
    if (len(sys.argv) != 2):
        sys.exit("Il faut charger une et une seule map.")

    curses.wrapper(main)
