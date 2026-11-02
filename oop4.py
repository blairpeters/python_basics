#inheritance

# employee == name, id, department, gender
# salaried -- + salary, tenure
#casual -- rates

class Employee:
    def __init__(self, name:str, id_no:str, department:str, gender:str):
        self.full_names = name
        self.identity_no = id_no
        self.department = department
        self.gender = gender
    def print_details(self):
            print(self.full_names)
            print(self.identity_no)
            print(self.department)
            print(self.gender)
            print("----------------")

    def print_name(self):
        print(self.full_names)

class SalariedEmployee(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, salary:int, tenure:int):
        super().__init__(name, id_no, department, gender)
        self.tenure = tenure
        self.salary = salary

class CasualWorker(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, rate:float):
        super().__init__(name, id_no, department, gender)
        self.rate = rate
    def calc_wage(self, hours:float):
        return hours * self.rate

    #override
    def print_details(self):
        print(f"Rate is : {self.rate} per hour")
        super().print_details()

# ---------------- TEST DATA ----------------

# Create regular employees
employee1 = Employee("John Kamau", "12345678", "IT", "Male")
employee2 = Employee("Mary Wanjiku", "23456789", "Finance", "Female")


# Create salaried employees
salaried1 = SalariedEmployee(
    "Brian Otieno",
    "34567891",
    "Human Resource",
    "Male",
    85000,
    3
)

salaried2 = SalariedEmployee(
    "Grace Akinyi",
    "45678912",
    "IT",
    "Female",
    120000,
    5
)


# Create casual workers
casual1 = CasualWorker(
    "Peter Mwangi",
    "56789123",
    "Security",
    "Male",
    800.50
)

casual2 = CasualWorker(
    "Lucy Njeri",
    "67891234",
    "Cleaning",
    "Female",
    650.00
)


# ---------------- TESTING ----------------

# Test Employee
employee1.print_details()

# Test Salaried Employees
salaried1.print_details()
salaried2.print_details()

# Test Casual Workers
casual1.print_details()
casual2.print_details()

