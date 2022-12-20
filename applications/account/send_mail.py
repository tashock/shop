from django.core.mail import send_mail


def send_hello(email):
    send_mail(
        'Вас приветствует крутой сайт', # title
        'привет как дела?', # body
        'muratalievaziret4@gamil.com', # from
        [email] # to
    )


def send_confirmation_email(email, code):
    import time
    time.sleep(5)
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'muratalievaziret4@gamil.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'muratalievaziret4@gamil.com',
        [email]
    )