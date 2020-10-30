# *** Работа с файлами ***

# *** Создание файла и запись в этот файл 
# контекстный менеджер with 
# Режимы функции open:
# w - write (запись)
# a - append (добавление)
# r -  read (чтение)
# with open("hello.txt", "w") as f:
#     f.write("Hello, World!\n")
#     f.write("Hello, Python!\n")

# Добавление новой записи без удаления старых
# with open("hello.txt", "a", encoding="utf8") as f:
#     f.write("Привет мир!\n")

# *** Чтение файла ***
# with open("hello.txt", encoding="utf8") as f:
#     text = f.read(11)
#     print(text)
    
# *** Чтение отдельных строк
# with open("hello.txt", "r", encoding="utf8") as f:
#     row = f.readline()
#     print(row, end="")
#     row = f.readline()
#     print(row,end="")

# Создание списка из строк файла
# with open("hello.txt", "r", encoding="utf8") as f:
#     row_list = f.readlines()
#     # print(row_list)
#     print(row_list[-1])
