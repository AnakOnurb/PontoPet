import app.utils as utils

config = utils.load_json(relative_path='config.json')

class Logging:
    level: str = config["LogLevel"]