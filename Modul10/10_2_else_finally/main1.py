# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку. Используйте операторы try except else finally. Обработайте возможные ошибки:
#
# Проблема при открытии файла.
# Нельзя преобразовать данные в целое.
# Неожиданная ошибка.
try:
    rivi = input('Syötä rivi: ')
    tiedosto = open('tiedosto.txt', 'w')
    tiedosto.write(rivi)
except (FileExistsError, PermissionError, FileNotFoundError) as exc:
    print('Virhe! Jokin meni pieleen')
except ValueError as exc:
    print('Virhe! Väärät tiedot')
except Exception as exc:
    print('Vrhe!')
else:
    print('Kaikki on OK')
finally:
    tiedosto.close()
    print('tiedosoto on kiini')

