import requests, json, logging

class PontoPet():
    def __init__(self, api_base_url, username, password):
        api_complement_url = "/services/auth/login"
        self.api_url = api_base_url + api_complement_url
        self.username = username
        self.password = password


    def authenticate(self):
        url = self.api_url

        headers = {
            "Content-Type": "application/json"
        }

        params = {

        }

        payload = ""

        response = requests.post(url, headers=headers, params=params, data=payload, verify=False)

        return_val = {}
        return_val['status'] = response.status_code

        if 200 == response.status_code:
            return_val['content'] = response.content
        else:
            return_val['content'] = response

        return return_val