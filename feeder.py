import feedparser
from random import choice

class GoogleNews(object):
    TEMPLATE = 'http://news.google.com/news?pz=1&cf=all&ned=%(territory)s&hl=%(language)s&topic=%(topic)s&output=rss'
    FEED_TOPIC = {
                  'POLITICS'     : 'p',
                  'ECONOMY'      : 'b',
                  'SOCIATY'      : 'y',
                  'CULTURE'      : 'l',
                  'WORLD'        : 'w',
                  'TECHNOLOGY'   : 't',
                  'ENTERTAIN'    : 'e',
                  'SPORTS'       : 's',
                  'POPULAR'      : 'p'
                 }

    LOCALE = {
               'ko'     : 'kr',
             }

    def getRSS(self, language, topic=None):
        return feedparser.parse(self.TEMPLATE % {'territory' : self.LOCALE[language],
                                                 'language'  : language,
                                                  'topic'    : topic is None and self.FEED_TOPIC[choice(self.getTopics())] or self.FEED_TOPIC[topic]
                                                 })
    def getTopics(self):
        return self.FEED_TOPIC.keys()
  
    def getLocale(self):
        return self.LOCALE.keys()
