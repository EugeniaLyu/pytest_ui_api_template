from page.AuthPage import AuthPage
from page.MainPage import MainPage


def auth_test(browser):
    email = "ximonix338@javnoi.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "Solo41pharM62@")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert auth_page.get_current_url().endswith("user76369519/boards")
    assert info[0] == "Евгения"
    assert info[1] == email
