import curses
import player
import box
import switch 

def initialisationMap(filemap, stdscr):
    stdscr.clear()
    gameMap = []
    with open(filemap, 'r') as file:
        for line in file:
            gameMap.append(line.strip())
    for i in range(0, len(gameMap)):
        stdscr.addstr(i, 0, gameMap[i])
        stdscr.refresh()
    return gameMap

def initialisationPlayer(gameMap):
    strMap = "".join(gameMap)
    nbPlayer = strMap.count("P")
    if (nbPlayer == 1):
        for i in range(0, len(gameMap)):
            for j in range(0, len(gameMap[i])):
                if (gameMap[i][j] == "P"):
                   return player.Player(j, i)
    else:
        print("1 et 1 seul joueur")

def initialisationBox(gameMap):
    strMap = "".join(gameMap)
    nbBox = strMap.count("O")
    boxes = []
    if (nbBox > 0):
        for i in range(0, len(gameMap)):
            for j in range(0, len(gameMap[i])):
                if (gameMap[i][j] == "O"):
                   boxes.append(box.Box(j, i))
        return boxes
    else:
        print("il faut au moins une boîte")

def initialisationSwitch(gameMap):
    strMap = "".join(gameMap)
    nbSwitches = strMap.count("X")
    switches = []
    if (nbSwitches > 0):
        for i in range(0, len(gameMap)):
            for j in range(0, len(gameMap[i])):
                if (gameMap[i][j] == "X"):
                   switches.append(switch.Switch(j, i))
                   print(switches)
        return switches
    else:
        print("il faut au moins un interrupteur")
   
