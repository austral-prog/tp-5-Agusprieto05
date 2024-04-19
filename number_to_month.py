def number_to_month(month):
    months = ("enero", "febrero", "marzo", "abril", "mayo", "junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    if month<=12 and month >=0:
        return months[month-1]
    else:
        return "error"
print(number_to_month(1))
print(number_to_month(12))
print(number_to_month(99))
