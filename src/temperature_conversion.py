import functools
import operator
from typing import Sequence, Type, Union, Iterable


class Temperature(float):

    @classmethod
    def from_string(cls, string: str) -> 'Temperature':
        return cls(string.removesuffix(cls.get_suffix()))

    @classmethod
    def get_temperature_types(cls) -> Sequence[Type['Temperature']]:
        return cls.__subclasses__()

    @classmethod
    def parse(cls, text: str) -> 'Temperature':
        return cls(text.removesuffix(cls.get_suffix()).rstrip())

    @classmethod
    def get_title(cls) -> str:
        raise NotImplementedError

    @classmethod
    def get_suffixes(cls) -> Sequence[str]:
        return tuple(temperature_type.get_suffix() for temperature_type in Temperature.get_temperature_types())

    @classmethod
    def get_suffix(cls) -> str:
        raise NotImplementedError

    def __str__(self):
        return f'{float(self):.2f}{self.get_suffix()}'

    def to_temperature(self, temperature_type: Type['Temperature']):
        if temperature_type == CelsiusTemperature:
            return self.to_celsius()

        elif temperature_type == KelvinTemperature:
            return self.to_kelvin()

        elif temperature_type == FahrenheitTemperature:
            return self.to_fahrenheit()

        return None

    def to_celsius(self) -> Union['CelsiusTemperature', None]:
        pass

    def to_kelvin(self) -> Union['KelvinTemperature', None]:
        pass

    def to_fahrenheit(self) -> Union['FahrenheitTemperature', None]:
        pass


class CelsiusTemperature(Temperature):

    @classmethod
    def get_title(cls) -> str:
        return 'celsius'

    @classmethod
    def get_suffix(cls) -> str:
        return '°'

    def to_kelvin(self) -> 'KelvinTemperature':
        kelvin = self + 273.15
        return KelvinTemperature(kelvin)

    def to_fahrenheit(self) -> 'FahrenheitTemperature':
        fahrenheit = ((9 / 5) * self) + 32
        return FahrenheitTemperature(fahrenheit)


class KelvinTemperature(Temperature):

    @classmethod
    def get_title(cls) -> str:
        return 'kelvin'

    @classmethod
    def get_suffix(cls) -> str:
        return 'K'

    def to_celsius(self) -> CelsiusTemperature:
        celsius = self - 273.15
        return CelsiusTemperature(celsius)

    def to_fahrenheit(self) -> 'FahrenheitTemperature':
        fahrenheit = (self * (9 / 5)) - 459.67
        return FahrenheitTemperature(fahrenheit)


class FahrenheitTemperature(Temperature):

    @classmethod
    def get_title(cls) -> str:
        return 'fahrenheit'

    @classmethod
    def get_suffix(cls) -> str:
        return '°F'

    def to_celsius(self) -> CelsiusTemperature:
        celsius = (5 / 9) * (self - 32)
        return CelsiusTemperature(celsius)

    def to_kelvin(self) -> KelvinTemperature:
        kelvin = (5 / 9) * (self + 459.67)
        return KelvinTemperature(kelvin)


def run_command_line_interface() -> None:
    try:
        while True:
            convert_temperatures()

    except KeyboardInterrupt:
        pass


def convert_temperatures() -> None:
    temperature = input_temperature()
    print_other_temperatures_from_temperature(temperature=temperature)


def input_temperature() -> Temperature:
    temperature_suffixes = '|'.join(Temperature.get_suffixes())

    while True:
        print()

        if not (raw_temperature_string := input(f'Bitte eine Temperatur angeben [{temperature_suffixes}]: ')):
            continue

        temperature_string = raw_temperature_string.replace(',', '.', 1).strip()

        if not (temperature_type := get_temperature_type_for_string_if_exists(string=temperature_string)):
            print(f'Die Temperatur muss mit ({temperature_suffixes}) enden.')
            continue

        if not is_decimal_temperature(string=temperature_string):
            print(f'Die Temperatur muss eine Zahl sein!')
            continue

        return temperature_type.from_string(string=temperature_string)


def get_temperature_type_for_string_if_exists(string: str) -> Union[Type[Temperature], None]:
    possible_temperature_types = filter(lambda temperature: string.rstrip().endswith(temperature.get_suffix()),
                                        Temperature.get_temperature_types())
    return next(possible_temperature_types, None)


def is_decimal_temperature(string: str) -> bool:
    string_without_suffix = remove_temperature_suffix(string)
    number_parts = string_without_suffix.split('.', 1)

    return all(map(str.isdecimal, number_parts))


def remove_temperature_suffix(string: str) -> str:
    suffix_on_string = next(filter(string.endswith, Temperature.get_suffixes()), '')
    return string.removesuffix(suffix_on_string).rstrip()


def print_other_temperatures_from_temperature(temperature: Temperature):
    other_temperature_types = get_temperature_types_excluding_type(temperature_type=temperature.__class__)
    other_temperatures = map(temperature.to_temperature, other_temperature_types)

    print()
    for other_temperature in other_temperatures:
        print(f'In {other_temperature.get_title().title()}: {other_temperature}')
    print()


def get_temperature_types_excluding_type(temperature_type: Type[Temperature]) -> Iterable[Type[Temperature]]:
    return filter(functools.partial(operator.ne, temperature_type), Temperature.get_temperature_types())


if __name__ == '__main__':
    run_command_line_interface()
