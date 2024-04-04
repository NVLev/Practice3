# Задача 2. Старая задача
# Возьмите любую задачу из домашнего задания, например, предыдущего модуля и
# оформите её решение в виде try except finally (можно ещё и else), обрабатывая возможные ошибки.
#
# Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос:
# когда стоит использовать обработку исключений и когда она будет излишней?
import os
def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


try:
    find_file('c:\\', 'hel')
except (TypeError, PermissionError) as exc:
    print(exc, type(exc))
