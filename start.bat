:: ‡ ¯ãáª á¥â¨ ª ááë ¨ ¬®¤ã«ï ­  ¯¨â®­¥ ¯® ®â¯à ¢ª¥ § ï¢®ª ¢ ¡ ­ª
@ECHO off
TITLE ‡€“‘Š Š€‘‘Ž‚Ž‰ ‘…’ˆ ˆ Žƒ€ŒŒ› Ž’€‚Šˆ ‡€Ÿ‚ŽŠ ‚ €Šˆ

ECHO ‡ ¯ãáª ‘¥â¨ ª ááë
netsh interface set interface "Kassa" enable
TIMEOUT 3 >nul

CD "C:\Users\sonic\PycharmProjects\ROI_Zayavki_na_sdachy"
python main.py

PAUSE