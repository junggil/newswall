import feedparser
from random import choice

class GoogleNews(object):
    TEMPLATE = 'http://news.google.com/news?pz=1&cf=all&ned=%(territory)s&hl=%(language)s&topic=%(topic)s&output=rss'
    FEED = {
              'ko' : { 
                       'territory' : 'kr',
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
                       'territory' : 'en',
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
                       'territory' : 'cn',
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

    COLOR_MAP = {
               'BLUE'    : ['WORLD'],
               'BROWN'   : ['ECONOMY'],
               'RED'     : ['SOCIATY', 'SCIENCE'],
               'GREEN'   : ['CULTURE', 'HEALTH'],
               'CYAN'    : ['POLITICS'],
               'PINK'    : ['ENTERTAIN'],
               'PURPLE'  : ['SPORTS'],
               'GRAY'    : ['TECHNOLOGY'],
               'ORANGE'  : ['POPULAR', 'SPOTLIGHT'],
               }

    def __init__(self, locale, topic):
        self.locale = locale
        self.topic  = topic

    def checkPickledfeed(self):
        return False

    def getRSS(self):
        if not self.checkPickledfeed():
            return feedparser.parse(self.TEMPLATE % {'territory' : self.LOCALE[language],
                                                     'language'  : language,
                                                      'topic'    : topic,
                                                     })
    def getTopics(self):
        return self.FEED_TOPIC.keys()
  
    def getLocale(self):
        return self.LOCALE.keys()
