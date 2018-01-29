from main import *

class PersonalInfo(db.Model):
    first_name = db.StringProperty(required=True)
    middle_name = db.StringProperty()
    last_name = db.StringProperty(required=True)
    address = db.StringProperty()
    city = db.StringProperty()
    state = db.StringProperty()
    zip = db.StringProperty()
    phone = db.StringProperty()
    email = db.StringProperty()
