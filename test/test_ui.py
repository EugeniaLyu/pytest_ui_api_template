import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage
from page.BoardPage import BoardPage


def auth_test(browser):
    email = "ximonix338@javnoi.com"
    password = "Solo41pharM62@"
    username = "Евгения"
    title_board = "Тестовая доска"
    text = """Эта доска закрыта. Чтобы изменить доску, ее нужно открыть.
Открыть доску заново"""
    title_card = "Тестовая карточка"
    color = "rgba(33, 110, 78, 1)"

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

    board_page = BoardPage(browser)
    board_page.create_board(title_board)
    info = board_page.get_board_info()

    with allure.step("Проверить данные новой доски"):
        with allure.step("Имя доски должно быть " + title_board):
            assert info == title_board

    board_page.add_card(title_card)
    info = board_page.get_card_info()

    with allure.step("Проверить данные карточки"):
        with allure.step("Должна быть строка " + title_card):
            assert info == title_card

    board_page.update_card()
    # info = board_page.get_color_label_info()

    # with allure.step("Проверить цвет метки"):
    #     with allure.step("Должен быть цвет " + color):
    #         assert info == color

    board_page.delete_board()
    info = board_page.get_close_board_info()

    with allure.step("Проверить, что доска закрылась"):
        with allure.step("Должна быть строка " + text):
            assert info == text
