
from main import *
import create_personal_info
import create_section

class CreateDatabase(webapp.RequestHandler):
    def get(self):
        self.response.content_type = 'text/plain'
        self.response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        self.response.headers['Pragma'] = 'no-cache'
        self.response.headers['Expires'] = '0'
        self.response.write(create_personal_info.create() + '\n')
        self.response.write(create_section.create() + '\n')
