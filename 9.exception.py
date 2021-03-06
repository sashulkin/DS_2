# *** Обработка исключений (исключительные события, исключ. ситуации) ***

# Генерация исключения 

# a = 100
# b = 0

# # " деление на ноль" - пример ошибки
# # c = a / b

# # решение - обработка исключений
# # конструкция "try-except"

# try: 
#     c = a / b
#     print("Все окей")
# except:
#     # тут должен быть код, который срабатывает при исключительных ситуцациях
#     # т.е. "запасной" код
#     print("Что-то пошло не так")
#     c = a / 0.1

# # тут может быть код, который выполняется после предыдущего
# print("Result: ", c)

# Обработка множества исключений

# try:
#     var = int(input("Введите число, но не ноль: "))
#     result = 50 / var
# обработка конкретного типа (класса)
# except ZeroDivisionError:
#     print("Вы попытались поделить на ноль!")
#     result = 50 / 1
# except ValueError as val_error:
#     print(f"По-моему, Вы ввели не число. Инфо: {val_error}")
#     result = 0

# обработка общего (базового) исключения
# except Exception as arr:
#     print(f"Что-то пошло не так: {err}")

# print("Result: ", result)

# конструкция "try-except-finally"

# try:
#     var = int(input("Введите число: "))
#     c = 100 / var
#     print("Полет нормальный!")
# except ZeroDivisionError:
#     c = 0 
#     print("Попытка деления на ноль")
# finally:
#     # finally срабатывает в любом случае, даже если программа завершится аварийно
#     # т.е. тут должна быть критически важная логика
#     print("Критически важное действие")

# print("Result", c)

try:
    var = int(input("Введите число: "))
    c = 100 / var
    print("Полет нормальный!")
except ZeroDivisionError:
    c = 0 
    print("Попытка деления на ноль")
else: 
    print("Логика, которая выполняется только если нет исключений")
finally:
    # finally срабатывает в любом случае, даже если программа завершится аварийно
    # т.е. тут должна быть критически важная логика
    print("Критически важное действие")

print("Result", c)