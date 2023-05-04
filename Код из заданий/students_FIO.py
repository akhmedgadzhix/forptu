# Дополнительное задание к этому:
# Дополнить программу таким образом, чтобы ФИО студента
# начиналась с заглавной буквы независимо от ввода пользователя

def FIO():
    f_, n_, o_ = [], [], []                                     # Создали отдельные списки для фамилий, имен и отчеств
    stud = int(input('Введите количество студентов: '))         # Указали сколько человек будет в нашем списке
    for i in range(stud):
        fio = input('ФИО студента: ')                           # Указываем ФИО полностью
        word_list = fio.split()
        f_.append(word_list[0])
        n_.append(word_list[1])
        o_.append(word_list[2])
    students = {'Фамилии': f_, 'Имена': n_, 'Отчества': o_}
    for key, value in students.items():
        print(key, value)


FIO() # Вызываем инструкцию

