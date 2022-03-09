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

PATH_BANKS = cfg.get('PATHS', 'docs_path')
OUTLOOK_BIN = cfg.get('PATHS', 'outlook_bin')

RECIPIENTS_TEST = cfg.get('NAMES', 'recipients_test')
RECIPIENTS_RNKO = cfg.get('NAMES', 'recipients_rnko')
RECIPIENTS_GPB = cfg.get('NAMES', 'recipients_gpb')
RECIPIENTS_VTB = cfg.get('NAMES', 'recipients_vtb')
RECIPIENTS_VBRR = cfg.get('NAMES', 'recipients_vbrr')


if __name__ == '__main__':
    print(PATH_TO_INI)
    print(OUTLOOK_BIN)
    print(PATH_BANKS)
    print(RECIPIENTS_TEST)
    print(RECIPIENTS_RNKO)
    print(RECIPIENTS_GPB)
    print(RECIPIENTS_VTB)
    print(RECIPIENTS_VBRR)

