from random import triangular as randvar
from pprint import pprint as pp

class TileBox(object):
    HORIZONTAL  = 10
    VERTIVAL    = 8
    SIZE_WEIGHT = 0.8

    def __init__(self):
        self.canvas     = [['*'] * self.HORIZONTAL for ver in range(self.VERTIVAL)]
        self.css_id     = ord('A')
        self.position   = (0, 0)
        self.trace      = []

    def move(self):
        relX, relY = self.HORIZONTAL, self.VERTIVAL
        self.position = (int(randvar(0, relX, (1 - self.SIZE_WEIGHT) * relX)), 
                         int(randvar(0, relY, (1 - self.SIZE_WEIGHT) * relY)))

    def getTile(self):
        posX, posY = self.position 
        relX, relY = (self.HORIZONTAL, 1)
        for tile in self.canvas[posY:]:
            if tile[posX] is not '*':
                break
            else:
                relY = relY + 1
                relX = min(relX, ''.join(tile[posX:]).rindex('*') + 1)

        relX = relX == 1 and 1 or int(randvar(1, relX, self.SIZE_WEIGHT * relX))
        relY = relY == 1 and 1 or int(randvar(1, relY, self.SIZE_WEIGHT * relY))
        return relX, relY

    def fill(self, newTile):
        posX, posY = self.position 
        lenX, lenY = newTile 
        for tile in self.canvas[posY:posY+lenY]:
            tile[posX:posX+lenX] = [chr(self.css_id)] * lenX
        self.css_id += 1
        self.trace.append((self.position, newTile))

    def checkAvailable(self, tileSize):
        patial_tile = ''
        posX, posY = self.position
        lenX, lenY = tileSize
        for tile in self.canvas[posY:posY+lenY]:
            patial_tile += reduce(lambda foo, bar: foo + bar, tile[posX:posX+lenX])
        return patial_tile == '*' * len(patial_tile)

    def checkDone(self):
        do_flat = lambda foo, bar: foo + bar
        return '*' not in reduce(do_flat, reduce(do_flat, self.canvas))

    def draw(self):
        pp(self.canvas)

    def histogram(self):
        tile_area    = lambda foo, bar : foo * bar
        rule_by_area = lambda foo, bar : tile_area(*bar[1]) - tile_area(*foo[1])
        self.trace.sort(rule_by_area)
        for offset, tile in enumerate(self.trace):
            print 'css', offset, ':', tile


if __name__ == '__main__':
    box = TileBox()

    while not box.checkDone():
        newTile = box.getTile()
        if box.checkAvailable(newTile):
            box.fill(newTile)
        box.move()

    box.draw()
    box.histogram()
