class EmployeeView:
    def display_menu(self):
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee by Name")
        print("5. Display All Employees")
        print("6. Exit")

    def get_input(self, message):
        return input(message)

    def display_employees(self, employees):
        print("\nEmployee List:")
        for employee in employees:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}")

    def display_message(self, message):
        print(message)
