from flask import Blueprint, render_template, request, url_for, flash, redirect, session
import app.utils.messages as messages
import app.core.user as user

root_blueprint = Blueprint('root',__name__)

@root_blueprint.route("/")
def index():      
    return render_template('index.html')

@root_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if 'POST' == request.method:        
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash(messages.login_missing_info)
        else:
            #auth_key = user.login(username, password)
            auth_key = '111'
            #if None != auth_key:
            if 1 == 1:
                session.permanent = True
                session.modified = True
                session['logged_in'] = True
                session['auth_key'] = auth_key
                session['username'] = username
                return redirect(url_for('user.timesheet'))
            else:
                flash(messages.login_failed)

    return render_template('login.html')

@root_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    if 'POST' == request.method:        
        name = request.form['name']
        document = request.form['document']
        login = request.form['login']
        password = request.form['password']
        if not name or not document or not login or not password:
            flash(messages.register_missing_info)
        else:
            
            return redirect(url_for('root.login'))

    return render_template('register.html')