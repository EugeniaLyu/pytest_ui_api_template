from api.BoardApi import BoardApi
from api.CardApi import CardApi

# import pytest


# @pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict, test_data: dict):
    board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    resp = api_client.create_board("Тестовая доска для удаления")
    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    assert len(board_list_after) - len(board_list_before) == 1


# @pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str, test_data: dict):
    board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    assert len(board_list_before) - len(board_list_after) == 1


# @pytest.mark.skip
def test_create_card(
    api_client: BoardApi, api_client_card: CardApi, dummy_board_id: str
):
    card_list_before = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    id_list = api_client.get_all_lists_by_board_id(dummy_board_id)

    api_client_card.create_card("Тестовая карточка", id_list)

    card_list_after = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    api_client.delete_board_by_id(dummy_board_id)

    assert len(card_list_after) - len(card_list_before) == 1


# @pytest.mark.skip
def test_create_a_new_label(
    api_client: BoardApi, api_client_card: CardApi, dummy_board_id: str
):
    color = "green"

    id_list = api_client.get_all_lists_by_board_id(dummy_board_id)

    card = api_client_card.create_card("Тестовая карточка", id_list)
    id_card = card["id"]

    new_label = api_client_card.create_a_new_label(id_card, color)

    api_client.delete_board_by_id(dummy_board_id)

    assert new_label["color"] == color


# @pytest.mark.skip
def test_update_card(
    api_client: BoardApi, api_client_card: CardApi, dummy_board_id: str
):
    id_list = api_client.get_all_lists_by_board_id(dummy_board_id)

    card = api_client_card.create_card("Тестовая карточка", id_list)
    id_card = card["id"]

    new_list = api_client.create_list_by_board_id("Тестовый лист", dummy_board_id)
    id_list = new_list["id"]

    update_card = api_client_card.update_card_by_id(id_card, id_list)

    assert update_card["idList"] == new_list["id"]


# @pytest.mark.skip
def test_delete_card(
    api_client: BoardApi, api_client_card: CardApi, dummy_board_id: str
):
    id_list = api_client.get_all_lists_by_board_id(dummy_board_id)

    card = api_client_card.create_card("Тестовая карточка", id_list)
    id_card = card["id"]

    card_list_before = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    api_client_card.delete_card_by_id(id_card)

    card_list_after = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    assert len(card_list_before) - len(card_list_after) == 1
