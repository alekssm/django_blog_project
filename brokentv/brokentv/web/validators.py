from django.core.exceptions import ValidationError

profile_name_validation_error = "Ensure this value contains only letters, numbers, and underscore."


def validator_profile_username(value):
    for ch in value:
        if ch.isalpha() or ch.isnumeric() or ch == "_":
            pass
        else:
            raise ValidationError(profile_name_validation_error)


def validator_profile_name_only_letters(value):
    for ch in value:
        if ch.isalpha():
            pass
        else:
            raise ValidationError(profile_name_validation_error)