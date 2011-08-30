import cgi
import feedparser

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


class FeedPage(webapp.RequestHandler):
    def post(self):
        try:
            rss = feedparser.parse(self.request.get('rss_feed'))
            self.response.out.write('<html><body>' + rss.feed.title)
            self.response.out.write('<ul>')
            for feed in rss.entries:
                self.response.out.write('<li>' + feed.title)
                if feed.get('summary', None):
                    self.response.out.write('<ul><li><a href="' + feed.link + '">' + feed.summary + '</a></ul>')
            self.response.out.write('</ul>')
            self.response.out.write('</body></html>')
        except:
            self.response.out.write('Invalid Feed')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/newswall', FeedPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
