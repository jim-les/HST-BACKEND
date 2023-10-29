import random, string
from django.core.mail import send_mail
from django.conf import settings


def generate_otp():
    """
    The function generates a 6 digit random number
    :param: None
    :Returns:
        6 digit random number
    """
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(6))
    return otp

def send_otp_email(email,otp):
    """
    The function sends an email containing otp to the user
    Args:
        param1: user email
        param2: generated otp
    Returns: None
    """
    subject = "HST OTP login"
    message = f"Your OTP is {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_email = [email]
    send_mail(subject, message, from_email, recipient_email)