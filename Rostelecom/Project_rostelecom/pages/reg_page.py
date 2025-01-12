from .base_page import BasePage
from .locators import BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators
import time

class RegPage(BasePage):
    # RT021 метод проверки расположения полей ввода, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        assert self.is_element_present(RegPageLocators.reg_first_name_input_page_right), "element not found"
        assert self.is_element_present(RegPageLocators.reg_register_button_page_right), "element not found"
        assert self.is_element_present(RegPageLocators.reg_user_agreement_link_page_right), "element not found"

    # TC_ROST-022 метод проверки валидации текстового поля (ввод валидных данных)
    def text_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.reg_first_name_input).send_keys(input_text)
        self.find_element(BaseLocators.body).click()
        assert self.is_not_element_present(RegPageLocators.reg_error_first_name_input), "element found"

    # TC_ROST-023 метод проверки на валидацию поля ввода email или мобильного телефона (ввод валидных данных)
    def email_or_phone_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.reg_email_phone_input).send_keys(input_text)
        self.find_element(BaseLocators.body).click()
        element = self.find_element(RegPageLocators.reg_email_phone_input_value)
        value = element.get_attribute("value")
        assert input_text == value, "email or phone do not match"
        assert self.is_not_element_present(RegPageLocators.reg_error_invalid_email_or_phone_input), "element found"

    # TC_ROST-024 метод проверки на валидацию поля ввода пароля (ввод валидных данных)
    def password_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.reg_password_input).send_keys(input_text)
        self.find_element(BaseLocators.body).click()
        assert self.is_not_element_present(RegPageLocators.reg_error_invalid_password_input), "element found"

    # TC_ROST-025 метод проверки регистрации с валидными данными и регионом по умолчанию
    def registration_with_valid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.reg_first_name_input).send_keys(first_name)
        self.find_element(RegPageLocators.reg_last_name_input).send_keys(last_name)
        self.find_element(RegPageLocators.reg_email_phone_input).send_keys(email_phone)
        self.find_element(RegPageLocators.reg_password_input).send_keys(password)
        self.find_element(RegPageLocators.reg_password_confirm_input).send_keys(password)
        self.find_element(RegPageLocators.reg_enter_button).click()
        assert self.is_element_present(EmailConfirmPageLocators.email_conf_heading), "element not found"

    # TC_ROST-026 метод проверки ссылки под кнопкой "Зарегистрироваться" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.reg_user_agreement_link).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.user_agreement_heading), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-027 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.reg_privacy_policy_link).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.user_agreement_heading), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-028 метод проверки валидации текстового поля (ввод невалидных данных)
    def text_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.reg_first_name_input).send_keys(input_text)
        self.find_element(BaseLocators.body).click()
        assert self.is_element_present(RegPageLocators.reg_error_first_name_input), "element not found"

    # TC_ROST-029 метод проверки валидации поля ввода email или мобильного телефона (ввод невалидных данных)
    def email_or_phone_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.reg_email_phone_input).send_keys(input_text)
        self.find_element(BaseLocators.body).click()
        assert self.is_element_present(RegPageLocators.reg_error_invalid_email_or_phone_input), "element not found"

    # TC_ROST-030 метод проверки валидации поля ввода пароля (ввод невалидных данных)
    def password_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.reg_password_input).send_keys(input_text)
        self.find_element(BaseLocators.body).click()
        assert self.is_element_present(RegPageLocators.reg_error_invalid_password_input), "element not found"

    # TC_ROST-031 метод проверки заполнения поля подтверждения пароля данными, отличными от введенных в поле ввода пароля
    def entering_data_in_the_password_confirmation_field(self, password1, password2):
        self.find_element(RegPageLocators.reg_password_input).send_keys(password1)
        self.find_element(RegPageLocators.reg_password_confirm_input).send_keys(password2)
        self.find_element(RegPageLocators.reg_enter_button).click()
        assert self.is_element_present(RegPageLocators.reg_error_password_dont_match), "element not found"

    # TC_ROST-032 метод проверки регистрации с невалидными данными
    def registration_with_invalid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.reg_first_name_input).send_keys(first_name)
        self.find_element(RegPageLocators.reg_last_name_input).send_keys(last_name)
        self.find_element(RegPageLocators.reg_email_phone_input).send_keys(email_phone)
        self.find_element(RegPageLocators.reg_password_input).send_keys(password)
        self.find_element(RegPageLocators.reg_password_confirm_input).send_keys(password)
        self.find_element(RegPageLocators.reg_enter_button).click()
        assert self.is_not_element_present(EmailConfirmPageLocators.email_conf_heading), "element found"