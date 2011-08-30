from random import randint
from pprint import pprint as pp

class TileBox(object):
    HORIZONTAL  = 10
    VERTIVAL    = 8

    def __init__(self):
        self.canvas     = [['*'] * self.HORIZONTAL for ver in range(self.VERTIVAL)]
        self.css_id     = ord('A')
        self.position   = (0, 0)

    def move(self):
        self.position = (randint(0, self.HORIZONTAL - 1), randint(0, self.VERTIVAL - 1))

    def getTile(self):
        posX, posY = self.position 
        return (randint(1, min(self.HORIZONTAL, self.HORIZONTAL - posX)), 
                randint(1, min(self.VERTIVAL, self.VERTIVAL - posY)))

    def fill(self, tileSize):
        posX, posY = self.position 
        lenX, lenY = tileSize
        for tile in self.canvas[posY:posY+lenY]:
            tile[posX:posX+lenX] = [chr(self.css_id)] * lenX
        self.css_id += 1

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

if __name__ == '__main__':
    box = TileBox()

    import time
    while not box.checkDone():
        newTile = box.getTile()
        if box.checkAvailable(newTile):
            print box.position, newTile, '{0}th piece'.format(box.css_id - ord('A') + 1)
            box.fill(newTile)
            box.draw()
            time.sleep(0.5)
        box.move()
