import pandas as pd
import csv


with open('../data/transactions.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

df = pd.read_excel("../data/transactions_excel.xlsx")
print(df.head())
