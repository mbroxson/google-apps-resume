from main import *

class Section(db.Model):
    title = db.StringProperty(required=True)
    type = db.StringProperty(
                             required=True,
                             choices=set([
                                          "text",
                                          "short_desc",
                                          "simple_list",
                                          "list",
                                          "html"
                                          ])
                             )
    sub_title = db.StringProperty()
    text = db.StringProperty()
    items = db.StringListProperty()
    start_date = db.DateProperty()
    end_date = db.DateProperty()
    city = db.StringProperty()
    state = db.StringProperty()
