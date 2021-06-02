from extensions import db
from datetime import datetime


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(201), nullable = True)
    surname = db.Column(db.String(201), nullable = True)
    clas = db.Column(db.String(201), nullable = True)  #class yazmadim cunki class yazanda ferqli sey hesab edir(deyesen)
    science = db.Column(db.String(201), nullable = True)


    def __repr__ (self):
        return self.name
    
    def __init__ (self, name, surname, clas, science):
        self.name = name
        self.surname = surname
        self.clas = clas
        self.science = science


    def save(self):
        db.session.add(self)
        db.session.commit()



class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(201), nullable = True)
    surname = db.Column(db.String(201), nullable = True)
    age = db.Column(db.Integer, nullable = True)
    clas = db.Column(db.String(201), nullable = True)
    science = db.Column(db.String(201), nullable = True)
    history = db.Column(db.DateTime)


    def __repr__ (self):
        return self.name

    def __init__ (self, name, surname, age, clas, science, history):
        self.name = name
        self.surname = surname
        self.age = age
        self.clas = clas
        self.science = science
        self.history = history

    def save(self):
        db.session.add(self)
        db.session.commit()