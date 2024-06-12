import requests


class BoardApi:
    def __init__(self, base_url: str, key: str, token: str) -> None:
        self.base_url = base_url
        self.key = key
        self.token = token

    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = "{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards".format(
            trello=self.base_url, id=org_id
        )

        query = {
            "key": self.key,
            "token": self.token,
        }
        resp = requests.get(path, params=query)

        return resp.json().get("boards")

    def get_all_lists_by_board_id(self, id: str) -> list:
        path = "{trello}/boards/{board_id}/lists".format(
            trello=self.base_url, board_id=id
        )

        query = {
            "key": self.key,
            "token": self.token,
        }
        resp = requests.get(path, params=query)

        return resp.json()[0]["id"]

    def create_list_by_board_id(self, name: str, board_id: str) -> list:
        path = "{trello}/lists".format(trello=self.base_url)

        query = {
            "name": name,
            "idBoard": board_id,
            "key": self.key,
            "token": self.token,
        }
        resp = requests.post(path, params=query)

        return resp.json()

    def create_board(self, name: str, default_list=True) -> dict:

        body = {
            "defaultLists": default_list,
            "name": name,
            "key": self.key,
            "token": self.token,
        }
        path = "{trello}/boards".format(trello=self.base_url)
        resp = requests.post(path, json=body)

        return resp.json()

    def delete_board_by_id(self, id: str):
        query = {
            "key": self.key,
            "token": self.token,
        }
        path = "{trello}/boards/{board_id}".format(trello=self.base_url, board_id=id)
        resp = requests.delete(path, params=query)

        return resp.json()

