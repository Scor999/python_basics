# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY                
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.           
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].             
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.          
# Проверку года на високосность вынести в отдельную защищённую функцию.           
# Решить задания, которые не успели решить на семинаре.                           
# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.            
# Запуск в терминале: python dz15final.py 29.02.2024

import logging
import sys

logging.basicConfig(filename='datelog.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def is_leap_year(year):
    """Проверяет, является ли год високосным."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def extract_year(date_str):
    """Извлекает год из строки с датой в формате DD.MM.YYYY."""
    try:
        day, month, year = map(int, date_str.split('.'))
        return year
    except ValueError:
        logger.error("Неверный формат даты: %s", date_str)
        return None

def is_valid_date(date_str):
    """Проверяет, существует ли введенная дата в формате DD.MM.YYYY."""
    year = extract_year(date_str)
    if year is None:
        return False
    
    if year < 1 or year > 9999:
        logger.error("Неверный год: %s", year)
        return False
    
    try:
        day, month, _ = map(int, date_str.split('.'))
        
        if month < 1 or month > 12:
            logger.error("Неверный месяц: %s", month)
            return False
        
        days_in_month = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if day < 1 or day > days_in_month[month - 1]:
            logger.error("Неверный день: %s", day)
            return False
        
        return True
    
    except ValueError:
        logger.error("Неверный формат даты: %s", date_str)
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py DD.MM.YYYY")
        sys.exit(1)
    
    date_str = sys.argv[1]
    logger.info("Проверка даты: %s", date_str)

    if is_valid_date(date_str):
        result = f"Дата {date_str} существует."
        if is_leap_year(extract_year(date_str)):
            result += " Год високосный."
        else:
            result += " Год не високосный."
        
        print(result)
        logger.info(result)
    else:
        error_message = "Неверная дата. Пожалуйста, исправьте ввод и повторите попытку."
        print(error_message)
        logger.error(error_message)