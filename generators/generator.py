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
    def random():
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        gender = random.choice(["Male", "Female", "Other"])
        mobile = fake.numerify("##########")
        date_of_birth = DateGenerator.random()

        subjects_tmp = [i for i in subjects_list if random.choice([True, False])]
        subjects = subjects_tmp if bool(subjects_tmp) else ['']

        hobbies_tmp = [i for i in hobbies_list if random.choice([True, False])]
        hobbies = hobbies_tmp if bool(hobbies_tmp) else ['']

        upload_file = "picture.jpg"
        cur_address = fake.street_address()

        state_and_city = random.choice([(k, v) for k, v in state_and_city_dict.items()])
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
    def random():
        year = fake.year()
        month = fake.month_name()
        day = fake.day_of_month()
        return {
            "year": year,
            "month": month,
            "day": day
        }
