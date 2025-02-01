from src.helpers.requests_API import ApiCalls
from src.credentials.credentials import Credentials

import pytest
class BaseTest:
    API_CALL: ApiCalls
    CREDENTIALS: Credentials
    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.API_CALL = ApiCalls()
        request.cls.CREDENTIALS = Credentials()


