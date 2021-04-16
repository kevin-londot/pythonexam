import curses
class Player : 

    def __init__(self,coordX,coordY):
        self.coordX = coordX
        self.coordY = coordY
        # self.actionNumber = actionNumber


    # def initPlayer(coordX,coordY):


    def movePlayer(self, key, stdscr) :
        if key == curses.KEY_UP : 
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordY -= 1
            stdscr.addstr( self.coordY,self.coordX, "P")
            stdscr.refresh()
        if key == curses.KEY_DOWN : 
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordY += 1
            stdscr.addstr( self.coordY,self.coordX, "P")
            stdscr.refresh()
        if key == curses.KEY_RIGHT : 
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordX += 1
            stdscr.addstr( self.coordY,self.coordX, "P")
        if key == curses.KEY_LEFT : 
            stdscr.addstr(self.coordY,self.coordX,  " ")
            self.coordX -= 1
            stdscr.addstr( self.coordY,self.coordX, "P")
            
