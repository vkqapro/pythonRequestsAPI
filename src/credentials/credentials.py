import os
from dotenv import load_dotenv

class Credentials:
    load_dotenv()
    def key(self):
        APIKey = os.environ.get('APIKEY')
        return APIKey

    def token(self):
        APIToken = os.environ.get('APITOKEN')
        return APIToken