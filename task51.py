# Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import json
data = open("BD.json", "r", encoding= 'utf-8')


def search (data):
    with open("BD.json", "r", encoding= 'utf-8') as file:
        data = json.load(file)
    search_name = input("Введите имя > ")
    for item in data["phone response"]:
        if item["name"] == search_name:
            print (item)
# def save (data):
#     new_name = input("Введите имя которое хотите добавить: ")

#     data = open("BD.json", "a", encoding= 'utf-8')
#     data['phone response':{'items'}]       
#     # data['phoneNumbers': {'items'}] = data['phone response':{'items'}:{'name':{new_name}}]
#     print (data)
    
def save(name,lastname,adress,phoneNumber):
    with open('BD.json','r') as jfr:
        jf_file = json.load(jfr)
    with open('BDt.json','w') as jf:
        name, lastname, adress, phoneNumber = input("Введите имя, фамилия, адрес и номер телефона, которые хотите добавить: ").split()
        jf_target = jf_file[0]['phone resopnse']
        user_info = {'name': name, 'lastname': lastname, 'adress': adress, 'phoneNumber':phoneNumber}
        jf_target.append(user_info)
        json.dump(jf_file, jf, indent=4)

            
def scan(data):
    with open("BD.json", "r", encoding= 'utf-8') as file:
        data = json.load(file)
    for i in  data["phone response"]:
        print(i)
    
dict_command = {'1' :  scan, '2' : search, '3' : save}
 
print('''Команды для работы со справочником:
    Просмотр всех записей справочника:  - 1
    Поиск по справочнику -2
    Добавление новой записи - 3 ''')
 
while True:
    command = input('Команда: > ')
    if command == "3":
        name, lastname, adress, phoneNumber = input("Введите имя, фамилия, адрес и номер телефона, которые хотите добавить: ").split()
        save(name,lastname,adress,phoneNumber)
    elif command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')