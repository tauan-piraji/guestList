from utils.func import *
from utils.fileController import *

headPrint('LIST NAME v1.0')

file = 'list'
if not existsFile(file):
    createFile(file)

while True:
    R = menu(['Guest List', 'New Guest', 'Logout'])
    if R == 1:
        headPrint('GUEST LIST')
        readFile(file)
    elif R == 2:
        line()
        headPrint('NEW GUEST')
        name = str(input('Name: '))
        age = readInt('Age: ')
        register(file, name, age)
    elif R == 3:
        headPrint('Leaving the system... see you later!')
        break
