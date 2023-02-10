from application.db import people
from application import salary
import datetime

dt = datetime.datetime.today()

if __name__ == '__main__':
    print(dt)
    salary.calculate_salary()
    people.get_employees()