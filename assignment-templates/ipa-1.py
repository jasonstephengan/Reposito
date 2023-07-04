#savings problem

gross_pay = 40000
tax_rate = 0.25
expenses = 12000.5

def savings(gross_pay, tax_rate, expenses):
    saving = int(gross_pay*(1-tax_rate)-expenses)
    return saving

saving = savings(gross_pay, tax_rate, expenses)
print("Savings:",saving, "pesos")




#material waste problem

total_material = 5000
material_units = "kg"
numjobs = 50
job_consumption = 12

def material_waste(total_material, material_units, numjobs, job_consumption):
    wasted = str(total_material-numjobs*job_consumption) + material_units
    return wasted

wasted = material_waste(total_material, material_units, numjobs, job_consumption)
print("Wasted Amount:", wasted)




#interest problem

principal = 30002
rate = 0.03
periods = 4

def interest(principal, rate, periods):
    final_value = int(principal + (principal*rate*periods))
    return final_value

final_value = interest(principal, rate, periods)
print("Final Investment Value:",final_value, "pesos")




#bmi problem

weight = 180
height = [5, 11]

def body_mass_index(weight, height):
    kg = weight/2.20462
    feet = height[0]
    inches = height [1]
    total_inches = feet*12 + inches
    meter = total_inches/39.37

    bmi = kg / (meter**2)
    return bmi

bmi = body_mass_index(weight, height)
print("BMI:",bmi)

