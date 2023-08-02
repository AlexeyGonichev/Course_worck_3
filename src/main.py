from utils import symbols_is_hide

def start_main():
    """ выводим данные на экран в требуемом виде"""
    for el in symbols_is_hide():
        print(f"{el['date']} {el['description']}")
        if 'from' in el:
            print(f"{el['from']} -> {el['to']}")
        else:
            print(el['to'])
        print(f"{el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    start_main()