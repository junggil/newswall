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
                                   'w'  : '국제',
                                   'b'  : '경제',
                                   'y'  : '사회',
                                   'l'  : '문화/생활',
                                   'p'  : '정치',
                                   't'  : '정보과학',
                                   'e'  : '연예',
                                   's'  : '스포츠',
                                   'po' : '인기뉴스',
                                  }
                      },
              'us' : { 
                       'ned'    : 'en',
                       'topics' : {
                                  'w'   : 'WORLD',
                                  'm'   : 'HEALTH',
                                  'b'   : 'BUSINESS',
                                  'e'   : 'ENTERTAIN',
                                  'tc'  : 'TECHNOLOGY',
                                  'snc' : 'SCIENCE',
                                  's'   : 'SPORTS',
                                  'ir'  : 'SPOTLIGHT',
                                  }
                      },
              'zh-CN' : { 
                       'ned'    : 'cn',
                       'topics' : {
                                   'b'  : '财经',
                                   'y'  : '社会',
                                   'w'  : '国际/港台',
                                   't'  : '科技',
                                   'e'  : '娱乐',
                                   's'  : '体育',
                                   'po' : '热门报道',
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

