import json

EMPLOYEE_FILE = "employees.pdf"

def load_employees():
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(employees, file, indent=4)

def add_employee(name, age, department, salary):
    employees = load_employees()
    employees.append({
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    })
    save_employees(employees)

def display_employees():
    employees = load_employees()
    for idx, employee in enumerate(employees, start=1):
        print(f"{idx}. {employee['name']} - {employee['age']} years old - Department: {employee['department']} - Salary: {employee['salary']}")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            department = input("Enter employee department: ")
            salary = input("Enter employee salary: ")
            add_employee(name, age, department, salary)
            print("Employee added successfully!")
        elif choice == "2":
            print("\nEmployees:")
            display_employees()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
