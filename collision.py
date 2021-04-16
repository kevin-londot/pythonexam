import curses
import player
import box
import switch

def checkCollision(gameMap, boxes, switches, object, key, stdscr) :
    if isinstance(object, player.Player) or isinstance(object, box.Box):
        if key == curses.KEY_UP:
            if gameMap[object.coordY - 1][object.coordX] == "#":
                return False
            else:
                isBox = False
                boxIndex = -1
                for i in range(0, len(boxes)):
                    if (boxes[i].coordX == object.coordX and boxes[i].coordY == object.coordY - 1):
                        isBox = True
                        boxIndex = i
                if boxIndex >= 0:  
                    isMovable = boxes[boxIndex].moveBox(key, gameMap, boxes, switches, stdscr)
                    return isMovable
            return True
        if key == curses.KEY_RIGHT:
            if gameMap[object.coordY][object.coordX + 1] == "#":
                return False
            else:
                isBox = False
                boxIndex = -1
                for i in range(0, len(boxes)):
                    if (boxes[i].coordX == object.coordX + 1 and boxes[i].coordY == object.coordY):
                        isBox = True
                        boxIndex = i
                if boxIndex >= 0:
                    isMovable = boxes[boxIndex].moveBox(key, gameMap, boxes, switches, stdscr)
                    return isMovable
            return True
        if key == curses.KEY_DOWN:
            if gameMap[object.coordY + 1][object.coordX] == "#":
                return False
            else:
                isBox = False
                boxIndex = -1
                for i in range(0, len(boxes)):
                    if (boxes[i].coordX == object.coordX and boxes[i].coordY == object.coordY + 1):
                        isBox = True
                        boxIndex = i
                if boxIndex >= 0:
                    isMovable = boxes[boxIndex].moveBox(key, gameMap, boxes, switches, stdscr)
                    return isMovable
            return True
        if key == curses.KEY_LEFT:
            if gameMap[object.coordY][object.coordX - 1] == "#":
                return False
            else:
                isBox = False
                boxIndex = -1
                for i in range(0, len(boxes)):
                    if (boxes[i].coordX == object.coordX - 1 and boxes[i].coordY == object.coordY):
                        isBox = True
                        boxIndex = i
                if boxIndex >= 0:
                    isMovable = boxes[boxIndex].moveBox(key, gameMap, boxes, switches, stdscr)
                    return isMovable
            return True