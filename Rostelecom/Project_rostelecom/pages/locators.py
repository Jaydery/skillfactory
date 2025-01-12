from selenium.webdriver.common.by import By

class BaseLocators:
    body = (By.XPATH, "//body")

class AuthPageLocators:
    auth_heading = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    auth_logo = (By.XPATH, "//section[@id='page-left']/*/div[@class='what-is-container__logo-container']/*")
    auth_slogan = (By.XPATH, "//section[@id='page-left']/*//p[contains(text(),'Персональный помощник в цифровом мире " "Ростелекома')]")
    auth_tab_menu = (By.XPATH, "//section[@id='page-right']/*//div[@id='t-btn-tab-phone' or @id='t-btn-tab-mail' or " "@id='t-btn-tab-login' or @id='t-btn-tab-ls']")
    auth_username_input_placeholder_telephone = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
    auth_username_input = (By.XPATH, "//input[@id='username']")
    auth_username_input_activ_email = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
    auth_forgot_password_link = (By.XPATH, "//a[@id='forgot_password']")
    auth_register_link = (By.XPATH, "//a[@id='kc-register']")
    auth_user_agreement_link = (By.XPATH, "//span[contains(text(),'Нажимая кнопку «Войти», вы принимаете " "условия')]/following-sibling::a")
    auth_privacy_policy_link = (By.XPATH, "//*[@id='app-footer']/div[1]/div[2]/a[2]/span")
    auth_social_vk_link = (By.XPATH, "//*[@id='oidc_vk']")
    auth_tab_phone = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    auth_enter_button = (By.XPATH, "//button[@id='kc-login']")
    auth_error_enter_phone_number = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    auth_password_input = (By.XPATH, "//input[@id='password']")

class ChangePassPageLocators:
    change_pass_heading = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    change_pass_username_input_placeholder_telephone = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
    change_pass_tab_phone = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    change_pass_username_input = (By.XPATH, "//input[@id='username']")
    change_pass_username_input_value = (By.XPATH, "//input[@name='username']")
    change_pass_tab_mail = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    change_pass_go_back_button = (By.XPATH, "//button[@id='reset-back']")
    change_pass_privacy_policy_link = (By.XPATH, "//*[@id='app-footer']/div[1]/div[2]/a[2]/span")
    change_pass_continue_button = (By.XPATH, "//button[@id='reset']")
    change_pass_error_enter_phone_number = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    change_pass_error_invalid_username_or_text = (By.XPATH, "//span[@id='form-error-message' and contains(text(),'Неверный логин или текст с картинки')]")

class RegPageLocators:
    reg_heading = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    reg_first_name_input_page_right = (By.XPATH, "//section[@id='page-right']//span[contains(text(),'Имя')]/preceding-sibling::input")
    reg_register_button_page_right = (By.XPATH, "//section[@id='page-right']//span[contains(text(),'Зарегистрироваться')]")
    reg_user_agreement_link_page_right = (By.XPATH, "//section[@id='page-right']//span[contains(text(),'Нажимая кнопку " "«Зарегистрироваться», вы принимаете условия')]/following-sibling::a")
    reg_first_name_input = (By.XPATH, "//span[contains(text(),'Имя')]/preceding-sibling::input")        #
    reg_error_first_name_input = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    reg_email_phone_input = (By.XPATH, "//input[@id='address']")                                        #
    reg_email_phone_input_value = (By.XPATH, "//input[@type='hidden' and @name='address']")
    reg_error_invalid_email_or_phone_input = (By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    reg_password_input = (By.XPATH, "//input[@id='password']")                                          #
    reg_error_invalid_password_input = (By.XPATH, "//span[contains(text(),'Пароль должен') or contains(text(),'Длина пароля')]")
    reg_last_name_input = (By.XPATH, "//span[contains(text(),'Фамилия')]/preceding-sibling::input")     #
    reg_password_confirm_input = (By.XPATH, "//input[@id='password-confirm']")                          #
    reg_enter_button = (By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']")  #
    reg_user_agreement_link = (By.XPATH, "//span[contains(text(),'Нажимая кнопку «Зарегистрироваться», " "вы принимаете условия')]/following-sibling::a")
    reg_privacy_policy_link = (By.XPATH, "//a[@class='rt-footer-agreement-link'][2]")
    reg_error_password_dont_match = (By.XPATH, "//span[contains(text(),'Пароли не совпадают')]")

class EmailConfirmPageLocators:
    email_conf_heading = (By.XPATH, "//p[contains(text(),'Kод подтверждения отправлен')]")

class UserAgreementPageLocators:
    user_agreement_heading = (By.XPATH, "//h1[contains(text(),'Пользователь')]")

class RejectedRequestPageLocators:
    rejected_request_heading = (By.XPATH, "//h2[contains(text(),'Ваш запрос был отклонен из соображений безопасности.')]")
    rejected_request_info = (By.XPATH, "//div[contains(text(),'Код запроса: ')]")