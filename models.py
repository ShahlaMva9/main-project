from run import db
class Persoinfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    title_icon=db.Column(db.String(50))
    title_content=db.Column(db.String(50))

class Experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    job_title=db.Column(db.String(50))
    company=db.Column(db.String(50))
    job_date=db.Column(db.String(50))
    job_content=db.Column(db.String(250))

class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education_title=db.Column(db.String(50))
    university_name=db.Column(db.String(50))
    education_date=db.Column(db.String(50))
    education_content=db.Column(db.String(250))
class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_name=db.Column(db.String(50))
    skill_rate1=db.Column(db.String(50))
    skill_rate2=db.Column(db.String(50))
    skill_rate3=db.Column(db.String(50))
    skill_rate4=db.Column(db.String(50))
    skill_rate5=db.Column(db.String(50))

class Myexperience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    experience_year=db.Column(db.String(50))
    doneproject=db.Column(db.String(50))
    happycustomers=db.Column(db.String(50))

class Image(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    image=db.Column(db.String(100))