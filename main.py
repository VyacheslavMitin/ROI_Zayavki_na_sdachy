# Модуль подготовки

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

PATH_BANKS = 'C:\\Users\\sonic\\YandexDisk\\Обмен\\заявки'
PATH_VBRR = f'{PATH_BANKS}/ВБРР/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_VTB = f'{PATH_BANKS}/ВТБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_RNKO = f'{PATH_BANKS}/РНКО/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_GPB = f'{PATH_BANKS}/ГПБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/{datetime.date.today().strftime("%d %m %Y")}/'

DICT_BANKS = {
    "ВБРР": os.path.join(PATH_VBRR),
    "ВТБ": os.path.join(PATH_VTB),
    "РНКО": os.path.join(PATH_RNKO),
    "ГПБ": os.path.join(PATH_GPB),
}

FILES_VBRR, FILES_VTB, FILES_RNKO, FILES_GPB = [], [], [], []
DICT_FILES = {
    "ВБРР": FILES_VBRR,
    "ВТБ": FILES_VTB,
    "РНКО": FILES_RNKO,
    "ГПБ": FILES_GPB,
}


def search_files_to_send(printable=False):
    print_log("Сбор файлов для отправки", line_after=False)
    for bank, path in DICT_BANKS.items():
        if printable:
            print_log(f"Начало работы по '{bank}'", line_before=True)
        # Получение в лист всех файлов в каталоге
        list_of_files = filter(os.path.isfile,
                               glob.glob(path + '*'))

        # Сортировка листа с файлами по дате
        list_of_files = sorted(list_of_files,
                               key=os.path.getmtime)
        if printable:
            if not list_of_files:
                print(f'Банка {bank} сегодня нет')

        for file in list_of_files:
            # Итерация по листу с файлами и получение дат файлов

            try:
                timestamp_str = time.strftime('%d.%m.%Y',
                                              time.gmtime(os.path.getmtime(file)))
                if timestamp_str == TODAY_DATE:  # проверка по текущей дате
                    if printable:
                        print(timestamp_str, ' -->', file)
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

    if printable:
        print("\nСловарь:")
        for key, values in DICT_FILES.items():
            if values:
                print(f"Банк '{key}', файлы {values}")


def main():
    search_files_to_send()
    # print(DICT_FILES, '\n')
    for bank, files in DICT_FILES.items():
        if files:
            sending_outlook(mode='work',
                            bank=bank,
                            files=files,
                            displayed=True)

    subprocess.Popen(OUTLOOK_BIN)  # запуск MS Outlook


if __name__ == '__main__':
    # print(search_files_to_send())
    main()
