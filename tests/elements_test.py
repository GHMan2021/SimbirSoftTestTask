from pages.elements_page import FormPage
import allure


@allure.suite('Form elements')
class TestFormElements:
    @allure.feature('Test Form elements')
    def test_form(self, driver):
        with allure.step('Open browser'):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
        with allure.step('Get output data'):
            output = form_page.fill_fields_and_submit()
        with allure.step('Get result table data'):
            result_table = form_page.form_result()

        with allure.step('Check data form'):
            with allure.step('Check full name'):
                assert f"{output.first_name} {output.last_name}" == result_table[0], 'full name does not matched'
            with allure.step('Check email'):
                assert output.email == result_table[1], 'email does not matched'
            with allure.step('Check gender'):
                assert output.gender == result_table[2], 'gender does not matched'
            with allure.step('Check mobile number'):
                assert output.mobile == result_table[3], 'mobile does not matched'
            with allure.step('Check date of birth'):
                assert (f"{output.date_of_birth.day} {output.date_of_birth.month},{output.date_of_birth.year}" ==
                        result_table[4]), 'date_of_birth does not matched'
            with allure.step('Check subjects'):
                assert output.subjects == list(result_table[5].split(', ')), 'subjects does not matched'
            with allure.step('Check hobbies'):
                assert output.hobbies == list(result_table[6].split(', ')), 'hobbies does not matched'
            with allure.step('Check upload file'):
                assert output.upload_file == result_table[7], 'upload file does not matched'
            with allure.step('Check address'):
                assert output.cur_address == result_table[8], 'current address does not matched'
            with allure.step('Check state and city'):
                assert f"{output.state} {output.city}" == result_table[9], 'state and city does not matched'
