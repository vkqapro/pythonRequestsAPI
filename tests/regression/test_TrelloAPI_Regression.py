import allure

from tests.BaseTest import BaseTest

import pytest
import allure_pytest
import logging as log
import json


base_url = "https://api.trello.com/1/"
endpoint_boards = "boards"
endpoint_cards = "cards"
board_data_root = 'tests/test_data/board_data.txt'

@allure.suite('Trello API Regression - Python Requests with Pytest and Allure reports')
@pytest.mark.TC000
class TestTrelloRegressionAPI(BaseTest):
    @allure.title('Create a board')
    @pytest.mark.TC001
    def test_create_board(self):
        query = {
            'name': "NewBoardAPI",
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }
        #### Create a new board #####
        result = self.API_CALL.POST(
            base_url=base_url,
            endpoint=endpoint_boards,
            query=query
        )
        result = result.json()
        self.new_board_id = result['id']
        with open(board_data_root, 'w') as file:
            file.write(self.new_board_id)

        #### Verify that the board is created ####
        query = {
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }
        result = self.API_CALL.GET(
            base_url=base_url,
            endpoint=f"{endpoint_boards}/{self.new_board_id}",
            query=query
        )
        result = result.json()
        assert result["id"] == self.new_board_id

    @allure.title('Create a list')
    @pytest.mark.TC002
    def test_create_list(self):
        new_list_name = 'NewAPIList'
        with open(board_data_root, 'r') as file:
            board_id = file.read()
        query = {
            'name': new_list_name,
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }

        response = self.API_CALL.POST(
            base_url=base_url,
            endpoint=f"{endpoint_boards}/{board_id}/lists",
            query=query
        )
        board_data = response.json()
        assert board_data['name'] == new_list_name
        data = {
            'list_id': board_data['id'],
            'board_id': board_data['idBoard'],
            'list_name': board_data['name']
        }
        with open(board_data_root, 'w') as f:
            json.dump(data, f, indent=4)


    @allure.title('Create a card')
    @pytest.mark.TC003
    def test_card_creation(self):
        with open(board_data_root, "r") as f:
            data = json.loads(f.read())
        query = {
            'idList': data['list_id'],
            'name': 'new_card',
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }

        response = self.API_CALL.POST(
            base_url,
            endpoint=endpoint_cards,
            query=query
        )
        card_data = response.json()
        # log.info(card_data)
        data['card_id'] = card_data['id']
        with open(board_data_root, 'w') as file:
            json.dump(data, file, indent=4)

    @allure.title('Drag a card from one list to another list')
    @pytest.mark.TC004
    def test_drag_drop_card(self):
        new_list_name = 'NewAPIList_2'
        with open(board_data_root, 'r') as file:
            board_data = json.loads(file.read())

        # creating a new list "NewAPIList_2"
        query_2 = {
            'name': new_list_name,
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }

        response = self.API_CALL.POST(
            base_url=base_url,
            endpoint=f"{endpoint_boards}/{board_data['board_id']}/lists",
            query=query_2
        )
        res_data = response.json()

        # adding new list ID to the file board_data.txt
        board_data['list_2_id'] = res_data['id']
        with open(board_data_root, 'w') as file:
            json.dump(board_data, file, indent=4)

        drag_n_drop_data = {
            'card_id': board_data['card_id'],
            'second_list_id': res_data['id']
        }

        query_3 = {
            'idList': drag_n_drop_data['second_list_id'],
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }

        response = self.API_CALL.PUT(
            base_url=base_url,
            endpoint=f"{endpoint_cards}/{drag_n_drop_data['card_id']}",
            query=query_3
        )

    @allure.title('Add "GREEN" label to the card')
    @pytest.mark.TC005
    def test_add_label_to_card(self):
        with open(board_data_root, 'r') as f:
            board_data = json.loads(f.read())

        query_post_new_label = {
            'color': 'green',
            'title': 'New label',
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }
        res = self.API_CALL.POST(
            base_url=base_url,
            endpoint=f"{endpoint_cards}/{board_data['card_id']}/labels",
            query=query_post_new_label
        )

    @allure.title('Archive the card')
    @pytest.mark.TC006
    def test_archive_card(self):
        with open(board_data_root, 'r') as file:
            board_data = json.load(file)

        query_card_deletion = {
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }
        response = self.API_CALL.DELETE(
            base_url=base_url,
            endpoint=f"{endpoint_cards}/{board_data['card_id']}",
            query=query_card_deletion
        )

    @allure.title('Delete the board')
    @pytest.mark.TC007
    def test_delete_board(self):
        with open(board_data_root, 'r') as f:
            board_data = json.loads(f.read())
        query = {
            'key': self.CREDENTIALS.key(),
            'token': self.CREDENTIALS.token()
        }
        response = self.API_CALL.DELETE(
            base_url=base_url,
            endpoint=f"{endpoint_boards}/{board_data['board_id']}",
            query=query
        )








