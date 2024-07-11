from django.core.exceptions import ValidationError


def validate_password(password):
    if password.isdigit():
        raise ValidationError(("password can not be only numeric"), params={'value': password})
    
    counter = 0
    for ch in password:
        if ch.isupper():
            counter += 1
    if counter == 0:
        raise ValidationError(("password need to have at least one upper letter"), params={'value': password})
    
    if len(password) <= 8:
        raise ValidationError(("password cannot be less than 8 characters"), params={'value': password})
    
    return password