def existsFile(fileName):
    """
    :param name:Path
    :return:File exists
    """
    try:
        FILE = open(fileName, 'rt')
        FILE.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(fileName):
    try:
        FILE = open(fileName, 'wt+')
        FILE.close()
    except Exception as e:
        print(f'\n\033[31mERROR: {e.__cause__}\033[m')
    else:
        print(f'File {fileName} created!')

def readFile(fileName):
    try:
        FILE = open(fileName, 'rt')
    except Exception as e:
        print(f'\n\033[31mERROR: {e.__cause__}\033[m')
    else:
        for line in FILE:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} years')
    finally:
        FILE.close()

def register(fileName, name = 'unknown', age = '0'):
    try:
        FILE = open(fileName, 'at')
    except Exception as e:
        print(f'\n\033[31mERROR: {e.__cause__}\033[m')
    else:
        try:
            FILE.write(f'{name};{age}\n')
        except Exception as e:
            print(f'\n\033[31mERROR: {e.__cause__}\033[m')
        else:
            print('New guest added')
    finally:
        FILE.close()
