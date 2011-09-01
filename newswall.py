import cgi
import feedparser

from tile import TileBox
from view import TileView
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/newswall" method="post">
                <div><input type="text" name="rss_feed" size="30" /></div>
                <div><input type="submit" value="Submit RSS Feed"></div>
              </form>
            </body>
          </html>""")

class FeedBox(webapp.RequestHandler):
    def post(self):
        view = TileView()
        rss  = feedparser.parse(self.request.get('rss_feed'))

        div_template = '<DIV class="box" id="%(id)"s style="%(div)s">%(title)s</DIV>\n'
        self.response.out.write(view.getTemplate('header'))
        self.response.out.write(view.getContents(rss.entries))
        self.response.out.write(view.getTemplate('footer'))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/newswall', FeedBox)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
