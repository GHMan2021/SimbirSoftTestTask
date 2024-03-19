import datetime
import random

from faker import Faker

fake = Faker()

subjects_list = [
    "Hindi", "English", "Maths", "Physics", "Chemistry",
    "Biology", "Computer Science", "Commerce", "Accounting",
    "Economics", "Arts", "Social Studies", "History", "Civics"
]

hobbies_list = ["Sports", "Reading", "Music"]

state_and_city_dict = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"]
}


class StudentGenerator:
    """Класс StudentGenerator используется для генерации данных о студенте

    Применение: формирует данные для проведения тестов

    Note:
        Данные о gender, subjects, hobbies, state, city взяты с сайта,
        объекта тестирования.

    Methods:
    --------
    random()
        Генерирует случайные данные из библиотеки Faker и выборочные с сайта.
        Результат возвращает в виде словаря.
    """

    @staticmethod
    def random() -> dict:
        first_name: str = fake.first_name()
        last_name: str = fake.last_name()
        email: str = fake.email()
        gender: str = random.choice(["Male", "Female", "Other"])
        mobile: str = fake.numerify("##########")
        date_of_birth: dict = DateGenerator.random()

        subjects_tmp = [i for i in subjects_list if random.choice([True, False])]
        subjects: list = subjects_tmp if bool(subjects_tmp) else ['']

        hobbies_tmp = [i for i in hobbies_list if random.choice([True, False])]
        hobbies: list = hobbies_tmp if bool(hobbies_tmp) else ['']

        upload_file: str = "picture.jpg"
        cur_address: str = fake.street_address()

        state_and_city: tuple = random.choice([(k, v) for k, v in state_and_city_dict.items()])
        state: str
        city: str
        state, city = state_and_city[0], random.choice(state_and_city[1])
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "gender": gender,
            "mobile": mobile,
            "date_of_birth": date_of_birth,
            "subjects": subjects,
            "hobbies": hobbies,
            "upload_file": upload_file,
            "cur_address": cur_address,
            "state": state,
            "city": city
        }


class DateGenerator:
    """Класс DateGenerator используется для генерации случайной даты.

    Применение: используется в классе StudentGenerator для поля
    дата рождения студента возрастом от 16 до 70 лет.

    Methods
    -------
    random()
        Из библиотеки Faker генерирует год, день числами и название месяца.
        Возвращает результат в виде словаря.
    """

    @staticmethod
    def random() -> dict:
        date: datetime.date = fake.date_of_birth(minimum_age=16, maximum_age=70)
        year: str = str(date.year)
        month: str = date.strftime("%B")
        day: str = str(date.day)
        return {
            "year": year,
            "month": month,
            "day": day
        }
