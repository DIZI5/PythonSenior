import logging

# 1. DEBUG - найнижчий рiвень налаштування. Найчастiше використовусться розробниками бiблiотек.
# 2. INFO - рiвень iнформування. вiн створенний для надання повiдомлень про коректну роботу компонентiв програми.
# 3. WARNING - рiвень застережень, якi повiдомляють користувачу про можливу неправильну -
# роботу програми або надають важливу iнформацiю.
# 4. ERROR - рiвень, помилок, якi сповiщають про неправильну роботу функцii або якогось кусочка коду.
# 5. CRITICAL - рiвень критичних помилок, що iнформуе про серйозний -
# збiй роботи програми, через який ii виконання зупинене.

# Налаштування конфігурації потрібно робити на початку програми.
# filename - рядок з шляхом до файлу. Логі заведено зберігати в спеціальний текстовий файл .log
# # filemode - режим відкриття файлу. "а" - режим надо записування тексту. "w" - режим на перезапис тексту.

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s-%(message)s")
logging.debug("debug")
logging.info ("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")

assert 2+2 == 5, "wrong assert"

# Доктесты

"""
>>> 2+2
5
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()