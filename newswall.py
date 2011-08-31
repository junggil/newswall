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
        rss  = feedparser.parse(self.request.get('rss_feed'))
        divs = TileView().getDivs()
        self.response.out.write('<html><body>%(title)s\n' % {'title' : rss.feed.title})
        for i, div in enumerate(divs):
            try:
                self.response.out.write('<div style="%(div)s">%(title)s</div>\n' % {'div' : div, 'title' : rss.entries[i].title})
            except:
                self.response.out.write('<div style="%(div)s">%(title)s</div>\n' % {'div' : div, 'title' : 'News-Wall Demo'})
        self.response.out.write('</body></html>')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/newswall', FeedBox)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
