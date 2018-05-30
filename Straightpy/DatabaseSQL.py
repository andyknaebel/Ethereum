import sqlite3
from employee import Employee

connMem = sqlite3.connect(':memory:')
connDb = sqlite3.connect('employee.db')

cm = connMem.cursor()
cdb = connDb.cursor()

#cdb.execute("""create table employees
# (first text, last text, pay integer)""")

#cdb.execute("insert into employees values ('Andy', 'Knaebel', 50000)")
 
emp_1 = Employee('Gilly', 'Jones', 50000)
emp_2 = Employee('Jane', 'Doe', 67000)

#cdb.execute("insert into employees values (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})


#cdb.execute("select * from employees where last=:last", {'last': emp_1.last})

cdb.execute("select * from employees")
alktest = cdb.fetchall()
for row in alktest:
    print(row)
    print(row[0])
    print(row[1])
    print(row[2])
    emp_3 = Employee(row[0], row[1], row[2])
    print(emp_3.fullname)
    print(emp_3.email)
    print(emp_3)

   
connDb.commit()
connMem.commit()

connDb.close()
connMem.close()




