# **** Генератор паролей ****
from tkinter import Tk, StringVar, Label, Entry, Button 
import hashlib as h 

def hashing():
    """
    Функция шифрования (хеширования)
    """ 
    # строка пароли
    origin_str = pwd.get()
    # кодирование в байт-строку
    byte_str = origin_str.encode()
    # шифрование байт-строки через хеш-Функция
    hash_str = h.sha256(byte_str)
    # преобразование в строку шестнадцатеричного числа (hex-числа)
    hex_str = hash_str.hexdigest()[:8]
    # передача хеш-строки 
    pwd_hash.set(hex_str)
    print(hex_str)
    # print(type(byte_str))

# объект окна
window = Tk() 
# Заголовок окна
window.title("** Password genetare **")
# Переменные с объектами класса StringVar
pwd = StringVar()
pwd_hash = StringVar()

# Текстовая метка созданная виджетом (компонентом, элементом) Label 
label = Label(text="Пароль: ")
# Позиционирование виджета методом grid (сетка)
label.grid(row=0, column=0, padx=5, pady=5)

# Поле ввода строки, созданная виджетом Entry 
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)

# Кнопка
Button(text="Click me", command=hashing).grid(row=1, column=0, padx=5, pady=5)

# Поле вывода хеш-строки 
Entry(textvariable=pwd_hash).grid(row=1, column=1, padx=5, pady=5)

window.mainloop()


