import argparse
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
        return None

def is_valid_date(date_str):
    """Проверяет, существует ли введенная дата в формате DD.MM.YYYY."""
    year = extract_year(date_str)
    if year is None:
        return False
    
    if year < 1 or year > 9999:
        return False
    
    try:
        day, month, _ = map(int, date_str.split('.'))
        
        if month < 1 or month > 12:
            return False
        
        days_in_month = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if day < 1 or day > days_in_month[month - 1]:
            return False
        
        return True
    
    except ValueError:
        return False

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Проверка даты в формате DD.MM.YYYY.")
    parser.add_argument("date", help="Дата для проверки в формате DD.MM.YYYY.")
    args = parser.parse_args()
    year = extract_year(args.date)
    if is_valid_date(args.date):
        print(f"Дата существует.")
        
        if is_leap_year(year):
            print(f"Год високосный.")
        else:
            print("Год не високосный.")
        
    else:
        print("Даты не существует. Пожалуйста, исправьте ошибки в вводе и повторите попытку.")