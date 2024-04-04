# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
#
# Напишите программу, которая считывает файл,
# даёт имя для каждого возраста (можно просто использовать буквы алфавита)
# и выводит результат в новый файл result.txt в формате «имя — возраст».
# Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:
#
# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
import string
import random

try:
    vanhuus = open('ages.txt', 'r')
    tulos = open("result.txt", "w")
except (FileExistsError, PermissionError, IsADirectoryError) as exc:
    print('Virhe! Jokin menш pieleen')
randlow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
laskuri = 0
if vanhuus and tulos:
    for rivi in vanhuus:
        try:
            siisti_rivi = rivi.rstrip()
            int(rivi)
            print(siisti_rivi)
            tulos.write(randlow[laskuri] + " - " + siisti_rivi)
            laskuri += 1
        except (ValueError, TypeError) as exc:
            print('Virhe! Jokin meni pieleen')

vanhuus.close()
tulos.close()
