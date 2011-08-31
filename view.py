import feedparser

from tile   import TileBox
from random import randint

class TileView(object):
    CANVAS = (1024, 768)
    BORDER = 0

    TEMPLATE = 'background: #%(color)s;font-size:%(font)spx;width:%(width)spx;height:%(height)spx;position:absolute;left:%(left)spx;top:%(top)spx;'
    
    def __init__(self, rule = 'WEIGHT_RAN'):
        box = TileBox(rule)

        while not box.checkDone():
            newTile = box.getTile()
            if box.checkAvailable(newTile):
                box.fill(newTile)
            box.move()
        self.trace = box.getTrace()
        self.unit  = box.getUnitSize(self.CANVAS)

    def getDivs(self):
        return [self.TEMPLATE %  {'color'  : hex(randint(0, 0xFFFFFF))[2:],
                                  'font'   : width * height * 3,
                                  'width'  : width  * self.unit[0], 
                                  'height' : height * self.unit[1],
                                  'left'   : left   * self.unit[0], 
                                  'top'    : top    * self.unit[1]}
                for (left, top), (width, height) in self.trace]
