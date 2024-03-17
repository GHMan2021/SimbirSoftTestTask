from selenium.webdriver.chrome.webdriver import WebDriver

from generators.generator import StudentGenerator
from pages.elements_page import FormPage
import allure


@allure.feature('demoqa.com')
@allure.title('Test Form elements')
@allure.description("""
    Goal: Testing form elements

    Steps:
    1. Open url 'https://demoqa.com/automation-practice-form'
    2. Fill all fields
    3. Get result table data
    4. Check full name
    5. Check email
    6. Check gender
    7. Check mobile number
    8. Check date of birth
    9. Check subjects
    10. Check hobbies
    11. Check upload file
    12. Check address
    13. Check state and city
""")
def test_form(driver: WebDriver) -> None:
    with allure.step('Open browser'):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()

    form_page.remove_footer()

    student_data = StudentGenerator.random()
    with allure.step('Fill all fields'):
        form_page.enter_first_name(student_data['first_name'])
        form_page.enter_last_name(student_data['last_name'])
        form_page.enter_email(student_data['email'])
        form_page.enter_gender(student_data['gender'])
        form_page.enter_mobile(student_data['mobile'])
        form_page.enter_date_of_birth(student_data['date_of_birth'])
        form_page.enter_subjects(student_data['subjects'])
        form_page.enter_hobbies(student_data['hobbies'])
        form_page.enter_picture(student_data['upload_file'])
        form_page.enter_cur_address(student_data['cur_address'])
        form_page.enter_state(student_data['state'])
        form_page.enter_city(student_data['city'])
    form_page.enter_submit()

    with allure.step('Get result table data'):
        result_data = form_page.form_result()

    with allure.step('Check full name'):
        assert (f"{student_data['first_name']} {student_data['last_name']}" == result_data['Student Name']), \
            'full name does not matched'
    with allure.step('Check email'):
        assert student_data['email'] == result_data['Student Email'], 'email does not matched'
    with allure.step('Check gender'):
        assert student_data['gender'] == result_data['Gender'], 'gender does not matched'
    with allure.step('Check mobile number'):
        assert student_data['mobile'] == result_data['Mobile'], 'mobile does not matched'
    with allure.step('Check date of birth'):
        date_dict = student_data['date_of_birth']
        assert f"{date_dict['day']} {date_dict['month']},{date_dict['year']}" == result_data['Date of Birth'], \
            'date of birth does not matched'
    with allure.step('Check subjects'):
        assert student_data['subjects'] == list(result_data['Subjects'].split(", ")), 'subjects does not matched'
    with allure.step('Check hobbies'):
        assert student_data['hobbies'] == list(result_data['Hobbies'].split(", ")), 'hobbies does not matched'
    with allure.step('Check upload file'):
        assert student_data['upload_file'] == result_data['Picture'], 'upload file does not matched'
    with allure.step('Check address'):
        assert student_data['cur_address'] == result_data['Address'], 'current address does not matched'
    with allure.step('Check state and city'):
        assert f"{student_data['state']} {student_data['city']}" == result_data['State and City'], \
            'state and city does not matched'
