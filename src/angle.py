import math
import re


class RadianAngle(float):

    def __str__(self):
        return f'{super().__str__()} rad'

    def to_degree_angle(self) -> 'DegreeAngle':
        degrees = (self * 180) / math.pi
        return DegreeAngle(degrees)


class DegreeAngle(float):

    def __str__(self):
        return f'{self.degrees}° {self.arc_minutes}\' {self.arc_seconds}"'

    @property
    def degrees(self) -> int:
        return int(self)

    @property
    def arc_minutes(self) -> int:
        remaining_angle = self - self.degrees
        return int(remaining_angle * 60)

    @property
    def arc_seconds(self) -> int:
        remaining_angle = self - self.degrees - (self.arc_minutes / 60)
        return int(remaining_angle * 3600)


def main():
    radian_angle = prompt_user_for_radian_angle()
    degree_angle = radian_angle.to_degree_angle()

    print()
    print(f'Bogenmaß: {radian_angle}')
    print(f'Gradmaß:  {degree_angle}')
    print()
    print()


def prompt_user_for_radian_angle() -> RadianAngle:
    message = 'Gib eine Nummer im Bogenmaß ein: '

    while (user_number := input(message).strip()) and not is_decimal_number(string=user_number):
        print('Die Eingabe muss eine Nummer sein!')
        print()

    return RadianAngle(user_number.replace(',', '.'))


def is_decimal_number(string: str) -> bool:
    return bool(re.match(r'\d+([.,]\d*)?$', string))


if __name__ == '__main__':
    main()
