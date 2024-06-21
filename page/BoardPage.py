import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BoardPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Создание новой доски {title}")
    def create_board(self, title: str):
        self.__driver.find_element(By.CSS_SELECTOR, "div.board-tile.mod-add").click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "input[data-testid=create-board-title-input]"
        ).send_keys(title)
        WebDriverWait(self.__driver, 2).until_not(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.AOsf5x5baMpD1a"))
        )
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]"
        ).click()

    @allure.step("Прочитать заголовок доски")
    def get_board_info(self) -> str:
        title = self.__driver.find_element(
            By.CSS_SELECTOR, "h1[data-testid=board-name-display]"
        ).text
        return title

    @allure.step("Удаление существующей доски")
    def delete_board(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, "div.board-tile-details.is-badged"
        ).click()
        self.__driver.find_element(By.CSS_SELECTOR, "div.jv7QDCKI8FPToj").click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "li>div.yhkRJjjbRlcC1Q>div.RNC8UUAwghG9uA>button>span"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "button.frrHNIWnTojsww.V1zfUmYP2wm_jb"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-testid=popover-close-board-confirm]"
        ).click()

    @allure.step("Прочитать информацию, что доска закрылась")
    def get_close_board_info(self) -> str:
        text = self.__driver.find_element(By.CSS_SELECTOR, "div.xJP6EH9jYQiWkk").text
        return text

    @allure.step("Добавление листа на доску")
    def add_list_name(self, title: str):
        self.__driver.find_element(
            By.CSS_SELECTOR, "textarea[data-testid=list-name-textarea]"
        ).send_keys(title)
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-testid=list-composer-add-list-button]"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "span[data-testid=CloseIcon]"
        ).click()

    @allure.step("Прочитать заголовк листа")
    def get_list_info(self) -> str:
        title = self.__driver.find_element(
            By.CSS_SELECTOR, "h2[data-testid=list-name]"
        ).text
        return title

    @allure.step("Добавление карточки на доску")
    def add_card(self, title: str):
        self.__driver.find_element(
            By.CSS_SELECTOR, "div.board-tile-details.is-badged"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-testid=list-add-card-button]"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "textarea[data-testid=list-card-composer-textarea]"
        ).send_keys(title)
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-testid=list-card-composer-add-card-button]"
        ).click()

    @allure.step("Прочитать заголовк карточки")
    def get_card_info(self) -> str:
        title = self.__driver.find_element(
            By.CSS_SELECTOR, "a[data-testid=card-name]"
        ).text
        return title

    @allure.step("Редактирование карточки")
    def update_card(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, "div.board-tile-details.is-badged"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "div[data-testid=trello-card]"
        ).click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "a[data-testid=card-back-labels-button]"
        ).click()
        self.__driver.find_element(By.CSS_SELECTOR, "span[data-color=green]").click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "span[data-testid=CloseIcon]"
        ).click()

    @allure.step("Проверить цвет метки")
    def get_color_label_info(self) -> str:
        label = self.__driver.find_element(
            By.CSS_SELECTOR, "span[data-testid=compact-card-label]"
        ).value_of_css_property("background-color")
        return label

    @allure.step("Перемещение карточки в другую колонку")
    def drag_card(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, "div.board-tile-details.is-badged"
        ).click()
        draggable = self.__driver.find_element(
            By.CSS_SELECTOR, "div[data-testid=trello-card]"
        )
        droppable = self.__driver.find_elements(
            By.CSS_SELECTOR, "div[data-testid=list]"
        )[1]
        ActionChains(self.__driver).drag_and_drop(draggable, droppable).perform()

    @allure.step("Проверить id перемещенной карточки")
    def get_drag_card_name_info(self) -> str:
        drag_card_name = self.__driver.find_element(
            By.CSS_SELECTOR,
            "div[data-testid=list]>ol>li>div>div>a[data-testid=card-name]",
        ).text
        return drag_card_name
