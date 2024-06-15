import requests


class CardApi:
    def __init__(self, base_url: str, key: str, token: str) -> None:
        self.base_url = base_url
        self.key = key
        self.token = token

    def get_all_cards_by_board_id(self, board_id: str) -> list:
        path = "{trello}/boards/{id}/cards".format(trello=self.base_url, id=board_id)

        query = {
            "key": self.key,
            "token": self.token,
        }

        resp = requests.get(path, params=query)

        return resp.json()

    def create_card(self, name, id_list: str) -> dict:
        body = {
            "name": name,
            "idList": id_list,
            "key": self.key,
            "token": self.token,
        }

        path = "{trello}/cards/".format(trello=self.base_url)

        resp = requests.post(path, json=body)

        return resp.json()

    def create_a_new_label(self, card_id: str, color) -> dict:
        path = "{trello}/cards/{id}/labels".format(trello=self.base_url, id=card_id)

        body = {
            "color": color,
            "key": self.key,
            "token": self.token,
        }

        resp = requests.post(path, params=body)

        return resp.json()

    def update_card_by_id(self, card_id: str, id_list: str) -> dict:
        path = "{trello}/cards/{id}".format(trello=self.base_url, id=card_id)

        body = {
            "idList": id_list,
            "key": self.key,
            "token": self.token,
        }

        resp = requests.put(path, params=body)

        return resp.json()

    def delete_card_by_id(self, card_id: str):
        path = "{trello}/cards/{id}".format(trello=self.base_url, id=card_id)

        query = {
            "key": self.key,
            "token": self.token,
        }

        resp = requests.delete(path, params=query)

        return resp.json()
