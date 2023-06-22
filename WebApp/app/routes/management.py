from flask import Blueprint, render_template, request, url_for, flash, redirect, session
import app.utils.messages as messages

management_blueprint = Blueprint('management',__name__)

@management_blueprint.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('management/dashboard.html')

@management_blueprint.route("/employees", methods=['GET'])
def employees():
    return render_template('management/employees.html')