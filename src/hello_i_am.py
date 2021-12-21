from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    first_name: str
    last_name: str
    birthday: datetime

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self) -> int:
        return datetime.now().year - self.birthday.year


def main():
    person = Person(first_name='Lukas', last_name='Weber',
                    birthday=datetime(year=2002, month=12, day=4))

    print_information_on_person(person)


def print_information_on_person(person: Person) -> None:
    print()
    print(f'Mein name ist {person.full_name}.')
    print(f'Ich bin {person.age} Jahre alt und mein Geburtstag ist der {person.birthday:%d.%m.%Y}.')
    print()
    print()


if __name__ == '__main__':
    main()
