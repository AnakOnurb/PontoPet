import app.utils.utils as utils

config = utils.load_json(relative_path='config.json')

class Logging:
    level: str = config["LogLevel"]

class PontoPet:
    url: str = config["PontoPetURL"]
    port: str = config["PontoPetPort"]