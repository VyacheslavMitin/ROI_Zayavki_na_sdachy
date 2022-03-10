# Модуль отправки Заявок на сдачу наличных денег

# ИМПОРТЫ
import glob
import subprocess
import sys
import os
import time
import datetime
# Мои модули
from MyModules.config_read import *
from MyModules.sending_files import sending_outlook
from MyModules.print_log import print_log

TODAY_DATE = datetime.date.today().strftime('%d.%m.%Y')
TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_MOUNTH = datetime.date.today().strftime("%m")

DICT_MOUNTS = {
    '01': "Январь",
    '02': "Февраль",
    '03': "Март",
    '04': "Апрель",
    '05': "Май",
    '06': "Июнь",
    '07': "Июль",
    '08': "Август",
    '09': "Сентябрь",
    '10': "Октябрь",
    '11': "Ноябрь",
    '12': "Декабрь"
}

PATH_VBRR = f'{PATH_BANKS}/ВБРР/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_VTB = f'{PATH_BANKS}/ВТБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_RNKO = f'{PATH_BANKS}/РНКО/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
# проверка вложенной папки в ГПБ
PATH_GPB = f'{PATH_BANKS}/ГПБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/{datetime.date.today().strftime("%d %m %Y")}/'
if os.path.isdir(f'{PATH_GPB}/{datetime.date.today().strftime("%d %m %Y")}/'):
    PATH_GPB = f'{PATH_GPB}/{datetime.date.today().strftime("%d %m %Y")}/'

DICT_BANKS = {  # словарь с путями для банков
    "ВБРР": os.path.join(PATH_VBRR),
    "ВТБ": os.path.join(PATH_VTB),
    "РНКО": os.path.join(PATH_RNKO),
    "ГПБ": os.path.join(PATH_GPB),
}

FILES_VBRR, FILES_VTB, FILES_RNKO, FILES_GPB = [], [], [], []
DICT_FILES = {  # словарь с пустыми списками файлов
    "ВБРР": FILES_VBRR,
    "ВТБ": FILES_VTB,
    "РНКО": FILES_RNKO,
    "ГПБ": FILES_GPB,
}


def network_work():
    """Функция работы с сетью"""
    print_log("Проверка сети и открытие каталога с папками банков", line_after=True)
    if not os.path.isdir(PATH_BANKS):
        print("\nНеобходимо включить кассовую сеть если это не произошло и перезапустить программу!\n".upper())
        input()
        sys.exit("Кассовая сеть не включена!")

    os.system(f"explorer.exe {PATH_BANKS}")


def search_files_to_send(printable=False, technical=False):
    """Функция подготовки списка файлов на отправку"""
    print_log(f"Сбор документов для отправки из '{PATH_BANKS}'", line_after=False)

    for bank, path in DICT_BANKS.items():
        if printable:
            print_log(f"Файлы для работы с банком '{bank}':", line_before=True)
        # Получение в лист всех файлов в каталоге
        list_of_files = filter(os.path.isfile,
                               glob.glob(path + '*'))

        # Сортировка листа с файлами по дате
        list_of_files = sorted(list_of_files,
                               key=os.path.getmtime)
        # if printable:
        #     if not list_of_files:
        #         print(f'Документов Банка {bank} в этом месяце нет')

        for file in list_of_files:  # Итерация по листу с файлами и получение дат файлов
            try:
                timestamp_str = time.strftime('%d.%m.%Y',
                                              time.gmtime(os.path.getmtime(file)))
                if timestamp_str == TODAY_DATE:  # проверка по текущей дате
                    if printable:
                        # print(timestamp_str, ' -->', file)
                        print(file)
                    if bank == "ВБРР":
                        FILES_VBRR.append(os.path.normpath(file))
                    elif bank == "ВТБ":
                        FILES_VTB.append(os.path.normpath(file))
                    elif bank == "РНКО":
                        FILES_RNKO.append(os.path.normpath(file))
                    elif bank == "ГПБ":
                        FILES_GPB.append(os.path.normpath(file))
            except FileNotFoundError:  # если нет каталога или файла
                pass

    if technical:  # вывод списка в принте если нужно
        print("\nСловарь:")
        for key, values in DICT_FILES.items():
            if values:
                print(f"Банк '{key}', файлы {values}")


def main():
    welcome = 'запуск отправки Заявок на сдачу наличных денег в банки\n'.upper()
    print(welcome)  # представление

    network_work()

    search_files_to_send(printable=True, technical=False)  # поиск файлов на отправку и запись в словарь

    print_log(f"Подготовка писем на отправку в MS Outlook:", line_before=True)
    for bank, files in DICT_FILES.items():  # отправка файлов (постановка в очередь аутлука)
        if files:
            sending_outlook(mode='work',
                            bank=bank,
                            files=files,
                            displayed=True)

    print_log(f"Запуск MS Outlook...", line_before=True)
    subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook
    print("MS Outlook запущен, необходимо выключить кассовую сеть")

    ending = '\nокончание отправки Заявок на сдачу наличных денег в банки\n'.upper()
    print(ending)

    input()  # пауза программы перед выходом
    sys.exit()


if __name__ == '__main__':
    main()
