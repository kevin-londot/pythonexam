import curses

class Box:
    def __init__(self, coordX, coordY, state=False):
        self.coordX = coordX
        self.coordY = coordY
        self.state = state

    def moveBox(self, key, stdscr):
        if key == curses.KEY_UP:
            self.coordY -= 1
            stdscr.addstr( self.coordY,self.coordX, "P")
            stdscr.refresh()
        if key == curses.KEY_RIGHT:
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordX += 1
            stdscr.addstr( self.coordY,self.coordX, "P")
        if key == curses.KEY_DOWN:
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordY += 1
            stdscr.addstr( self.coordY,self.coordX, "P")
            stdscr.refresh()
        if key == curses.KEY_LEFT:
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordX -= 1
            stdscr.addstr( self.coordY,self.coordX, "P")