import feedparser

from re     import sub
from math   import log
from tile   import TileBox
from random import choice

class TileView(object):
    CANVAS = (1280, 720)
    BORDER = 1

    CONF = {
            'border'        : 1, 
            'maxFontSize'   : 400,
            'minFontSize'   : 10,
            'padding'       : 5
           }

    TEMPLATE = {
                'title'     : '<DIV class="box" id="tile%(id)s" onmouseover="showDetail(this);" onmouseout="hideDetail(this);" '
                              'style="background-color: %(color)s;font-size:%(font)spx;width:%(width)spx;height:%(height)spx;left:%(left)spx;top:%(top)spx;">'
                              '<A onclick=\'showArticle("%(link)s"); resizeIF();\'>%(title)s</a>'
                              '</DIV>\n',
                'detail'    : '<DIV id="tile%(id)s_detail" class="box_detail" style="display:none; width:600px; height:300px; background-color:white">'
                              '%(summary)s'
                              '</DIV>\n',
                'header'    : '<!DOCTYPE html>\n'
                              '<HTML>\n'
                              '<HEAD>\n'
                              '<META http-equiv="Content-Type" content="text/html; utf-8">\n'
                              '<LINK rel="stylesheet" type="text/css" href="/site_media/css/common.css"/>\n'
                              '<SCRIPT type="text/javascript" src="/site_media/js/effects.js"></SCRIPT>'
                              '</HEAD>\n'
                              '<TITLE>NewsMap</TITLE>\n'
                              '<BODY style="margin:0" onLoad="timedRefresh(3000)")>\n'
                              '<IFRAME id="articleContainer" onmouseout="hideArticle();" class="newsReader"></IFRAME>\n'
                              '<IMG id="rectangle" src="/site_media/images/rectangle.png" style="display:none; position:absolute;" />\n'
                              '<DIV style="width:1280px; height:720px; overflow:hidden; background-color:black">\n',
                'footer'    : '</DIV>\n' 
                              '</BODY>\n' 
                              '</HTML>\n'
                }

    COLORS = {
               'BLUE'    : ['#154669', '#144365', '#1A5782', '#103650', '#123D5B', '#113854'], 
               'BROWN'   : ['#7B6C19', '#84741A', '#524810', '#5E5313', '#6F6116', '#7F7019'],
               'RED'     : ['#6D1616', '#671515', '#470E0E', '#801A1A', '#621414', '#541111'], 
               'GREEN'   : ['#265511', '#367C19', '#306C16', '#2F6C16', '#1F480E', '#41941E'],
               'CYAN'    : ['#1A8053', '#0B3925', '#1B8557', '#0D432C', '#13613F', '#17754C'],
               'PURPLE'  : ['#180B38', '#3C1C8D', '#200F4C', '#21104E', '#231153', '#401E95'],
               'PINK'    : ['#9C1F8B', '#420D3B', '#741767', '#8C1C7D', '#54114B', '#7F1971'],
              }

    def __init__(self):
        box = TileBox()

        while not box.checkDone():
            newTile = box.getTile()
            if box.checkAvailable(newTile):
                box.fill(newTile)
            box.move()
        self.trace = box.getTrace()
        self.unitX, self.unitY = box.getUnitSize(self.CANVAS)

    def getFontSize(self, tileSize, textLength):
        return (float((self.CONF['maxFontSize'] - self.CONF['minFontSize'])) / textLength) * log(tileSize) + self.CONF['minFontSize']
    
    def manipulate(self, summary):
        return sub('valign="top"', 'valign="center"', summary)

    def removeTail(self, title):
        return sub(' -.*', '', title)

    def getContents(self, feed):
        feedCount  = len(feed)
        themeColor = choice(self.COLORS.keys()) 
        contents = [self.TEMPLATE['title'] % {'id'   : i,
                                            'color'  : choice(self.COLORS[themeColor]),
                                            'font'   : self.getFontSize(width * height, len(self.removeTail(feed[i % feedCount].title))),
                                            'width'  : width  * self.unitX - (self.CONF['padding'] + self.CONF['border']) * 2,
                                            'height' : height * self.unitY - (self.CONF['padding'] + self.CONF['border']) * 2,
                                            'left'   : left   * self.unitX,
                                            'top'    : top    * self.unitY,
                                            'title'  : self.removeTail(feed[i % feedCount].title),
                                            'link'   : feed[i % feedCount].link} + \
                    self.TEMPLATE['detail'] % {'id' : i, 'summary' : self.manipulate(feed[i % feedCount].summary)}
                    for i, ((left, top), (width, height)) in enumerate(self.trace)] 

        return ''.join(contents)

    def getTemplate(self, key):
        return self.TEMPLATE.get(key, '')
