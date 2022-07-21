from lesson.employee import Employee, Developer, Lead

#---------------------------------------------------------------
# your code here
class Payroll:

    #init function
def __init__(self, name):
    self.name = name
    self.employee_list = []
    


    #add_employee()
def add_employees(self, employee):
    self.employee_list.append(employee)
    


    #get_payroll()
def get_payroll(self):
    for x in self.employee_list:
        print(x.name + " " + str(x.payment(x.sal)))
    



# ---------------------------------------------------------------



payroll = Payroll("Code Works")

payroll.add_employee(Employee('John', 20))
payroll.add_employee(Developer('Jane', 22))
payroll.add_employee(Lead('Molly', 25))

payroll.get_payroll()
