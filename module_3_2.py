from time import sleep # я знаю, этого в задание не было, просто добавил. Надеюсь за ошибку не считается
def send_email(message, recipient: str, *, sender = "university.help@gmail.com"):
    if '@' not in recipient or '@' not in sender or not (sender.endswith(('.com', '.ru', '.net')) and recipient.endswith(('.com', '.ru', '.net'))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return message, recipient, sender
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
sleep(1)
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
sleep(1)
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
sleep(1)
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')