
import cgi
import wsgiref.handlers
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    self.response.out.write("""
        <html><body>
        <form method="post" action="/new_location?imei=1&rmc=2">
	IMEI:<input type="text" name="imeii" value="357248015263000"></input><br/>
	RMC :<input type="text" name="rmc" value="$GPRMC,AUTO"></input><br/>
        <input type="submit" value="enter"></input>
        </form>
        </body></html>""")

class FormTest(webapp.RequestHandler):
  def post(self):
    self.response.out.write('<html><body>POST Field:<br/>')
    self.response.out.write('imei: ' + cgi.escape(self.request.get('imeii')) + '<br/>')
    self.response.out.write('rmc: ' + cgi.escape(self.request.get('rmc')) + '<br/>')
    self.response.out.write('<br/> GET Field: <br/>')
    self.response.out.write('imei: ' + cgi.escape(self.request.get('imei')) + '<br/>' )
    self.response.out.write('rmc: ' + cgi.escape(self.request.get('rmc')) + '<br/>' )
    self.response.out.write('</body></html>')           

def main():
  application = webapp.WSGIApplication(
                                       [('/', MainPage),
                        ('/new_location', FormTest)
                       ],
                                       debug=True)

  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main() 
