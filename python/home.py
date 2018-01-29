from main import *

class HomePage(webapp.RequestHandler):
    def get(self):
        tpl_data = base_tpl_data.copy()
        tpl_data['PersonalInfo'] = personal_info.PersonalInfo.all().fetch(1)[0]
        tpl_data['section_order'] = ['OBJECTIVE', 'EDUCATION', 'SKILLS', 'EXPERIENCE', 'CODE EXAMPLES']
        tpl_data["sections"] = {
                                'OBJECTIVE': section.Section.all().filter('title =', 'OBJECTIVE').order('-start_date').fetch(100),
                                'EDUCATION': section.Section.all().filter('title =', 'EDUCATION').order('-start_date').fetch(100),
                                'SKILLS': section.Section.all().filter('title =', 'SKILLS').order('-start_date').fetch(100),
                                'EXPERIENCE': section.Section.all().filter('title =', 'EXPERIENCE').order('-start_date').fetch(100),
                                'CODE EXAMPLES': section.Section.all().filter('title =', 'CODE EXAMPLES').order('-start_date').fetch(100),
                                }
        self.response.write(jinja_env.get_template('resume.htm').render(tpl_data))
