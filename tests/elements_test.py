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
                assert f"{output.first_name} {output.last_name}" == (result_table['full_name'],
                                                                     'full name does not matched')
            with allure.step('Check email'):
                assert output.email == result_table['email'], 'email does not matched'
            with allure.step('Check gender'):
                assert output.gender == result_table['gender'], 'gender does not matched'
            with allure.step('Check mobile number'):
                assert output.mobile == result_table['mobile'], 'mobile does not matched'
            with allure.step('Check date of birth'):
                assert (f"{output.date_of_birth.day} {output.date_of_birth.month},{output.date_of_birth.year}" ==
                        result_table['date_of_birth']), 'date_of_birth does not matched'
            with allure.step('Check subjects'):
                assert output.subjects == list(result_table['subjects'].split(", ")), 'subjects does not matched'
            with allure.step('Check hobbies'):
                assert output.hobbies == list(result_table['hobbies'].split(", ")), 'hobbies does not matched'
            with allure.step('Check upload file'):
                assert output.upload_file == result_table['upload_file'], 'upload file does not matched'
            with allure.step('Check address'):
                assert output.cur_address == result_table['cur_address'], 'current address does not matched'
            with allure.step('Check state and city'):
                assert f"{output.state} {output.city}" == (result_table['state_and_city'],
                                                           'state and city does not matched')
