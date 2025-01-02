import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить или редактировать данные по оценкам, предметам, ученикам
        5. Вывод информации по всем оценкам для определенного ученика
        6. Вывод среднего балла по каждому предмету, для определенного ученику
        7. Добавить ученика
        8. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                try:
                # находим сумму оценок по предмету
                    marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                    marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                    print(f'\t{class_} - {marks_sum // marks_count}')
                    print()
                except:
                    print()
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                try:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                    print()
                except:
                    print()
    elif command == 4:
        print('4. Удалить или редактировать данные по оценкам, предметам, ученикам')
        comma = int(input('''
        Введиде 1, если хотите удалить данные по оценкам, предметам, ученикам.
        Введите 2, если хотите редактировать данные по оценкам, предметам, ученикам.
        Введите команду: '''))
        if comma == 1:
            deleted = int(input('''
            Введиде 1, если хотите удалить данные по оценкам
            Введите 2, если хотите удалить данные по предметам
            Введите 3, если хотите удалить данные по ученикам
            Введите команду: '''))
            if deleted == 1:
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                mark = int(input('Введите позицию оценки в списке, которую нужно удалить: ')) - 1
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    students_marks[student][class_].pop(mark)
                    print(f'Для {student} по предмету {class_} удалена оценка которая стоит {mark+1}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            elif deleted == 2:
                student = input('Введите имя ученика: ')
                class_del = input('Введите предмет, который хотите удалить: ')
                if student in students_marks.keys() and class_del in students_marks[student].keys():
                    del students_marks[student][class_del]
                    print(f'Для {student} удален предмет {class_del} ')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            elif deleted == 3:
                print(students)
                student = input('Введите имя ученика, которого нужно удалить: ')
                if student in students_marks.keys():
                    student_del = students.index(student)
                    students.pop(student_del)
                    print(f' {student} удален(а) ')
                else:
                    print('ОШИБКА: неверное имя ученика')
        elif comma == 2:
            redact = int(input('''
                        Введиде 1, если хотите редактировать данные по оценкам
                        Введите 2, если хотите редактировать данные по предметам
                        Введите 3, если хотите редактировать данные по ученикам
                        Введите команду: '''))
            if redact == 1:
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                mark = int(input('Введите позицию оценки в списке, которую нужно изменить: ')) - 1
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    redact_mark = int(input('Введите новое значение оценки: '))
                    students_marks[student][class_][mark] = redact_mark
                    print(f'Для {student} по предмету {class_} изменена оценка которая стоит {mark + 1}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')

            elif redact == 2:
                student = input('Введите имя студента: ')
                print(classes)
                class_ = input('Введите назваине предмета, которое нужно изменить: ')
                if class_ in classes:
                    redact_class= input('Введите новое название предмета: ')
                    students_marks[student][redact_class] = students_marks[student].pop(class_)
                    class_new = classes.append(redact_class)
                    print(f'Изменено имя предмета, новое название: {redact_class}')

            elif redact == 3:
                print(students)
                studentik = input('Введите имя студента: ')
                if studentik in students_marks.keys():
                    redact_student = input('Введите новое имя: ')
                    students_marks[redact_student] = students_marks.pop(studentik)
                    student_redact = students.append(redact_student)
                    print(f'Имя изменено на {redact_student}.')
                    number_student = students.index(studentik)
                    students.pop(number_student)
        else:
            print('Неверная команда!')
    elif command == 5:
        student = input('Введите имя студента: ')
        if student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                try:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                    print()
                except:
                    print()
        else:
            print('Данного ученика нет')
    elif command == 6:
        student = input('Введите имя студента: ')
        if student in students:
            print(student)
        # цикл по предметам
            for class_ in classes:
                try:
                # находим сумму оценок по предмету
                    marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                    marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                    print(f'\t{class_} - {marks_sum // marks_count}')
                    print()
                except:
                    print()
        else:
            print('Данного ученика нет')
    elif command == 7:
        new_student = input("Введите имя нового ученика: ")
        students.append(new_student)
        students_marks[new_student] = {
            "Математика": [],
            "Русский язык": [],
        }
        students.sort()
        print(students_marks)
    elif command == 8:
        print('8. Выход из программы')
        break
    else:
        print('Такой команды нет.')