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
    decimal_number = input_decimal_number(message='Gib eine Nummer im Bogenmaß ein: ',
                                          wrong_input_message='Die Eingabe muss eine Nummer sein!')
    return RadianAngle(decimal_number)


def input_decimal_number(message: str, wrong_input_message: str) -> str:
    while (decimal_number := input_with_decimal_number_format(message)) \
            and not is_decimal_number(string=decimal_number):
        print(wrong_input_message)
        print()

    return decimal_number


def input_with_decimal_number_format(message: str) -> str:
    return input(message).strip().replace(',', '.')


def is_decimal_number(string: str) -> bool:
    decimal_number_pattern = r'\d+(\.\d*)?$'
    return bool(re.match(decimal_number_pattern, string))


if __name__ == '__main__':
    main()
