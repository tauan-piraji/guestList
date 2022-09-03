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
            N = open(fileName, 'rt')
            FILE.write(f'{len(N.readlines()) + 1}-{name};{age}\n')
        except Exception as e:
            print(f'\n\033[31mERROR: {e.__cause__}\033[m')
        else:
            print('New guest added')
    finally:
        FILE.close()

def removeGuest(fileName, guest):
    try:
        FILE = open(fileName, 'r')
    except Exception as e:
        print(f'\n\033[31mERROR: {e.__cause__}\033[m')
    else:
        try:
                lines = FILE.readlines()

                # pointer for position
                ptr = 1
                count = 1
                # opening in writing mode
                with open(fileName, 'w') as fw:
                    for line in lines:
                        # we want to remove 5th line
                        if ptr != guest:
                            line = line.replace(str(line.split('-')[0]), str(count))
                            count += 1
                            fw.write(line)
                        if ptr == guest:
                            x = line.split('-')[1]
                            name = x.split(';')[0]
                        ptr += 1

        except Exception as e:
            print(f'\n\033[31mERROR: {e.__cause__}\033[m')
        else:
            print(f'\033[31m{name} removed\033[m')
    finally:
        FILE.close()
