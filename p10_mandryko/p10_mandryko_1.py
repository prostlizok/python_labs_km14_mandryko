salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]

changed_salary = list(map(lambda x: round(x * 0.3, 1), salary_list))
changed_salary_list = list(map(lambda x, y: round(x+y, 1), salary_list, changed_salary))

print("Salary table:")
list_output = list(map(lambda x, y, z: print(x, y, z), salary_list, changed_salary_list, changed_salary))

