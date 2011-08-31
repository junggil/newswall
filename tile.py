from random import randint, triangular as randvar
from pprint import pprint as pp

class TileBox(object):
    HORIZONTAL  = 10
    VERTIVAL    = 8

    def __init__(self, rule):
        self.canvas     = [['*'] * self.HORIZONTAL for ver in range(self.VERTIVAL)]
        self.css_id     = ord('A')
        self.position   = (0, 0)
        self.trace      = []
        self.rule       = rule

    def move(self):
        self.position = (randint(0, self.HORIZONTAL- 1), randint(0, self.VERTIVAL - 1))

    def getTile(self):
        posX, posY = self.position 
        relX, relY = (self.HORIZONTAL, 1)
        for tile in self.canvas[posY:]:
            if tile[posX] is not '*':
                break
            else:
                relY = relY + 1
                relX = min(relX, ''.join(tile[posX:]).rindex('*') + 1)
        
        return TilePlanning((relX, relY)).doPlace(self.rule)

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

class TilePlanning(object):
    def __init__(self, tileSize):
        self.posX, self.posY = tileSize

        self.RULES = {'RANDOM'       : self.random,
                      'WEIGHT_SUM'   : self.weightSum,
                      'WEIGHT_RAN'   : self.triangular}

        self.SIZE_WEIGHT = 0.8

    def weightSum(self):
        candidates = [(sizeX + 1, sizeY + 1) for sizeX in range(self.posX) for sizeY in range(self.posY) ]
        getWeigth  = lambda foo, bar: foo * bar - abs(foo - bar)**2
        sortComp   = lambda foo, bar: getWeigth(*bar) - getWeigth(*foo)
        candidates.sort(sortComp)
        return choice(candidates[:len(candidates) / 2])

    def triangular(self):
        relX = self.posX == 1 and 1 or int(randvar(1, self.posX, self.SIZE_WEIGHT * self.posX))
        relY = self.posY == 1 and 1 or int(randvar(1, self.posY, self.SIZE_WEIGHT * self.posY))
        return (relX, relY)

    def random(self):
        return (randint(1, round(self.posX * self.SIZE_WEIGHT)),
                randint(1, round(self.posY * self.SIZE_WEIGHT)))

    def doPlace(self, rule):
        try:
            return self.RULES[rule]()
        except:
            return (1, 1)

if __name__ == '__main__':
    box = TileBox('WEIGHT_RAN')

    import time
    while not box.checkDone():
        newTile = box.getTile()
        if box.checkAvailable(newTile):
            box.fill(newTile)
        box.move()
    box.draw()
