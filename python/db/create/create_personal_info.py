import personal_info

def create():
    query = personal_info.PersonalInfo.all()
    if query.count() == 0:
        PI = personal_info.PersonalInfo(
                                        first_name="Mitchell",
                                        middle_name="Ryan",
                                        last_name="Broxson",
                                        address="202 Wooddale St.",
                                        city="Maryville",
                                        state="TN",
                                        zip="37801",
                                        phone="(865) 300-3618",
                                        email="mitchellbroxson@gmail.com"
                                        )
        PI.put()
        return "Created PersonalInfo"
    return "PersonalInfo already exists"
