# Модуль работы с поиском и отправкой файлов через емейл

# Импорты
import glob
import subprocess
import time
import datetime
import win32com.client as win32  # импорт модуля для работы с Win32COM (MS Outlook, etc.)

# Мои модули
from MyModules.print_log import print_log

# КОНСТАНТЫ
SIGNATURE = """

--
с уважением,
Начальник Ульяновского участка пересчета
Регионального Центра "Ульяновск"
Нурмухамедова Регина Маулетдиновна
Тел.: (8422) 63-47-78 
С 7:00 до 12:00 и с 13:00 до 16:00
"""

RECIPIENTS_TEST = "mva@rosinkas.ru"
RECIPIENTS_RNKO = "centr-msk@r-inkas.ru; dep@r-inkas.ru"
RECIPIENTS_GPB = "inkass-uln@gazprombank.ru"
RECIPIENTS_VTB = "nlevagin@vtb.ru; tazetdinova@vtb.ru; TugushevaEA@vtb.ru"
RECIPIENTS_VBRR = "kalinina@samara.vbrr.ru; kuznetsovaon@samara.vbrr.ru; bagryanova_eg@samara.vbrr.ru; tyakina_iv@samara.vbrr.ru; kalashnikova_nv@samara.vbrr.ru"

# ФУНКЦИИ
def sending_outlook(mode, displayed=True) -> None:
    """Функция подготовки писем к отправке через MS Outlook.
    Режимы mode могут быть 'work' и 'test'"""
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')  # вызов MS Outlook
    new_mail = outlook.CreateItem(0)  # создание письма в MS Outlook

    new_mail.BodyFormat = 2  # формат HTML

    if mode == 'test':
        new_mail.Subject = f'Тестовое письмо {period_for_emails()}'  # указание темы
        new_mail.Body = f"Тестовое письмо из ИТКО за {period_for_emails()}." + SIGNATURE  # сообщение
        new_mail.To = RECIPIENTS_TEST  # обращение к списку получателей

    elif mode == 'work':
        new_mail.Subject = f'Форма 202 {period_for_emails()}'  # указание темы
        new_mail.Body = f"Форма 202 из ИТКО за {period_for_emails()}.\n\nФайлы:\n{search_sending_files(mode_)[1]}" \
                        + SIGNATURE  # сообщение
        new_mail.To = RECIPIENTS_202  # обращение к списку получателей

    if mode_ != 'test':  # работа с вложениями
        print_log("Поиск файлов для отправки через e-mail:", line_before=True)
        for files in (search_sending_files(mode_)[0]):  # вложения
            new_mail.Attachments.Add(files)
        tuple_not_used = ('test', 'vou')
        if mode_ not in tuple_not_used:
            print_log(f"Файлы для отправки:\n{search_sending_files(mode_)[1]}")

    if displayed:  # отображать окно письма
        new_mail.Display(True)  # отображение подготовленного письма или new_mail.Send()  # немедленная отправка письма
    else:
        new_mail.Send()

    print_log("Письмо для отправки через MS Outlook подготовлено")

    time.sleep(0.5)
    subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook


if __name__ == '__main__':
    pass
    # sending_outlook('test')
    # sending_outlook('sformirovat')
    # sending_outlook('202')
    # print(search_sending_files('202')[0])
    # print(search_sending_files('pp')[1])
    # sending_outlook('vou')
