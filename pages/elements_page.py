import os

import allure
from selenium.webdriver import Keys

from generators.generator import StudentGenerator
from locators.element_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    student_data = StudentGenerator.random()
    first_name = student_data['first_name']
    last_name = student_data['last_name']
    email = student_data['email']
    gender = student_data['gender']
    mobile = student_data['mobile']
    date = student_data['date_of_birth']
    subjects = student_data['subjects']
    hobbies = student_data['hobbies']
    upload_file = student_data['upload_file']
    cur_address = student_data['cur_address']
    state = student_data['state']
    city = student_data['city']

    def fill_fields_and_submit(self):
        self.remove_footer()

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(self.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(self.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(self.email)

        locator_gender = {
            'Male': self.locators.MALE_RADIOBTN,
            'Female': self.locators.FEMALE_RADIOBTN,
            'Other': self.locators.OTHER_RADIOBTN
        }.get(self.gender)
        self.element_is_visible(locator_gender).click()

        self.element_is_visible(self.locators.MOBILE).send_keys(self.mobile)

        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, self.date['year'])
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, self.date['month'])
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, self.date['day'])

        for subject in self.subjects:
            element = self.element_is_visible(self.locators.SUBJECTS)
            element.send_keys(subject)
            element.send_keys(Keys.RETURN)

        hobbies_elements = self.elements_are_visible(self.locators.HOBBIES_LIST)
        for hobby in hobbies_elements:
            if hobby.text in self.hobbies:
                hobby.click()

        upload_file = self.element_is_visible(self.locators.UPLOAD_FILE)
        upload_file.send_keys(os.path.join(os.getcwd(), 'data', self.upload_file))

        self.element_is_visible(self.locators.CUR_ADDRESS).send_keys(self.cur_address)

        state = self.element_is_present(self.locators.STATE_LIST)
        state.send_keys(self.state)
        state.send_keys(Keys.RETURN)

        city = self.element_is_present(self.locators.CITY_LIST)
        city.send_keys(self.city)
        city.send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.SUBMIT).click()

    @allure.title('Get form result')
    def form_result(self):
        output_fields = (
            'full_name',
            'email',
            'gender',
            'mobile',
            'date_of_birth',
            'subjects',
            'hobbies',
            'upload_file',
            'cur_address',
            'state_and_city'
        )
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_text = {k: v.text for k, v in zip(output_fields, result_list)}
        print(result_text)
        return result_text
