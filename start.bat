:: ����� �� ����� � ����� �� ��⮭� �� ��ࠢ�� ��� � ����
@ECHO off
TITLE ������ �������� ���� � ��������� �������� ������ � �����

ECHO ����� ��� �����
netsh interface set interface "Kassa" enable
TIMEOUT 3 >nul

CD "C:\Users\sonic\PycharmProjects\ROI_Zayavki_na_sdachy"
python main.py

PAUSE