from time import sleep

def line(tam = 40):
    print('-' + ('=' * tam) + '-')

def headPrint(txt, tam = 40):
    line()
    print(txt.center(tam))
    line()

def menu(list):
    headPrint('MAIN MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    line()
    while True:
        try:
            opc = readInt('\033[33mYour option: \033[m')
            if opc > len(list):
                print('\033[31mERROR: Please enter a valid option\n\033[m')
                sleep(2)
                continue
        except Exception as e:
                print(f'\n\033[31mERROR: {e.__cause__}\033[m')
                continue
        else:
            return opc

def inputNewGuest():
    """
    :return:Name and age
    """
    conv = []
    while True:
        try:
            name = str(input('Name: '))
        except (ValueError, TypeError):
            print('\n\033[31mERROR: please type only letters.\033[m')
            continue
        except Exception as e:
            print(f'\n\033[31mERROR: {e.__cause__}\033[m')
            continue
        else:
            name += ';'
            conv += name
            conv += str(inputAgeList())
            return conv

def inputAgeList():
    while True:
        try:
            idade = int(input('Age: '))
        except (ValueError, TypeError):
            print('\n\033[31mERROR: Please enter a valid number.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERROR: User chose not to enter this number.\033[m')
            return 0
        except Exception as e:
            print(f'\n\033[31mERROR: {e.__cause__}\033[m')
            continue
        else:
            return idade

def readInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: Please enter a valid number.\033[m')
            continue
        except Exception as e:
            print(f'\n\033[31mERROR: {e.__cause__}\033[m')
            continue
        else:
            return i
