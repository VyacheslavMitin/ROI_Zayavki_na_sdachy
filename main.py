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

today_date = datetime.date.today().strftime('%d.%m.%Y')
today_year = datetime.date.today().strftime("%Y")
today_mounth = datetime.date.today().strftime("%m")
print(today_mounth, today_year)

dict_mounts = {
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

path_vbrr = f'V:\\ВБРР\\{today_year}\\{dict_mounts.get(today_mounth)}\\'
path_vtb = f'V:\\ВТБ\\{today_year}\\{dict_mounts.get(today_mounth)}\\'
path_rnko = f'V:\\РНКО\\{today_year}\\{dict_mounts.get(today_mounth)}\\'
path_gpb = f'V:\\ГПБ\\{today_year}\\{dict_mounts.get(today_mounth)}\\{datetime.date.today().strftime("%d %m %Y")}\\'


path = path_rnko
print(path)


# Get list of all files only in the given directory
list_of_files = filter( os.path.isfile,
                        glob.glob(path + '*') )
# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files,
                        key = os.path.getmtime)
# Iterate over sorted list of files and print file path
# along with last modification time of file
rnko_files = []
for file_path in list_of_files:
    timestamp_str = time.strftime(  '%d.%m.%Y',
                                time.gmtime(os.path.getmtime(file_path)))
    if timestamp_str == today_date:
        print(timestamp_str, ' -->', file_path)
        rnko_files.append(file_path)

print(rnko_files)