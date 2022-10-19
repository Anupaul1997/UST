

"""
4. Write functions to calculate and display grosssalary and netsalary of an employee after getting input as basicsalary
Write separate functions for allowances and deductions to calculate them respectively

netsalary = grosssalary - deductions
grosssalary = basicsalary + allowances

allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)

deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)

"""


def calc_allowances(basic):
    hra=(22/100)*basic
    da=(18/100)*basic
    ta=(10/100)*basic
    allowance=hra+da+ta
    return allowance

def calc_deduction(basic):
    if(basic>8000):
        prof_tax=200
    else:
        prof_tax:150

    pf=(12/100)*basic
    insurance=(8/100)*basic
    deduction=prof_tax+pf+insurance
    return deduction

    
def gross_salary(basic):
    gross_salary=basic+calc_allowances(basic)
    print("Gross salary:",gross_salary)
    return gross_salary
    

def net_salary(basic):
    net_salary=gross_salary(basic)-calc_deduction(basic)
    print("Net salary:",net_salary)


basic=int(input("Enter the basic salary:"))
net_salary(basic)


