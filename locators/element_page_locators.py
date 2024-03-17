from selenium.webdriver.common.by import By


class FormPageLocators:
    # text form fields
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")  # xpath
    LAST_NAME = (By.ID, "lastName")  # id
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    CUR_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")

    # radiobutton fields
    MALE_RADIOBTN = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    FEMALE_RADIOBTN = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    OTHER_RADIOBTN = (By.CSS_SELECTOR, "label[for='gender-radio-3']")

    # date_picker field
    DATE_INPUT = (By.ID, "dateOfBirthInput")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    # checkbox fields
    HOBBIES_LIST = (By.CSS_SELECTOR, "label[for^='hobbies-checkbox']")

    # dropdown fields
    STATE_LIST = (By.ID, "react-select-3-input")
    CITY_LIST = (By.ID, "react-select-4-input")

    # upload file field
    UPLOAD_FILE = (By.ID, "uploadPicture")

    # submit button
    SUBMIT = (By.ID, "submit")

    # result data table
    RESULT_TITLE_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[1]")
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")
