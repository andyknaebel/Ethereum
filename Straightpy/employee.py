# This is a great simple example of a class file.
#
# The calss statement defines this as the Employee Class.  Class names are typically capitalized
# the class has 4 elements, the default sef, then first, last and pay
#
# good example of a propery being defined, email for example returns the email address of the 
# employee as firsname.lastname@email.com
#  
# The def __repr__(self) returns the string "Employee then all the employee attributes"
# dummy comment


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)