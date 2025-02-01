from tests.BaseTest import BaseTest

import pytest
import logging as log
import json

# url = "https://api.trello.com/1/members/me/boards"
base_url = "https://api.trello.com/1/"
endpoint = "boards"

class TestTrelloRegressionAPI(BaseTest):

    @pytest.mark.test
    def test_get_board(self):
        id = "6760f146b0b5cacf97136ce2"
        query = {
            # "id": "6760f146b0b5cacf97136ce2",
            "key": self.CREDENTIALS.key(),
            "token": self.CREDENTIALS.token()
        }

        result = self.API_CALL.GET(
            base_url=base_url,
            endpoint=f"{endpoint}/{id}",
            query=query
        )
        res = result.json()
        log.info(res['id'])
