import csv

companies = []
sales = []

with open ("output.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        companies.append(row[0]) 
        sales.append([int(x.replace(",", "")) for x in row[1:]]) 

monthly_sum = [sum(month) for month in zip(*sales)]

yearly_sum = {}
for company, sale in zip(companies, sales):
    yearly_sum[company] = sum(sale)

print(monthly_sum)
print(yearly_sum)
for company, total in yearly_sum.items():
    print(company, total)
