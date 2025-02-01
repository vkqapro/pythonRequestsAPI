import os
from dotenv import load_dotenv

class Credentials:
    load_dotenv()
    def key(self):
        APIKEY = os.environ.get('APIKEY')
        return APIKEY

    def token(self):
        APITOKEN = os.environ.get('APITOKEN')
        return APITOKEN