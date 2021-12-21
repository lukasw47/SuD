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
    radian_angle = input_radian_angle()
    degree_angle = radian_angle.to_degree_angle()

    print()
    print(f'Bogenmaß: {radian_angle}')
    print(f'Gradmaß:  {degree_angle}')
    print()
    print()


def input_radian_angle() -> RadianAngle:
    message = 'Gib eine Nummer im Bogenmaß ein: '
    wrong_input_message = 'Die Eingabe muss eine Nummer sein!'

    while (input_number := input(message).strip().replace(',', '.')) and not is_decimal_number(string=input_number):
        print(wrong_input_message)
        print()

    return RadianAngle(input_number)


def is_decimal_number(string: str) -> bool:
    decimal_number_pattern = r'\d+(\.\d*)?$'
    return bool(re.match(decimal_number_pattern, string))


if __name__ == '__main__':
    main()
