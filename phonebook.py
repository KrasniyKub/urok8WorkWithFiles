#базовые функции
def input_name():
    return (input('Введите имя: '))

def input_surname():
    return (input('Введите фамилию: '))

def input_patrynomic():
    return (input('Введите отчество: '))

def input_phone():
    return (input('Введите номер телефона: '))

def input_adress():
    return (input('Введите адресс: '))


#копирование строки
def copy_line():
    list = []
    string = ''
    line = int(input('Введите номер строки: '))
    filename = input('Введите имя файла: ')
    with open("phonebook.txt","r",encoding="utf-8") as file:
        contact_list = file.read().rstrip().split("\n")
        for nn,contact_str in enumerate(contact_list,1):
            if nn == line:
                string=contact_str

    with open(filename+".txt","a",encoding="utf-8") as file:
        file.write(string)
        pass
            

#поиск контактов
def search_contact():
    search = input('Введите данные для поиска: ')
    with open("phonebook.txt","r",encoding="utf-8") as file:
        contact_list = file.read().rstrip().split("\n")
    for contact_str in contact_list:
        if search in contact_str:
            print(contact_str)


#вывод контактов
def show_info():
    with open ("phonebook.txt","r", encoding="utf-8") as file:
        print(file.read().rstrip())
        pass
        

#добавление контакта
def create_contact():
    name = input_name()
    surname = input_surname()
    patrynomic = input_patrynomic()
    phone = input_phone()
    address = input_adress()
    return f'{name} {surname} {patrynomic} {phone} {address}\n'

def add_contact(data):
    with open("phonebook.txt","a", encoding="utf-8") as file:
        file.write(data)
        pass


#интерфейс
def interface():
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
              '1. Добавить контакт\n'
              '2. Вывести на экран\n'
              '3. Поиск контакта\n'
              '4. Копировать данные в другой файл\n'
              '5. Выход из программы')
        
        command = input('Введите число: ')
        while command not in ('1', '2', '3', '4', '5'):
            print('Некоректные данные, введите число')
            command = input('Введите число: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copy_line()
            case '5':
                print('Работа заврешена')
                
interface()