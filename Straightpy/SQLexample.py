import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

# Uncomment and use this connection statement if you want to use a file based datagbase, the example
# above creates and in memory data base that is flushed on every execution.
# conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_lastname(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

# Get employee using a hardcoded value
emps = get_emps_by_lastname('Doe')
print(emps)

# GEt employee using a variable
employeeLastName = 'Doe'
emps = get_emps_by_lastname(employeeLastName)
print(emps)

# the above statement returns multiple rows, the rows can be iterated through using the following
for row in emps:
    last = row[0]
    first = row[1]
    pay = row[2] 
    print(last, first, pay)

    print(row.__getitem__(0))
    print(emps.__sizeof__())


update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_lastname('Doe')
print(emps)

conn.close()