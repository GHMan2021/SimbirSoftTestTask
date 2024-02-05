from dataclasses import dataclass


@dataclass
class Student:
    first_name: str = None
    last_name: str = None
    email: str = None
    gender: str = None
    mobile: str = None
    date_of_birth: str = None
    subjects: list = None
    hobbies: list = None
    upload_file: str = None
    cur_address: str = None
    state_and_city: dict = None


@dataclass
class Date:
    year: str = None
    month: str = None
    day: str = None
