from model import *
from flask import render_template, request
from form import *
from flask import Flask

from app import app


@app.route('/home')
def home():
    return render_template('index.html')




@app.route('/teacher', methods=["GET","POST"])
def tc():
    data = request.form
    form = Teacher_form()
    if request.method == 'POST':
        form = Teacher_form(data=data)
        if form.validate_on_submit():
            t = Teacher(name = form.name.data, surname = form.surname.data, clas = form.clas.data, science = form.science.data)
            t.save()
    return render_template('teacher.html',form=form)




@app.route('/student', methods=["GET","POST"])
def st():
    data = request.form
    form = Student_form()
    if request.method == 'POST':
        form = Student_form(data=data)
        if form.validate_on_submit():
            s = Student(name = form.name.data, surname = form.surname.data, age = form.age.data, clas = form.clas.data, science = form.science.data, school = form.school.data)
            s.save()
    return render_template('student.html',form=form)