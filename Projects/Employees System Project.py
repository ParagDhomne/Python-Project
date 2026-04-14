# --------------------------------------------Employees System Project-----------------------------------------------------------

# The Employees System Project is a simple Python-based project that showcases the use of object-oriented programming (OOP) principles.
# It includes three main classes: Employee, EmployeesManager, and FrontendManager.
# This project provides a basic example of managing employee data and interactions using OOP concepts.

# Table of Contents
# •	Introduction
# •	Classes
#   o	Employee
#   o	EmployeesManager
#   o	FrontendManager

# Introduction
# The Employees System Project demonstrates the implementation of object-oriented programming concepts in Python.
# It encompasses three primary classes, each serving a distinct purpose:

# Employee
# The Employee class represents an individual employee with the following attributes:
# •	name: The name of the employee.
# •	age: The age of the employee.
# •	salary: The salary of the employee.
# This class provides methods for string representation and formatted output of employee information.

# EmployeesManager
# The EmployeesManager class is responsible for managing a list of employees. It offers functionalities to:
# •	Add a new employee to the list.
# •	List all existing employees.
# •	Delete employees within a specified age range.
# •	Find an employee by their name.
# •	Update an employee's salary by name.

# FrontendManager
# The FrontendManager class provides a user interface for interacting with the EmployeesManager. Users can perform actions such as:
# •	Adding new employees.
# •	Listing existing employees.
# •	Deleting employees based on age range.
# •	Finding an employee by their name.
# •	Updating employee salaries by name.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        return emp

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for i, emp in enumerate(self.employees, 1):
            print(f"\nEmployee {i}")
            print(emp)

    def delete_emp_age_wise(self, a, b):
        before = len(self.employees)
        self.employees = [emp for emp in self.employees if not (a < emp.age < b)]
        return before - len(self.employees)

    def find_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

    def update_salary(self, name, salary):
        emp = self.find_employee(name)
        if emp:
            emp.salary = salary
            return True
        return False


class FrontendManager:
    def __init__(self):
        self.system = EmployeesManager()

    def get_int(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid input! Please enter a number.")

    def get_float(self, message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def run(self):
        while True:
            print("\n-------- Employees System ----------")
            print("1. Add employee")
            print("2. List employees")
            print("3. Delete employee by age range")
            print("4. Find employee")
            print("5. Update employee salary")
            print("6. Exit")

            choice = self.get_int("Enter your choice: ")

            if choice == 1:
                name = input("Enter employee name: ")
                age = self.get_int("Enter employee age: ")
                salary = self.get_float("Enter employee salary: ")

                self.system.add_employee(name, age, salary)
                print("Employee added successfully.")

            elif choice == 2:
                print("\nList of Employees:")
                self.system.list_employees()

            elif choice == 3:
                a = self.get_int("Enter lower age limit: ")
                b = self.get_int("Enter upper age limit: ")

                deleted_count = self.system.delete_emp_age_wise(a, b)

                if deleted_count == 0:
                    print("No employees found in that age range.")
                else:
                    print(f"{deleted_count} employee(s) deleted.")

            elif choice == 4:
                name = input("Enter employee name: ")
                emp = self.system.find_employee(name)

                if emp:
                    print("\nEmployee Found:")
                    print(emp)
                else:
                    print("Employee not found.")

            elif choice == 5:
                name = input("Enter employee name: ")
                salary = self.get_float("Enter new salary: ")

                if self.system.update_salary(name, salary):
                    print("Salary updated successfully.")
                else:
                    print("Employee not found.")

            elif choice == 6:
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = FrontendManager()
    app.run()











