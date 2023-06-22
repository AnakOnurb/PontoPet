from a2wsgi import ASGIMiddleware
from flask import Flask, render_template, request, url_for, flash, redirect, session
from app.routes.root import root_blueprint
from app.routes.user import user_blueprint
from app.routes.management import management_blueprint
from datetime import timedelta

app = Flask(__name__, template_folder='pages', static_folder='static')
app.config['SECRET_KEY'] = 'alongrandomstringtosecretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

app.register_blueprint(root_blueprint)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(management_blueprint, url_prefix='/management')

@app.before_request
def before_request_func():
    print(session)
    if 'logged_in' not in session:
        session['logged_in'] = False
        return redirect(url_for('root.index'))

wsgi_app = ASGIMiddleware(app)