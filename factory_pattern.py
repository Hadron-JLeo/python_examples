""" 
Created this script as a reference for a class Subject and a Factory Pattern,
which is not instantiated but can keep track of how many and which Subject Objects have been created 

Such as class is also referred to as a "Static Utility Class or Factory Class"
"""



from dataclasses import dataclass
from typing import Dict


@dataclass
class Subject:
    """ A subject class which only stores data: name, code, credits """
    name: str
    code: str
    credits: int


class SubjectFactory:
    """ A factory class which created and manages instances of type Subject """
    _subject_count: int = 0
    _subjects: Dict[str, Subject] = {}

    @classmethod
    def create(cls, name: str, code: str, credits: int) -> Subject:
        if credits <= 0:
            raise ValueError("Credits must be positive")

        subject = Subject(name=name, code=code, credits=credits)

        cls._subject_count += 1
        cls._subjects[code] = subject

        return subject

    @classmethod
    def from_dict(cls, data: dict) -> Subject:
        return cls.create(
            name=data["name"],
            code=data["code"],
            credits=data["credits"]
        )

    @classmethod
    def default(cls) -> Subject:
        return cls.create("Untitled", "XXX000", 3)

    @classmethod
    def get_subject_count(cls) -> int:
        return cls._subject_count

    @classmethod
    def get_all_subjects(cls) -> Dict[str, Subject]:
        return cls._subjects.copy()
