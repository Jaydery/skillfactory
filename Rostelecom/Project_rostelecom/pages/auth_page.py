from settings import valid_email, sql_injection, random_int
from .base_page import BasePage
from .locators import BaseLocators, AuthPageLocators, ChangePassPageLocators, RegPageLocators, \
    UserAgreementPageLocators, RejectedRequestPageLocators

class AuthPage(BasePage):
    # TC_ROST-001 метод проверки перехода на форму авторизации
    def the_authorization_form_is_open(self):
        assert self.is_element_present(AuthPageLocators.auth_heading)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-002 метод проверки расположения логотипа и слогана
    def location_of_the_logo_and_slogan(self):
        assert self.is_element_present(AuthPageLocators.auth_logo), "element not found"
        assert self.is_element_present(AuthPageLocators.auth_slogan), "element not found"

    # TC_ROST-003 метод проверки расположения меню выбора типа аутентификации
    def location_of_the_tab_menu(self):
        assert self.is_element_present(AuthPageLocators.auth_tab_menu), "element not found"

    # TC_ROST-004 метод проверки типа аутентификации по умолчанию
    def default_authentication_type(self):
        assert self.is_element_present(AuthPageLocators.auth_username_input_placeholder_telephone), \
            "element not found"

    # TC_ROST-005 метод проверки автоматического изменения типа аутентификации
    def automatic_change_of_authentication_type(self):
        self.find_element(AuthPageLocators.auth_username_input).send_keys(valid_email())
        self.find_element(BaseLocators.body).click()
        assert self.is_element_present(AuthPageLocators.auth_username_input_activ_email), "element not found"

    # TC_ROST-006 метод проверки ссылки на форму восстановления пароля
    def link_to_the_password_recovery_form(self):
        self.find_element(AuthPageLocators.auth_forgot_password_link).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.change_pass_heading), "element not found"

    # TC_ROST-007 метод проверки ссылки на форму регистрации
    def link_to_the_registration_form(self):
        self.find_element(AuthPageLocators.auth_register_link).click()
        assert self.is_element_present(RegPageLocators.reg_heading), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               in self.browser.current_url, "url do not match"

    # TC_ROST-008 метод проверки ссылки под кнопкой "Войти" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthPageLocators.auth_user_agreement_link).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.user_agreement_heading), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-009 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthPageLocators.auth_privacy_policy_link).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.user_agreement_heading), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-010 метод проверки ссылки на страницу авторизации с помощью соцсети "ВКонтакте"
    def link_to_social_vk(self):
        self.find_element(AuthPageLocators.auth_social_vk_link).click()
        assert "https://id.vk.com/" \
            in self.browser.current_url, "url do not match"

    # TC_ROST-011 метод проверки авторизации с незаполненными полями
    def authorization_with_blank_fields(self):
        self.find_element(AuthPageLocators.auth_tab_phone).click()
        self.find_element(AuthPageLocators.auth_enter_button).click()
        assert self.is_element_present(AuthPageLocators.auth_error_enter_phone_number), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # TC_ROST-012 метод проверки текстового поля на SQL-инъекции
    def sql_injection_in_a_text_field(self):
        self.find_element(AuthPageLocators.auth_username_input).send_keys(sql_injection())
        self.find_element(AuthPageLocators.auth_password_input).send_keys(random_int())
        self.find_element(AuthPageLocators.auth_enter_button).click()
        assert self.is_element_present(RejectedRequestPageLocators.rejected_request_heading), "element not found"
        assert self.is_element_present(RejectedRequestPageLocators.rejected_request_info), "element not found"
