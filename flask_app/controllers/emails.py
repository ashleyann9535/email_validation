from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import email

# put in routes
@app.route('/')
def home():
    return render_template('index.html')

#Create 
@app.route('/create', methods = ['POST'])
def create():
    if not email.Email.validate_email(request.form):
        return redirect('/')

    email.Email.create_email(request.form)
    return redirect('/read_all')

#Read 
@app.route('/read_all')
def read_all():
    these_emails = email.Email.read_all_emails()
    return render_template('view_emails.html', these_emails = these_emails)
#Update 


#Delete 
@app.route('/delete/<int:id>')
def delete_email(id):
    email.Email.delete_user(id)
    return redirect('/read_all')