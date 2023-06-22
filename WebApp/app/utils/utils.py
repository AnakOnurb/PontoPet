import datetime
import json
from os import path

_root_path = path.join(path.dirname(__file__), "..")

def get_root_path():
    return _root_path

def get_current_datetime():
    return datetime.datetime.now()

def get_current_datetime_string(datetime_format = None):
    now = get_current_datetime()
    date_string = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    if None != datetime_format:
        date_string = str(now.strftime(datetime_format))

    return date_string

def get_current_date_string(date_format = None):
    now = get_current_datetime()
    date_string = str(now.strftime("%Y-%m-%d"))
    if None != date_format:
        date_string = str(now.strftime(date_format))

    return date_string

def get_current_time_string(time_format = None):
    now = get_current_datetime()
    date_string = str(now.strftime("%H:%M:%S"))
    if None != time_format:
        date_string = str(now.strftime(time_format))

    return date_string

def load_json(relative_path = None, absolute_path = None):
    if relative_path is None and absolute_path is None:
        raise TypeError('Relative or Absolute Path must be provided')
    
    file_path = absolute_path
    if None == file_path:
        file_path = path.join(get_root_path(), relative_path)
    
    if not path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write("{\n\n}")

    content = {}
    with open(file_path, 'r') as file:
        content = json.load(file)

    return content