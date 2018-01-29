from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime
from google.appengine.ext import db

import os
import sys
import jinja2

sys.path.append(os.path.dirname(__file__))
for dirname in [os.path.join(dp, d) for dp, dn, fn in os.walk(os.path.dirname(__file__)) for d in dn]:
    if os.path.isdir(os.path.join(os.path.dirname(__file__), dirname)) and os.path.join(os.path.dirname(__file__), dirname) not in sys.path:
        sys.path.append(os.path.join(os.path.dirname(__file__), dirname))


import personal_info
import section

jinja_env = jinja2.Environment(
                               loader=jinja2.FileSystemLoader(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))),
                               extensions=['jinja2.ext.autoescape'],
                               autoescape=False
                               )
base_tpl_data = {
                 'program': 'resume.mitchellbroxson.com'
                 }

application = webapp.WSGIApplication([
                                      ('/CreateDatabase', "create_all.CreateDatabase"),
                                      ('/', "home.HomePage")
                                      ], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
