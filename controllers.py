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
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(data=data)
        if form.validate_on_submit():
            t = Teacher(name = form.name.data, surname = form.surname.data, clas = form.clas.data, science = form.science.data)
            t.save()
    return render_template('teacher.html',form=form)




@app.route('/student', methods=["GET","POST"])
def st():
    data = request.form
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(data=data)
        if form.validate_on_submit():
            
            print('fkdfefg')
            s = Student(name = form.name.data, surname = form.surname.data, age = form.age.data, clas = form.clas.data, science = form.science.data, school = form.school.data)
            s.save()
    return render_template('student.html',form=form)