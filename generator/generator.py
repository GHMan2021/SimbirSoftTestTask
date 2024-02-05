from data.data import Student, Date
from faker import Faker

faker = Faker()
Faker.seed()


def generated_student():
    yield Student(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        mobile=faker.numerify('##########'),
        subjects=[
            "Hindi", "English", "Maths", "Physics", "Chemistry",
            "Biology", "Computer Science", "Commerce", "Accounting",
            "Economics", "Arts", "Social Studies", "History", "Civics"
        ],
        cur_address=faker.street_address(),
        state_and_city={
            "NCR": ["Delhi", "Gurgaon", "Noida"],
            "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
            "Haryana": ["Karnal", "Panipat"],
            "Rajasthan": ["Jaipur", "Jaiselmer"]
        }
    )


def generated_date():
    yield Date(
        year=faker.year(),
        month=faker.month_name(),
        day=faker.day_of_month()
    )
