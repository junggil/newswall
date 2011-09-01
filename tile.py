import re
from random import randint, choice, random as rand
from pprint import pprint as pp

class TileBox(object):
    BOUNDARY_X, BOUNDARY_Y = (10, 8)
    UNIT_MAX_X, UNIT_MAX_Y = ( 4, 3)

    def __init__(self):
        self.canvas     = [['*'] * self.BOUNDARY_X for ver in range(self.BOUNDARY_Y)]
        self.css_id     = ord('A')
        self.position   = (0, 0)
        self.trace      = []

    def move(self):
        posX, posY = self.position 
        for tile in self.canvas[posY:]:
            if '*' not in tile:
                posY += 1
            else:
                posX = ''.join(tile).index('*')
                break

        self.position = posX, posY

    def getTile(self):
        posX, posY = self.position 
        boxX, boxY = (self.UNIT_MAX_X, 0)
        for tile in self.canvas[posY:]:
            if tile[posX] is not '*':
                break
            else:
                boxY = boxY + 1
                boxX = min(boxX, len(re.compile('[^*]').split(''.join(tile[posX:]))[0]))

        return self.distort((boxX, min(boxY, self.UNIT_MAX_Y)))

    def distort(self, tileSize, factor = 1.6):
        tileX, tileY = tileSize
        return (max(min(int(tileX * rand() * factor), tileX), 1),
                max(min(int(tileY * rand() * factor), tileY), 1))

    def fill(self, tileSize):
        posX, posY = self.position 
        lenX, lenY = tileSize
        for tile in self.canvas[posY:posY+lenY]:
            tile[posX:posX+lenX] = [chr(self.css_id)] * lenX
        self.css_id += 1
        self.trace.append((self.position, tileSize))

    def checkAvailable(self, tileSize):
        patial_tile = ''
        posX, posY = self.position
        lenX, lenY = tileSize
        for tile in self.canvas[posY:posY+lenY]:
            patial_tile += reduce(lambda foo, bar: foo + bar,  tile[posX:posX+lenX])
        return patial_tile == '*' * len(patial_tile)

    def checkDone(self):
        do_flat = lambda foo, bar: foo + bar
        return '*' not in reduce(do_flat, reduce(do_flat, self.canvas))

    def draw(self):
        pp(self.canvas)

    def getTrace(self):
        return self.trace

    def getUnitSize(self, canvasSize):
        canvasX, canvasY = canvasSize 
        return (canvasX / self.BOUNDARY_X, canvasY / self.BOUNDARY_Y)

if __name__ == '__main__':
    box = TileBox()

    import time
    while not box.checkDone():
        newTile = box.getTile()
        if box.checkAvailable(newTile):
            box.fill(newTile)
        box.move()
    box.draw()
