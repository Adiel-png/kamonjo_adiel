def main():
    total_annual_salary = 0

    while True:
        print("1. IT DEPT")
        print("2. ACC DEPT")
        print("3. HR DEPT")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Welcome to IT DEPT")
        elif choice == '2':
            print("Welcome to ACC DEPT")
        elif choice == '3':
            print("Welcome to HR DEPT")
        else:
            print("Invalid choice, please try again.")
            continue

        employee_id = input("Enter employee id: ")
        employee_name = input("Enter employee name: ")
        employee_salary = float(input("Enter employee salary: "))

        annual_salary = employee_salary * 12
        print(f"Salary: {employee_salary}")
        print(f"Annual Salary: {annual_salary}")

        if annual_salary > 60000:
            print("You are making good money")
        else:
            print("You should work more")

        total_annual_salary += annual_salary

        more_employees = input("Do you want to enter more employees? (yes/no): ").lower()
        if more_employees != 'yes':
            break

    print(f"Total annual salary of all employees: {total_annual_salary}")

if __name__ == "__main__":
    main()
