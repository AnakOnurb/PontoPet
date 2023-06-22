from flask import Blueprint, render_template, request, url_for, flash, redirect, session
import app.utils.messages as messages

user_blueprint = Blueprint('user',__name__)

@user_blueprint.route("/profile", methods=['GET', 'POST'])
def profile():
    if 'POST' == request.method:        
        name = request.form['name']
        document = request.form['document']
        login = request.form['login']
        password = request.form['password']
        if not name or not document or not login or not password:
            flash(messages.register_missing_info)
        print('NOME: ' + name)

    #get user info
    return render_template('user/profile.html', username=session['username'])

@user_blueprint.route("/timesheet", methods=['GET', 'POST'])
def timesheet():
    if 'POST' == request.method:        
        pass

    return render_template('user/timesheet.html')