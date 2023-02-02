import re
from enum import Enum


class MetaFieldWrongDatatype(Exception):
    pass


class MetaFieldMissingMandatoryValue(Exception):
    pass


class MetaFieldDuplicate(Exception):
    pass


class MetaFieldNumberOutOfRange(Exception):
    pass


class Optionality(Enum):
    MANDATORY = 1,
    OPTIONAL = 2


JSON_PATH_VALID_RE = re.compile("^[a-zA-Z0-9_]*$")    # Allow only letters, numbers, underscores


class MetaField:
    def __init__(self, json_path: str, data_type: type, optionality: Optionality, min_value=None, max_value=None):
        assert(JSON_PATH_VALID_RE.match(json_path))
        assert(data_type in [int, float, str])
        assert(optionality in [Optionality.MANDATORY, Optionality.OPTIONAL])
        assert(min_value is None or isinstance(min_value, data_type))
        assert(max_value is None or isinstance(max_value, data_type))
        assert(min_value is None or max_value is None or min_value < max_value)

        self._json_path = json_path
        self._data_type = data_type
        self._optionality = optionality
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    def set(self, value):
        if not isinstance(value, self._data_type):
            raise MetaFieldWrongDatatype()

        if self._min_value is not None and value < self._min_value:
            raise MetaFieldNumberOutOfRange

        if self._max_value is not None and value > self._max_value:
            raise MetaFieldNumberOutOfRange

        self._value = value

    def get(self):
        return self._value

    def add_to_json(self, output_json: dict):
        if self._value is None and self._optionality == Optionality.MANDATORY:
            raise MetaFieldMissingMandatoryValue

        if self._value is not None:
            if self._json_path in output_json:
                raise MetaFieldDuplicate
            else:
                output_json[self._json_path] = self._value

    def get_from_json(self, input_json: dict):
        try:
            self.set(input_json[self._json_path])
        except KeyError:
            if self._optionality == Optionality.MANDATORY:
                raise MetaFieldMissingMandatoryValue

    @staticmethod
    def create_json(fields: list):
        output_json = {}
        for f in fields:
            f.add_to_json(output_json)
        return output_json

    @staticmethod
    def parse_json(fields: list, input_json: dict):
        for f in fields:
            f.get_from_json(input_json)
