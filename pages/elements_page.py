import random
import time
from pathlib import Path

from selenium.webdriver import Keys

from generator.generator import generated_student, generated_date
from locators.element_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_fields_and_submit(self):
        student_data = next(generated_student())

        first_name = student_data.first_name
        last_name = student_data.last_name
        email = student_data.email
        mobile = student_data.mobile
        subjects = student_data.subjects
        cur_address = student_data.cur_address
        state_and_city = student_data.state_and_city

        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)

        gender = self.element_is_visible(self.locators.GENDER_RADIOBUTTON)
        gender.click()
        student_data.gender = gender.text

        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)

        # select date of birth
        date = next(generated_date())
        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        student_data.date_of_birth = date

        #  select subjects
        count_of_subjects = random.randint(0, 14)
        if count_of_subjects > 0:
            random.shuffle(subjects)
            student_subjects = subjects[:count_of_subjects]
            for subject in student_subjects:
                element = self.element_is_visible(self.locators.SUBJECTS)
                element.send_keys(subject)
                element.send_keys(Keys.RETURN)
            student_data.subjects = student_subjects
        else:
            student_data.subjects = ['']

        #  select hobbies
        count_of_hobbies = random.randint(0, 3)
        if count_of_hobbies > 0:
            hobbies = self.elements_are_visible(self.locators.HOBBIES_LIST)
            random.shuffle(hobbies)
            student_hobbies = hobbies[:count_of_hobbies]
            for hobby in student_hobbies:
                hobby.click()
                time.sleep(1)
            student_data.hobbies = [i.text for i in student_hobbies]
        else:
            student_data.hobbies = ['']

        # upload file
        upload_file = self.element_is_visible(self.locators.UPLOAD_FILE)
        upload_file.send_keys(f"{Path.cwd().parent}/tests/picture.jpg")
        student_data.upload_file = "picture.jpg"

        self.element_is_visible(self.locators.CUR_ADDRESS).send_keys(cur_address)

        # select state and city
        state_and_city_list = [(k, v) for k, v in state_and_city.items()]
        state_name, cities_list = random.choice(state_and_city_list)
        city_name = random.choice(cities_list)

        state = self.element_is_present(self.locators.STATE_LIST)
        state.send_keys(state_name)
        state.send_keys(Keys.RETURN)
        student_data.state = state_name

        city = self.element_is_present(self.locators.CITY_LIST)
        city.send_keys(city_name)
        city.send_keys(Keys.RETURN)
        student_data.city = city_name

        # submit button
        self.element_is_visible(self.locators.SUBMIT).click()

        return student_data

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text
