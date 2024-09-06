def getIncomeTax(salary):
    personal_allowance = 11850
    tax = 0

    taxable_income = max(0, salary - personal_allowance)

    if taxable_income <= 34500:
        tax = taxable_income * 0.20
    elif taxable_income <= 150000:
        tax = 34500 * 0.20 + (taxable_income - 34500) * 0.40
    else:
        tax = 34500 * 0.20 + (150000 - 34500) * 0.40 + (taxable_income - 150000) * 0.45

    return tax

if __name__ == "__main__":
    salaries = [20000, 50000, 100000, 200000]
    for salary in salaries:
        tax = getIncomeTax(salary)
        print(f"Salary: £{salary}, Tax: £{tax:.2f}")
