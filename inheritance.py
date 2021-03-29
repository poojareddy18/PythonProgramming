class Employee:
    emp_count = 0
    emp_salaries = []
    def __init__(self, name, family, salary, department):
        self.emp_name = name
        self.emp_family = family
        self.emp_salary = salary
        self.emp_department_name = department
        Employee.emp_count += 1
        Employee.emp_salaries.append(salary)

    def displayEmp(self):
        print("Name : ", self.emp_name, ", Family Name : ", self.emp_family, ", Salary: ", self.emp_salary, ", department: ", self.emp_department_name)
    def get_salary(self):
        total_salaries = 0
        for i in Employee.emp_salaries:
            total_salaries = total_salaries + i
        return total_salaries / len(Employee.emp_salaries)
class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

E1 = Employee("pooja reddy", "gopu", 1000000, "CS")
E2 = Employee("vikranth reddy", "gopu", 1200000, "CSE")
E3 = FullTimeEmployee("jessi", "sahali", 800000, "CS")
E4 = FullTimeEmployee("chicky", "reddy", 600000, "CS")
print("Total Employees are %d" % Employee.emp_count)
avg_salary = E1.get_salary()
print("All the employees together has an average salary of", avg_salary)
print(E1.displayEmp(),E2.displayEmp(),E3.displayEmp(),E4.displayEmp())