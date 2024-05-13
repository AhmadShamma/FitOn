import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    PATTERN = r"^[a-zA-Z]+$"
    message = "The name must contain only alphabit letters."
    code = "invalid_name"


    def __init__(self, message=None, code=None) -> None:
        if self.message is not None:
            self.message = message
        if self.code is not None:
            self.code = code

    def __call__(self, value):
        if not re.match(self.PATTERN, value):
            raise ValidationError(self.message, self.code, params={"value": value})
        


def validate_name(value):
    PATTERN = r"^[a-zA-Z]+$"
    message = "The name must contain only alphabit letters."
    code = "invalid_name"

    if not re.match(PATTERN, value):
        raise ValidationError(message, code, params={"value": value})