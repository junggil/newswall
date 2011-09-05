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
                                   'WORLD'        : 'w',
                                   'ECONOMY'      : 'b',
                                   'SOCIATY'      : 'y',
                                   'CULTURE'      : 'l',
                                   'POLITICS'     : 'p',
                                   'TECHNOLOGY'   : 't',
                                   'ENTERTAIN'    : 'e',
                                   'SPORTS'       : 's',
                                   'POPULAR'      : 'p'
                                  }
                      },
              'us' : { 
                       'ned'    : 'en',
                       'topics' : {
                                   'WORLD'        : 'w',
                                   'HEALTH'       : 'm',
                                   'BUSINESS'     : 'b',
                                   'ENTERTAIN'    : 'e',
                                   'TECHNOLOGY'   : 'tc',
                                   'SCIENCE'      : 'snc',
                                   'SPORTS'       : 's',
                                   'SPOTLIGHT'    : 'ir',
                                  }
                      },
              'zh-CN' : { 
                       'ned'    : 'cn',
                       'topics' : {
                                   'ECONOMY'      : 'b',
                                   'SOCIATY'      : 'y',
                                   'WORLD'        : 'w',
                                   'TECHNOLOGY'   : 't',
                                   'ENTERTAIN'    : 'e',
                                   'SPORTS'       : 's',
                                   'POPULAR'      : 'p'
                                  }
                      }
            }

    def __init__(self, locale):
        self.locale = locale

    def checkPickledFeed(self):
        return False

    def getRSS(self, topic):
        if not self.checkPickledFeed():
            return feedparser.parse(self.TEMPLATE % {'topic'     : self.FEED[self.locale]['topics'][topic], 
                                                     'territory' : self.FEED[self.locale]['ned'],
                                                     'language'  : self.locale,
                                                     }).entries
    def getAllTopics(self):
        return self.FEED[self.locale]['topics']
  
    def getAllLocales(self):
        return self.FEED.keys()

