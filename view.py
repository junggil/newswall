import feedparser

from tile   import TileBox
from random import randint, choice

class TileView(object):
    CANVAS = (1280, 720)
    BORDER = 1

    CONF = {
            'border'        : 1, 
            'maxFontSize'   : 64,
            'minFontSize'   : 18,
            'padding'       : 5
            }

    TEMPLATE = {
                'div'       : '<DIV class="box" id="tile%(id)s" style="background-color: %(color)s;font-size:%(font)spx;width:%(width)spx;height:%(height)spx;left:%(left)spx;top:%(top)spx;"> %(title)s </DIV>\n',
                'header'    : '<!DOCTYPE html>\n'
                              '<HTML>\n'
                              '<HEAD>\n'
                              '<META http-equiv="Content-Type" content="text/html; utf-8">\n'
                              '<LINK rel="stylesheet" type="text/css" href="/site_media/css/common.css"/>\n'
                              '</HEAD>\n'
                              '<TITLE>NewsMap</TITLE>\n'
                              '<BODY style="margin:0" onload="javascript:timedRefresh(1000);">\n'
                              '<DIV style="width:1280px; height:720px; overflow:hidden; background-color:black">\n',
                'footer'    : '</DIV>\n' 
                              '</BODY>\n' 
                              '</HTML>\n'
                }

    BG_COLORS = [ "#9C1F1F", "#9C891F", "#449C1F", "#1F9C66", "#1F689C", "#421F9C", "#9C1F8B" ]
    
    def __init__(self):
        box = TileBox()

        while not box.checkDone():
            newTile = box.getTile()
            if box.checkAvailable(newTile):
                box.fill(newTile)
            box.move()
        self.trace = box.getTrace()
        self.unitX, self.unitY = box.getUnitSize(self.CANVAS)

    def getFontSize(self, tileSize):
        return (float((self.CONF['maxFontSize'] - self.CONF['minFontSize'])) / 12) * tileSize + self.CONF['minFontSize']

    def getContents(self, feed):
        contents = [self.TEMPLATE['div'] % {'id'     : i,
                                            'color'  : choice(self.BG_COLORS),
                                            'font'   : self.getFontSize(width * height),
                                            'width'  : width  * self.unitX - (self.CONF['padding'] + self.CONF['border']) * 2,
                                            'height' : height * self.unitY - (self.CONF['padding'] + self.CONF['border']) * 2,
                                            'left'   : left   * self.unitX,
                                            'top'    : top    * self.unitY,
                                            'title'  : i < len(feed) and feed[i].title or 'NewsWall Demo'}
                    for i, ((left, top), (width, height)) in enumerate(self.trace)] 

        return ''.join(contents)

    def getTemplate(self, key):
        return self.TEMPLATE.get(key, '')
