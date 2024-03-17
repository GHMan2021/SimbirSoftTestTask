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
    @staticmethod
    def random() -> dict:
        year: str = fake.year()
        month: str = fake.month_name()
        day: str = fake.day_of_month()
        return {
            "year": year,
            "month": month,
            "day": day
        }
