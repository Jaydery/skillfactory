import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Неявное ожидание в 10 секунд

    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()


def test_pets(driver):
    # Проверка явного ожидания для поля email
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))

    # Вводим email и password нажимаем на кнопку Войти
    driver.find_element(By.ID, 'email').send_keys('ewrhzdfbh@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('123qwe')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ожидаем вход на главную страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Получаем питомцев
    pet_cards = driver.find_elements(By.CSS_SELECTOR, 'div.card')

    # Проверяем наличие питомцев
    assert len(pet_cards) > 0, "Не найдено ни одного питомца"

    for card in pet_cards:
        # Явные ожидания для элементов питомца
        WebDriverWait(card, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img'))
        )
        WebDriverWait(card, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h5'))
        )


def test_my_pets(driver):
    # Вводим email и password нажимаем на кнопку Войти
    driver.find_element(By.ID, 'email').send_keys('ewrhzdfbh@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('123qwe')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Переходим на страницу "Мои питомцы"
    driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    # Явное ожидание для таблицы питомцев
    WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table'))
    )

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', "Изображение питомца отсутствует"
        assert names[i].text != '', "Имя питомца отсутствует"
        assert descriptions[i].text != '', "Описание питомца отсутствует"
        assert ', ' in descriptions[i].text, "Описание питомца должно содержать запятую"

        parts = descriptions[i].text.split(", ")
        assert len(parts) == 2, "Описание питомца должно содержать два элемента"
        assert len(parts[0]) > 0, "Первый элемент описания пуст"
        assert len(parts[1]) > 0, "Второй элемент описания пуст"