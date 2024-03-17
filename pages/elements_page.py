import os
from typing import Dict

from selenium.webdriver import Keys
from locators.element_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def enter_first_name(self, first_name: str) -> None:
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)

    def enter_email(self, email: str) -> None:
        self.element_is_visible(self.locators.EMAIL).send_keys(email)

    def enter_gender(self, gender: str) -> None:
        locator_gender = {
            'Male': self.locators.MALE_RADIOBTN,
            'Female': self.locators.FEMALE_RADIOBTN,
            'Other': self.locators.OTHER_RADIOBTN
        }
        self.element_is_visible(locator_gender[gender]).click()

    def enter_mobile(self, mobile: str) -> None:
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)

    def enter_date_of_birth(self, date: Dict[str, str]) -> None:
        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date['year'])
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date['month'])
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date['day'])

    def enter_subjects(self, subjects: list[str]) -> None:
        for subject in subjects:
            element = self.element_is_visible(self.locators.SUBJECTS)
            element.send_keys(subject)
            element.send_keys(Keys.RETURN)

    def enter_hobbies(self, hobbies: list[str]) -> None:
        hobbies_elements: list = self.elements_are_visible(self.locators.HOBBIES_LIST)
        for hobby in hobbies_elements:
            if hobby.text in hobbies:
                hobby.click()

    def enter_picture(self, file: str) -> None:
        upload_file = self.element_is_visible(self.locators.UPLOAD_FILE)
        upload_file.send_keys(os.path.join(os.getcwd(), 'data', file))

    def enter_cur_address(self, cur_address: str) -> None:
        self.element_is_visible(self.locators.CUR_ADDRESS).send_keys(cur_address)

    def enter_state(self, state: str) -> None:
        state_element = self.element_is_present(self.locators.STATE_LIST)
        state_element.send_keys(state)
        state_element.send_keys(Keys.RETURN)

    def enter_city(self, city: str) -> None:
        city_element = self.element_is_present(self.locators.CITY_LIST)
        city_element.send_keys(city)
        city_element.send_keys(Keys.RETURN)

    def enter_submit(self) -> None:
        self.element_is_visible(self.locators.SUBMIT).click()

    def form_result(self) -> Dict[str, str]:
        result_title_list = self.elements_are_visible(self.locators.RESULT_TITLE_TABLE)
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_dict = {k.text: v.text for k, v in zip(result_title_list, result_list)}
        return result_dict
