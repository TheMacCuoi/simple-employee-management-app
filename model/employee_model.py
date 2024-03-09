import sqlite3

class EmployeeModel:
    def __init__(self, db_name='employee_db.sqlite'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT,
                    salary REAL
                )
            ''')

    def add_employee(self, name, position, salary):
        with self.conn:
            self.conn.execute('INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)',
                              (name, position, salary))

    def update_employee(self, employee_id, name, position, salary):
        with self.conn:
            self.conn.execute('''
                UPDATE employees 
                SET name=?, position=?, salary=?
                WHERE id=?
            ''', (name, position, salary, employee_id))

    def delete_employee(self, employee_id):
        with self.conn:
            self.conn.execute('DELETE FROM employees WHERE id=?', (employee_id,))

    def search_employee_by_name(self, name):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM employees WHERE name LIKE ?', (f'%{name}%',))
            return cursor.fetchall()

    def get_all_employees(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM employees')
            return cursor.fetchall()