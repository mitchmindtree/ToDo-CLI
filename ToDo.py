#!usr/bin/env python


'''

ToDo.py

by Mitchell Nordine

My CLI ToDo.

Usage:
    ToDo.py
    ToDo.py [-h | --help] [-v | --version]
    ToDo.py <project>

Options:
    -h --help           Show this screen.
    -v --version        Show version.

'''


import os, sys
import curses
import curses.textpad as textpad
from pprint import pprint

win = curses.initscr()
HEIGHT, WIDTH = win.getmaxyx()
text = ""
todo = []


def getToDoJsonFP():
    return os.path.join(os.path.expanduser("~"), ".ToDo.json")


def safeExit():
    curses.endwin()
    sys.exit(0)


def addItemToList(item):
    pass


def checkForExit():
    check = text.lower()
    if check == "q" or check == "x" or check == "exit" or check == "quit":
        safeExit()


def checkForAdd():
    if text.lower()[:3] == "add":
        addItemToList(text[2:])
    elif text.lower()[:1] == "+":
        addItemToList(text[0:])


def runText():
    checkForExit()
    win.addstr(10, 5, text)


def removeCharFromText():
    global text
    text = text[:-1]


def addToText(event):
    global text
    text = text+event
    win.addstr(6, 5, text)


def checkEvent(event):
    if event == ord("\n"):
        runText()
        resetCursor()
    elif event == curses.KEY_BACKSPACE or int(event) == 127:
        removeCharFromText()
    else:
        addToText(chr(event))
    win.addstr(1, 5, 'key: \'%s\' <=> %c <=> 0x%X <=> %d' % (curses.keyname(event), event & 255, event, event))
    win.addstr(6, 5, text)


def drawTitle():
    win.addstr(2, 5, "ToDo List")
    win.addstr(3, 5, "---------")


def drawRectangle():
    textpad.rectangle(win, HEIGHT-3, 1, HEIGHT-1, WIDTH-2)


def resetCursor():
    text = ""
    win.move(HEIGHT-2, 2)


def drawAll():
    drawTitle()
    drawRectangle()
    win.addstr(HEIGHT-2, 2, text)


def mainLoop():
    '''Run the main Program Loop. Quit with "q".'''
    drawAll()
    resetCursor()
    while True:
        event = win.getch()
        if event:
            win.clear()
            checkEvent(event)
            drawAll()


def setupCurses():
    curses.noecho()
    #curses.curs_set(0)
    win.keypad(1)


def setup():
    setupCurses()


def main():
    fp = getToDoTxtFP()
    print(fp)
    setup()
    #try:
    mainLoop()
    #except Exception, e:
    #    pprint(e)
    #    safeExit()


if __name__ == "__main__":
    main() 


safeExit()
