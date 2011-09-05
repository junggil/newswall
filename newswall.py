import cgi

from tile import TileBox
from view import TileView
from feeder import GoogleNews
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class FeedBox(webapp.RequestHandler):
    def get(self):
        locale, topic = ('ko', 'POPULAR')
        viewer = TileView(locale)
        feeder = GoogleNews(locale)
        div_template = '<DIV class="box" id="%(id)"s style="%(div)s">%(title)s</DIV>\n'
        self.response.out.write(viewer.getTemplate('header'))
        self.response.out.write(viewer.getContents(feeder.getRSS(topic), topic))
        self.response.out.write(viewer.getTopics(feeder.getAllTopics()))
        self.response.out.write(viewer.getLogos())
        self.response.out.write(viewer.getTemplate('footer'))

application = webapp.WSGIApplication(
                                     [('/', FeedBox)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
