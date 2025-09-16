from datetime import datetime

EmployeeList = []

numOfEmployeeIn = int(input("How many Employees?: "))

for i in range(numOfEmployeeIn):
    name = input(f"Input Name for Employee {i+1}: ")
    position = input("Input Position: ")
    # timeIn = datetime.utcnow().strftime("%c")
    Employee = {f"Name of Employee {i+1}": name, "Position": position}
    EmployeeList.append(Employee)

print(EmployeeList)

# print("The follwing are the details of the employee")
# print("Name: ", Employee["Name"])
# print("Position: ", Employee["Position"])
# print("Time In: ", Employee["Time In"])


# this
