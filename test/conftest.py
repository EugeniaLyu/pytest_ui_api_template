import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.BoardApi import BoardApi

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi(
        "https://api.trello.com/1",
        "a9c159f465214bde276eb86d8140e0b7",
        "ATTAf39f231f0d7859becbad77974bc15277249040240cc55ccbe9f16bc1280a3ba25F6B5E71",
    )


@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "")


@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi(
        "https://api.trello.com/1",
        "a9c159f465214bde276eb86d8140e0b7",
        "ATTAf39f231f0d7859becbad77974bc15277249040240cc55ccbe9f16bc1280a3ba25F6B5E71",
    )
    resp = api.create_board("Доска для удаления").get("id")
    return resp


@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardApi(
        "https://api.trello.com/1",
        "a9c159f465214bde276eb86d8140e0b7",
        "ATTAf39f231f0d7859becbad77974bc15277249040240cc55ccbe9f16bc1280a3ba25F6B5E71",
    )
    api.delete_board_by_id(dictionary.get("board_id"))
