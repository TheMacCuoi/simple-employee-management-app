from model.employee_model import EmployeeModel
from view.employee_view import EmployeeView

class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()
        self.view = EmployeeView()
        self.menu_options = {
            '1': self.add_employee,
            '2': self.update_employee,
            '3': self.delete_employee,
            '4': self.search_employee,
            '5': self.display_employees,
            '6': self.exit_program,
        }

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Enter your choice: ")

            if choice in self.menu_options:
                self.menu_options[choice]()
            else:
                self.view.display_message("Invalid choice. Please try again.")

    def add_employee(self):
        name = self.view.get_input("Enter employee name: ")
        position = self.view.get_input("Enter employee position: ")
        salary = float(self.view.get_input("Enter employee salary: "))
        self.model.add_employee(name, position, salary)
        self.view.display_message("Employee added successfully!")

    def update_employee(self):
        employee_id = int(self.view.get_input("Enter employee ID to update: "))
        name = self.view.get_input("Enter updated name: ")
        position = self.view.get_input("Enter updated position: ")
        salary = float(self.view.get_input("Enter updated salary: "))
        self.model.update_employee(employee_id, name, position, salary)
        self.view.display_message("Employee updated successfully!")

    def delete_employee(self):
        employee_id = int(self.view.get_input("Enter employee ID to delete: "))
        self.model.delete_employee(employee_id)
        self.view.display_message("Employee deleted successfully!")

    def search_employee(self):
        name = self.view.get_input("Enter employee name to search: ")
        employees = self.model.search_employee_by_name(name)
        self.view.display_employees(employees)

    def display_employees(self):
        employees = self.model.get_all_employees()
        self.view.display_employees(employees)

    def exit_program(self):
        self.view.display_message("Exiting program.")
        exit()