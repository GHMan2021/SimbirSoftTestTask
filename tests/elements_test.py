from pages.elements_page import FormPage


class TestFormElements:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        output = form_page.fill_fields_and_submit()
        result_table = form_page.form_result()

        assert f"{output.first_name} {output.last_name}" == result_table[0], 'full name does not matched'
        assert output.email == result_table[1], 'email does not matched'
        assert output.gender == result_table[2], 'gender does not matched'
        assert output.mobile == result_table[3], 'mobile does not matched'
        assert (f"{output.date_of_birth.day} {output.date_of_birth.month},{output.date_of_birth.year}" ==
                result_table[4]), 'date_of_birth does not matched'
        assert output.subjects == list(result_table[5].split(', ')), 'subjects does not matched'
        assert output.hobbies == list(result_table[6].split(', ')), 'hobbies does not matched'
        assert output.upload_file == result_table[7], 'upload file does not matched'
        assert output.cur_address == result_table[8], 'current address does not matched'
        assert f"{output.state} {output.city}" == result_table[9], 'state and city does not matched'
