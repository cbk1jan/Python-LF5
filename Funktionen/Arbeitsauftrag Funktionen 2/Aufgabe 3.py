def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_in_months[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    
    days_up_to_month = 0
    for m in range(1, month):
        dim = days_in_month(year, m)
        if dim is None:
            return None
        days_up_to_month += dim
    
    max_day = days_in_month(year, month)
    if day < 1 or day > max_day:
        return None
    
    return days_up_to_month + day

# Testbeispiel
print(day_of_year(2000, 12, 31))  # → 366 (Schaltjahr)
print(day_of_year(2021, 3, 1))    # → 60
print(day_of_year(2024, 2, 29))   # → 60 (Schaltjahr)
print(day_of_year(2024, 2, 30))   # → None (ungültig)
