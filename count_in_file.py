#Написать программу, которая при запуске принимает 2 вопроса командной строки - имя файла и операция, с ним надо сделать.
#Параметр для следующих файлов: --file <имя файла и путь>, параметр для указания действия: --option <имя параметра>.
#Примечания.
#1. Команда для запуска программы должна выглядеть примерно вот так:
#python count_in_file.py --file <имя_файла> --option <имя_параметра>
#Опции могут быть поменяны местами. Пока предполагаем, что опции ВСЕГДА задаются верно.
#Задания:
#1. Вывести на экран введенные параметры - имя файла и название действия (что указано при запуске)
#2. Реализовать обработку отсутствующих значений для опций.
#3. Реализовать сумение чисел в файле, пропуские буквы и слова. Пример: если в
#1 2 33 привет 10
#программа должна вывести результат суммирования: 46
#3. <продолжение следует>

import sys

if __name__ == "__main__":
    if len (sys.argv) == 1:
        print ("Привет, мир!")
    else:
        if len (sys.argv) < 3:
            print ("Ошибка. Слишком мало параметров.")
            sys.exit (1)

        if len (sys.argv) > 3:
            print ("Ошибка. Слишком много параметров.")
            sys.exit (1)

        param_name = sys.argv[1]
        param_value = sys.argv[2]

        if (param_name == "--name" or
                param_name == "-n"):
            print ("Привет, {}!".format (param_value) )
        else:
            print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
            sys.exit (1)
import os

def file_base_name(file_name):
    if '.' in file_name:
        separator_index = file_name.index('.')
        base_name = file_name[:separator_index]
        return base_name
    else:
        return file_name

def path_base_name(path):
    file_name = os.path.basename(path)
    return file_base_name(file_name)
print ("python count_in_file.py, file,option")
while True:
    file="option"
    if option== "file" :
        print ("1. file_name")
        print ("2. option_name")
	    elif option != 'option':
	        print()
option_name =("option")
верно
print("file_name,option_name")
option_1= 1+2+33+10
option_2=("привет")
print(option_1,option_2)

