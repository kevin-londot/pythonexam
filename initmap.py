import curses

def initialisationMap(filemap, stdscr):
    stdscr.clear()
    map = []
    with open(filemap, 'r') as file:
        for line in file:
            map.append(line.strip())
    for i in range(0, len(map)):
        stdscr.addstr(i, 0, map[i])
        stdscr.refresh()
    return map