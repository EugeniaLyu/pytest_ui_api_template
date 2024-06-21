import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage
from page.BoardPage import BoardPage

# import pytest


# @pytest.mark.skip
def auth_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")
    username = "Евгения"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step(
        "Проверить, что URL " + current_url + "заканчивается на user76369519/boards"
    ):
        assert current_url.endswith("user76369519/boards")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть " + email):
            assert info[1] == email


def board_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()

    title_board = "Тестовая доска 1"
    board_page = BoardPage(browser)
    board_page.create_board(title_board)
    info = board_page.get_board_info()

    with allure.step("Проверить данные новой доски"):
        with allure.step("Имя доски должно быть " + title_board):
            assert info == title_board


def card_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    board_page = BoardPage(browser)

    title_card = "Тестовая карточка 1"
    board_page.add_card(title_card)
    info = board_page.get_card_info()

    with allure.step("Проверить данные карточки"):
        with allure.step("Должна быть строка " + title_card):
            assert info == title_card


def edit_card_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    #     text = """Эта доска закрыта. Чтобы изменить доску, ее нужно открыть.
    # Открыть доску заново"""
    board_page = BoardPage(browser)

    board_page.update_card()
    info = board_page.get_color_label_info()

    color = "rgba(33, 110, 78, 1)"
    with allure.step("Проверить цвет метки"):
        with allure.step("Должен быть цвет " + color):
            assert info == color


def drag_card_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    board_page = BoardPage(browser)

    board_page.drag_card()
    info = board_page.get_drag_card_name_info()

    title_card = "Тестовая карточка 1"
    with allure.step("Проверить, что карточка переместилась"):
        with allure.step(
            '"В процеесе" должен содержать карточку с названием' + title_card
        ):
            assert info == title_card


def delete_board_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    board_page = BoardPage(browser)

    board_page.delete_board()
    info = board_page.get_close_board_info()

    text = "Эта доска закрыта. Чтобы изменить доску, ее нужно открыть."
    with allure.step("Проверить, что доска закрылась"):
        with allure.step("Должна быть строка " + text):
            assert info == text
