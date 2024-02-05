from pages.elements_page import FormPage
import pprint


class TestFormElements:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        output = form_page.fill_fields_and_submit()

        print('\n')
        pprint.pprint(output)
        print('\n')

        result_table = form_page.form_result()
        pprint.pprint(result_table)

        assert f"{output.first_name} {output.last_name}" == result_table[0]
        assert output.email == result_table[1]
        assert output.gender == result_table[2]
        assert output.mobile == result_table[3]
        assert f"{output.date_of_birth.day} {output.date_of_birth.month},{output.date_of_birth.year}" == result_table[4]
        assert output.subjects == list(result_table[5].split(', '))
        assert output.hobbies == list(result_table[6].split(', '))
        assert output.upload_file == result_table[7]
        assert output.cur_address == result_table[8]
        assert f"{output.state} {output.city}" == result_table[9]
