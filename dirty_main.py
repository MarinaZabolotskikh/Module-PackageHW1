from datetime import datetime
from apllication.salary import *
from apllication.DB.people import *

print(datetime.today().strftime("%d/%m/%y"))
get_employees()
calculate_salary()