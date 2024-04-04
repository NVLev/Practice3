# Задача 2. Логирование
#
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
# но и записывают эту ошибку в файл.
# Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще
# их исправить. Это называется логированием ошибок.
#
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов,
# из которых можно получить палиндром (привет предыдущим модулям).
# Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает эту ошибку
# в файл errors.log

def check_palindrome(word):
    return word == word[::-1]


# оператор with из 23.5
with open('words.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
    count = 0

    for line in file:
        try:
            clear_line = line.rstrip()
            if clear_line.isalpha():
                count += check_palindrome(clear_line)
            else:
                raise ValueError("строка не полностью состоит из букв!")
        except ValueError as exc:
            log_file.write(str(exc))

    print(count)
