# Модуль чтения конфига с настройками
# from MyModules.config_read import *

import configparser
import os

# КОНСТАНТЫ
name_curdir = os.path.basename(os.path.abspath(os.path.curdir))

if name_curdir == 'MyModules':
    path_ = os.path.abspath(os.path.join(os.path.curdir, '..')) + '\\'
else:
    path_ = os.path.abspath(os.path.join(os.path.curdir)) + '\\'

INI_FILE = 'config.ini'
PATH_TO_INI = path_ + INI_FILE

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read(PATH_TO_INI)


OUTLOOK_BIN = cfg.get('PATHS', 'outlook_bin')

RECIPIENTS_TEST = "mva@rosinkas.ru; vyacheslav.mitin@gmail.com"
RECIPIENTS_RNKO = "centr-msk@r-inkas.ru; dep@r-inkas.ru"
RECIPIENTS_GPB = "inkass-uln@gazprombank.ru"
RECIPIENTS_VTB = "nlevagin@vtb.ru; tazetdinova@vtb.ru; TugushevaEA@vtb.ru"
RECIPIENTS_VBRR = "kalinina@samara.vbrr.ru; kuznetsovaon@samara.vbrr.ru; bagryanova_eg@samara.vbrr.ru; tyakina_iv@samara.vbrr.ru; kalashnikova_nv@samara.vbrr.ru"


if __name__ == '__main__':
    print(PATH_TO_INI)
    print(OUTLOOK_BIN)
    print(RECIPIENTS_TEST)
    print(RECIPIENTS_RNKO)
    print(RECIPIENTS_GPB)
    print(RECIPIENTS_VTB)
    print(RECIPIENTS_VBRR)

