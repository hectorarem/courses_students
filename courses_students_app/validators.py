import re
from django.core.exceptions import ValidationError


def validate_name(value):
    if re.match("^[\-'a-zA-Z ]+$", value):
        return value
    else:
        raise ValidationError("Solo Letras")

def validate_age(value):
    if 7 < value < 60: # here we validate age range, now we have a example
        return value
    else:
        raise ValidationError("Rango de 7 a 60 años")
