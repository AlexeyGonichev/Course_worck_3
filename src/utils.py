import json
from datetime import datetime


def load_operations():
    with open('operations.json', 'r') as file:
        data = json.load(file)

    return data

def get_errors():
    operations = []
    for el in load_operations():
        if 'state' in el:
            operations.append(el)
    return operations

def get_executed_operations():
    """фильтруем по проведённым операциям по счёту"""
    new_list_operations = []
    for el in get_errors():
        if el["state"] == "EXECUTED":
            new_list_operations.append(el)

    return new_list_operations

def date_correction():
    """переводим дату в правильный формат"""
    operations_with_data = []
    for el in get_executed_operations():
        date = datetime.strptime(el['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        el['date'] = date
        operations_with_data.append(el)
    return operations_with_data

def sort_data(corr_data):
     list = sorted(corr_data, key=lambda e: '.'.join(reversed(e['date'].split('.'))))
     return list

cor_data = date_correction()

def get_last_5_operations():
    return sort_data(cor_data)[-5:]

def sorted_last_operation():
    last_operations = get_last_5_operations()
    last_operations.reverse()
    return last_operations

def symbols_is_hide():
    """меняем часть символов на звёздочки в соотвествии с требованиями"""
    list_operations = sorted_last_operation()

    for el in list_operations:
        if el['to'][0] == 'С':
            el['to'] ='Счет ' + '**' + el['to'][-4:]
        else:
            el['to'] = el['to'][:-12] + ' ' + el['to'][-11:-9] + '** ' + '**** ' + el['to'][-4:]
        if 'from' in el:
            if el['from'][0] == 'С':
                el['from'] = 'Счет ' + '**' + el['from'][-4:]
            else:
                el['from'] = el['from'][:-12] + ' ' + el['from'][-11:-9] + '** ' + '**** ' + el['from'][-4:]
        else:
            continue
    return list_operations

