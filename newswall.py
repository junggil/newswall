import cgi

from tile import TileBox
from view import TileView
from feeder import GoogleNews
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class FeedBox(webapp.RequestHandler):
    def get(self):
        view = TileView()
        rss  = GoogleNews().getRSS('ko')
        div_template = '<DIV class="box" id="%(id)"s style="%(div)s">%(title)s</DIV>\n'
        self.response.out.write(view.getTemplate('header'))
        self.response.out.write(view.getContents(rss.entries))
        self.response.out.write(view.getTemplate('footer'))

application = webapp.WSGIApplication(
                                     [('/', FeedBox)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
