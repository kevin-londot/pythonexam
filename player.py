import curses
import collision

class Player : 

    def __init__(self,coordX,coordY):
        self.coordX = coordX
        self.coordY = coordY
        # self.actionNumber = actionNumber

    def movePlayer(self,key,gameMap,boxes,switches,stdscr):
        if key == curses.KEY_UP :
            if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                stdscr.addstr(self.coordY, self.coordX, " ")
                self.coordY -= 1
                stdscr.addstr(self.coordY, self.coordX, "P")
                stdscr.refresh()
        if key == curses.KEY_RIGHT :
            if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                stdscr.addstr(self.coordY, self.coordX, " ")
                self.coordX += 1
                stdscr.addstr(self.coordY, self.coordX, "P")
                stdscr.refresh()
        if key == curses.KEY_DOWN :
            if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                stdscr.addstr(self.coordY, self.coordX, " ")
                self.coordY += 1
                stdscr.addstr(self.coordY, self.coordX, "P")
                stdscr.refresh()
        if key == curses.KEY_LEFT :
            if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                stdscr.addstr(self.coordY, self.coordX, " ")
                self.coordX -= 1
                stdscr.addstr(self.coordY, self.coordX, "P")
                stdscr.refresh()
            
