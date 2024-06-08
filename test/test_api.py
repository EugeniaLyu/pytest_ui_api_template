from api.BoardApi import BoardApi
from api.CardApi import CardApi


def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("66559c2033e4c31c75f3cadf")

    resp = api_client.create_board("Тестовая доска для удаления")
    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id("66559c2033e4c31c75f3cadf")

    assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id("66559c2033e4c31c75f3cadf")

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id("66559c2033e4c31c75f3cadf")

    assert len(board_list_before) - len(board_list_after) == 1


def test_create_card(
    api_client: BoardApi, api_client_card: CardApi, dummy_board_id: str
):
    card_list_before = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    id_list = api_client.get_all_lists_by_board_id(dummy_board_id)

    api_client_card.create_card("Тестовая карточка", id_list)

    card_list_after = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    api_client.delete_board_by_id(dummy_board_id)

    assert len(card_list_after) - len(card_list_before) == 1


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


def test_delete_card(
    api_client: BoardApi, api_client_card: CardApi, dummy_board_id: str
):

    card_list_before = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    id_list = api_client.get_all_lists_by_board_id(dummy_board_id)

    card = api_client_card.create_card("Тестовая карточка", id_list)
    id_card = card["id"]

    api_client_card.delete_card_by_id(id_card)

    card_list_after = api_client_card.get_all_cards_by_board_id(dummy_board_id)

    assert len(card_list_before) - len(card_list_after) == 1
