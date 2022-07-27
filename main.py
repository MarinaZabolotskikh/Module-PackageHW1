from datetime import datetime
from apllication.DB.people import get_employees
from apllication.salary import calculate_salary

if __name__ == '__main__':
    print(datetime.today().strftime("%d/%m/%y"))
    get_employees()
    calculate_salary()
