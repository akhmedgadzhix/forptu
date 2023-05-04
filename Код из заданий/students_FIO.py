def FIO():
    f_, n_, o_ = [], [], []
    stud = int(input('Введите количество студентов: '))
    for i in range(stud):
        fio = input('ФИО студента №{i}: ')
        word_list = fio.split()
        f_.append(word_list[0])
        n_.append(word_list[1])
        o_.append(word_list[2])
    students = {'Фамилии': f_, 'Имена': n_, 'Отчества': o_}
    for key, value in students.items():
        print(key, value)


FIO()
