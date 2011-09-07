# -*- coding: utf-8 -*-
import feedparser

from random import choice
from pickle import dump, load
from time   import time, localtime, asctime

class GoogleNews(object):
    TEMPLATE = 'http://news.google.com/news?pz=1&cf=all&ned=%(territory)s&hl=%(language)s&topic=%(topic)s&output=rss'
    FEED = {
              'ko' : { 
                       'ned'    : 'kr',
                       'topics' : {
                                   'w'  : u'국제',
                                   'b'  : u'경제',
                                   'y'  : u'사회',
                                   'l'  : u'문화/생활',
                                   'p'  : u'정치',
                                   't'  : u'정보과학',
                                   'e'  : u'연예',
                                   's'  : u'스포츠',
                                   'po' : u'인기뉴스',
                                  }
                      },
              'us' : { 
                       'ned'    : 'en',
                       'topics' : {
                                  'w'   : u'WORLD',
                                  'm'   : u'HEALTH',
                                  'b'   : u'BUSINESS',
                                  'e'   : u'ENTERTAIN',
                                  'tc'  : u'TECHNOLOGY',
                                  'snc' : u'SCIENCE',
                                  's'   : u'SPORTS',
                                  'ir'  : u'SPOTLIGHT',
                                  }
                      },
              'zh-CN' : { 
                       'ned'    : 'cn',
                       'topics' : {
                                   'b'  : u'财经',
                                   'y'  : u'社会',
                                   'w'  : u'国际/港台',
                                   't'  : u'科技',
                                   'e'  : u'娱乐',
                                   's'  : u'体育',
                                   'po' : u'热门报道',
                                  }
                      }
            }

    def __init__(self, locale):
        self.locale = locale

    def checkPickledFeed(self):
        return False

    def getRSS(self, topic):
        if not self.checkPickledFeed():
            return feedparser.parse(self.TEMPLATE % {'topic'     : topic,
                                                     'territory' : self.FEED[self.locale]['ned'],
                                                     'language'  : self.locale,
                                                     }).entries
    def getAllTopics(self):
        return self.FEED[self.locale]['topics']
  
    def getAllLocales(self):
        return self.FEED.keys()

