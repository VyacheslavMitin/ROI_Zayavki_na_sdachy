# Модуль подготовки

# ИМПОРТЫ
import glob
import sys
import os
import time
import datetime
# Мои модули
# from MyModules.config_read import *
# from MyModules.sending_files import sending_outlook
# from MyModules.past_dates import past_dates
from MyModules.print_log import print_log

TODAY_DATE = datetime.date.today().strftime('%d.%m.%Y')
TODAY_YEAR = datetime.date.today().strftime("%Y")
TODAY_MOUNTH = datetime.date.today().strftime("%m")
# print(TODAY_MOUNTH, TODAY_YEAR)

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

PATH_BANKS = '/Users/sonic/Yandex.Disk.localized/Обмен/заявки'
PATH_VBRR = f'{PATH_BANKS}/ВБРР/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_VTB = f'{PATH_BANKS}/ВТБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_RNKO = f'{PATH_BANKS}/РНКО/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/'
PATH_GPB = f'{PATH_BANKS}/ГПБ/{TODAY_YEAR}/{DICT_MOUNTS.get(TODAY_MOUNTH)}/{datetime.date.today().strftime("%d %m %Y")}/'

DICT_BANKS = {
    "ВБРР": PATH_VBRR,
    "ВТБ": PATH_VTB,
    "РНКО": PATH_RNKO,
    "ГПБ": PATH_GPB,
}

# print(DICT_BANKS)

FILES_VBRR, FILES_VTB, FILES_RNKO, FILES_GPB = [], [], [], []
DICT_FILES = {
    "ВБРР": FILES_VBRR,
    "ВТБ": FILES_VTB,
    "РНКО": FILES_RNKO,
    "ГПБ": FILES_GPB,
}

# path = os.path.normpath(PATH_VBRR)
# path = PATH_VBRR
path = os.path.join(PATH_VBRR)
print(path)
# print(os.path.normpath(path))


# Получение в лист всех файлов в каталоге
list_of_files = filter(os.path.isfile,
                       glob.glob(path + '*'))

# Сортировка листа с файлами по дате
list_of_files = sorted(list_of_files,
                       key=os.path.getmtime)


# Итерация по листу с файлами и получение дат файлов
rnko_files = []
for file_path in list_of_files:
    timestamp_str = time.strftime('%d.%m.%Y',
                                  time.gmtime(os.path.getmtime(file_path)))
    # print(timestamp_str, ' -->', file_path)

    if timestamp_str == TODAY_DATE:  # проверка по текущей дате
        print(timestamp_str, ' -->', file_path)
        rnko_files.append(file_path)

print(rnko_files)
