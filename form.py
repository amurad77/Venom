from flask_wtf import FlaskForm
from flask import Flask
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class Teacher_form(FlaskForm):
    name = StringField(label='name:', validators=[DataRequired(), Length(min=3, max=20)]) 
    surname = StringField(label='surname:', validators=[DataRequired(), Length(min=3, max=30)])
    clas = StringField(label='class:', validators=[DataRequired(), Length(min=3, max=30)])
    science = StringField(label='science', validators=[DataRequired(), Length(min=3, max=30)])

class Student_form(FlaskForm):
    name = StringField(label='name:', validators=[DataRequired(), Length(min=3, max=20)]) 
    surname = StringField(label='surname:', validators=[DataRequired(), Length(min=3, max=30)])
    age = StringField(label='age:', validators=[DataRequired(), Length(min=3, max=30)])
    clas = StringField(label='class', validators=[DataRequired(), Length(min=3, max=30)])
    science = StringField(label='science:', validators=[DataRequired(), Length(min=3, max=20)]) 
    school = StringField(label='school:', validators=[DataRequired(), Length(min=3, max=30)])