from app.config.environment import PontoPet as pontopet_config
import app.pontopet_lib.pontopet as pontopet_lib

def login(username, password):
    pontopet = pontopet_lib.PontoPet(pontopet_config.url, username, password)
    pontopet_auth = pontopet.authenticate()
    pontopet_key = None
    if 200 == pontopet_auth['status']:
        pontopet_key = pontopet_auth['content']

    return pontopet_key

def create(name, email, document, password, login):
    success = False

    try:
        # send to api
        success = True
    except:
        # log error
        pass
    finally:
        return success
