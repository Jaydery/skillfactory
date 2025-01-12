from settings import valid_phone, valid_email, sql_injection
from .base_page import BasePage
from .locators import AuthPageLocators, ChangePassPageLocators, UserAgreementPageLocators, \
    RejectedRequestPageLocators, BaseLocators

class ChangePassPage(BasePage):
    # TC_ROST-013 метод проверки типа восстановления пароля по умолчанию
    def default_password_recovery_type(self):
        assert self.is_element_present(ChangePassPageLocators.change_pass_username_input_placeholder_telephone), \
            "element not found"

    # TC_ROST-014 метод проверки на валидацию поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного номера)
    def phone_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.change_pass_tab_phone).click()
        phone = valid_phone()
        self.find_element(ChangePassPageLocators.change_pass_username_input).send_keys(phone)
        self.find_element(BaseLocators.body).click()
        element = self.find_element(ChangePassPageLocators.change_pass_username_input_value)
        value = element.get_attribute("value")
        assert ("7"+str(phone)) == value, "phone do not match"

    # TC_ROST-015 метод проверки на валидацию поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного email)
    def email_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.change_pass_tab_mail).click()
        username_input = self.find_element(ChangePassPageLocators.change_pass_username_input)
        email = valid_email()
        username_input.send_keys(email)
        self.find_element(BaseLocators.body).click()
        element = self.find_element(ChangePassPageLocators.change_pass_username_input_value)
        value = element.get_attribute("value")
        assert email == value, "email do not match"

    # TC_ROST-016 метод проверки кнопки на форму авторизации
    def go_back_button(self):
        self.find_element(ChangePassPageLocators.change_pass_go_back_button).click()
        assert self.is_element_present(AuthPageLocators.auth_heading), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-017 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(ChangePassPageLocators.change_pass_privacy_policy_link).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.user_agreement_heading), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-018 метод проверки восстановления пароля с незаполненными полями
    def password_recovery_with_blank_fields(self):
        self.find_element(ChangePassPageLocators.change_pass_tab_phone).click()
        self.find_element(ChangePassPageLocators.change_pass_continue_button).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.change_pass_error_enter_phone_number), \
            "element not found"

    # TC_ROST-019 метод проверки восстановления пароля с незаполненным значением капчи
    def password_recovery_with_blank_captcha(self):
        self.find_element(ChangePassPageLocators.change_pass_tab_mail).click()
        self.find_element(ChangePassPageLocators.change_pass_username_input).send_keys(valid_email())
        self.find_element(ChangePassPageLocators.change_pass_continue_button).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.change_pass_error_invalid_username_or_text), \
            "element not found"

    # TC_ROST-020 метод проверки текстового поля на SQL-инъекции
    def sql_injection_in_a_text_field(self):
        self.find_element(ChangePassPageLocators.change_pass_username_input).send_keys(sql_injection())
        self.find_element(ChangePassPageLocators.change_pass_continue_button).click()
        assert self.is_element_present(RejectedRequestPageLocators.rejected_request_heading), "element not found"
        assert self.is_element_present(RejectedRequestPageLocators.rejected_request_info), "element not found"