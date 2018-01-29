import section
import datetime

def create():
    section_attributes = ["title", "type", "sub_title", "text", "items", "start_date", "end_date", "city", "state"]
    sections = [
                { "title": "OBJECTIVE", "type": "text", "text": "To further my knowledge in software development field in order to improve myself and my employer." },
                
                { "title": "EDUCATION", "type": "short_desc", "sub_title": "Florida Institute of Technology", "text": "Master of Science in Information Technology", "start_date": datetime.date(year=2013, month=3, day=1), "end_date": datetime.date(year=2015, month=5, day=1), "city": "Melbourne", "state": "FL" },
                { "title": "EDUCATION", "type": "short_desc", "sub_title": "Florida Institute of Technology", "text": "Bachelor of Science in Computer Information Systems", "start_date": datetime.date(year=2009, month=7, day=1), "end_date": datetime.date(year=2012, month=12, day=21), "city": "Melbourne", "state": "FL" },
                { "title": "EDUCATION", "type": "short_desc", "sub_title": "Pellissippi State Technical Community College", "text": "Associate of Applied Science in Computer Science and Information Technology\\nProgramming Concentration", "start_date": datetime.date(year=2007, month=8, day=26), "end_date": datetime.date(year=2009, month=5, day=1), "city": "Knoxville", "state": "TN" },
                
                { "title": "SKILLS", "type": "simple_list", "sub_title": "Programming Languages", "text": "", "items": ["HTML", "JavaScript", "CSS", "Python", "C", "PHP", "Java", "Shell", "AWK", "Perl", "AutoHotKey"], 'start_date': datetime.date(year=2014, month=1, day=4) },
                { "title": "SKILLS", "type": "simple_list", "sub_title": "Databases", "text": "", "items": ["c-tree", "MSSQL", "MySQL", "PostgreSQL", "MS Access", "Mongo"], 'start_date': datetime.date(year=2014, month=1, day=3) },
                { "title": "SKILLS", "type": "simple_list", "sub_title": "Environments", "text": "", "items": ["Linux", "Windows", "All major browsers"], 'start_date': datetime.date(year=2014, month=1, day=2) },
                { "title": "SKILLS", "type": "simple_list", "sub_title": "Servers", "text": "", "items": ["Google App Engine", "SVN", "SSH", "SFTP", "FTP", "SAMBA"], 'start_date': datetime.date(year=2014, month=1, day=1) },
                
                { "title": "EXPERIENCE", "type": "list", "sub_title": "QRS, Inc.", "text": "Lead Product Developer", "items": ["Lead developer of web based Electronic Medical Records software", "Led development efforts to successfully obtain 2014 ONC HIT Certification", "Leading efforts to move the software backend to a modern environment", "Evaluated and integrated open and closed source libraries/products", "Tier-III support", "Internal systems development", "Indirectly manage EHR development team", "Indirectly manage interface/data conversion team"], "start_date": datetime.date(year=2012, month=12, day=1), "city": "Knoxville", "state": "TN" },
                { "title": "EXPERIENCE", "type": "list", "sub_title": "QRS, Inc.", "text": "Intermediate Software Developer", "items": ["Coordinated seamless system integration with 3rd party systems", "Tier-II support", "Oversee interface implementations", "Oversee data conversion processes"], "start_date": datetime.date(year=2011, month=3, day=1), "end_date": datetime.date(year=2012, month=12, day=1), "city": "Knoxville", "state": "TN" },
                { "title": "EXPERIENCE", "type": "list", "sub_title": "QRS, Inc.", "text": "Entry Level Developer", "items": ["Develop and maintain interfaces with other software", "Data conversions from previous software for new clients", "Interface support", "Tier-II support"], "start_date": datetime.date(year=2009, month=6, day=9), "end_date": datetime.date(year=2011, month=3, day=1), "city": "Knoxville", "state": "TN" },
                { "title": "EXPERIENCE", "type": "list", "sub_title": "Goody's Family Clothing", "text": "Helpdesk Technician", "items": ["Tier-I support", "Resolved support issues for PCs, Servers, and POS systems for over 300 stores", "Resolved support issues for PC and software for over 500 corporate users"], "start_date": datetime.date(year=2008, month=11, day=28), "end_date": datetime.date(year=2009, month=1, day=12), "city": "Knoxville", "state": "TN" },
                
                { "title": "CODE EXAMPLES", "type": "html", "text": "As you can see above, I have been working while continuing my education.  Unfortunately, this has not left time to work on open source projects in my personal time.", 'start_date': datetime.date(year=2014, month=1, day=3) },
                { "title": "CODE EXAMPLES", "type": "html", "text": "The best I can give right now would be the source code to this site. I will be updating this site as I continue my career search, so please check back to see improvements. <a href='/files/src.zip'>Download Now</a>", 'start_date': datetime.date(year=2014, month=1, day=2) },
                { "title": "CODE EXAMPLES", "type": "html", "text": "Please contact me if you would like to request specific code examples.", 'start_date': datetime.date(year=2014, month=1, day=1) },
                ]
    for sec in sections:
        query = section.Section.all()
        for att in section_attributes:
            if att in sec and att != 'items':
                query.filter(att + ' =', sec[att])
        if query.count() == 0:
            S = section.Section(title=sec['title'], type=sec['type'])
            for att in section_attributes:
                if att in sec:
                    S.__setattr__(att, sec[att])
            S.put()
    return "Done with sections"
