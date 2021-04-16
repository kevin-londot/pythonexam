import curses
import collision

class Box:
    def __init__(self, coordX, coordY, locked=False):
        self.coordX = coordX
        self.coordY = coordY
        self.locked = locked

    def moveBox(self,key,gameMap,boxes,switches,stdscr):
        if (not self.locked):
            if key == curses.KEY_UP:
                if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                    self.coordY -= 1
                    stdscr.addstr(self.coordY,self.coordX, "O")
                    stdscr.refresh() 
                    return True
                return False
            if key == curses.KEY_RIGHT:
                if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                    self.coordX += 1
                    stdscr.addstr(self.coordY,self.coordX, "O")
                    stdscr.refresh() 
                    return True
                return False
            if key == curses.KEY_DOWN:
                if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                    self.coordY += 1
                    stdscr.addstr(self.coordY,self.coordX, "O")
                    stdscr.refresh() 
                    return True
                return False
            if key == curses.KEY_LEFT:
                if collision.checkCollision(gameMap,boxes,switches,self,key,stdscr):
                    self.coordX -= 1
                    stdscr.addstr(self.coordY,self.coordX, "O")
                    stdscr.refresh() 
                    return True
                return False
        else:
            return False