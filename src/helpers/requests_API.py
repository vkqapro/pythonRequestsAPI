import json

import requests
import logging as log


class ApiCalls:

    def POST(self, base_url, endpoint, query, headers=None, expected_status_code=200):
        if not headers:
            headers = {
                'Accept': "application/json"
            }
        r = requests.post(
            url=base_url+endpoint,
            headers=headers,
            params=query
        )
        assert r.status_code == expected_status_code
        return r

    def GET(self, base_url, endpoint, query, headers=None, expected_status_code=200):
        if not headers:
            headers = {
                'Accept': 'application/json'
            }
        r = requests.get(
            url=base_url+endpoint,
            headers=headers,
            params=query
        )
        assert r.status_code == expected_status_code
        return r


    def DELETE(self, base_url, endpoint, query, headers=None, expected_status_code=200):
        if not headers:
            headers = {
                'Accept': 'application/json'
            }
        r = requests.delete(
            url=base_url+endpoint,
            headers=headers,
            params=query
        )
        assert r.status_code == expected_status_code
        return r

    def PUT(self, base_url, endpoint, query, headers=None, expected_status_code=200):
        if not headers:
            headers = {
                'Accept': 'application/json'
            }
        r = requests.put(
            url=base_url+endpoint,
            headers=headers,
            params=query
        )
        assert r.status_code == expected_status_code
        return r
