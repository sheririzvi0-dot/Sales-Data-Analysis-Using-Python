import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Sales Dataset.csv")
df["Date"]=pd.to_datetime(df["Date"])

# Sales Over Time(Line Chart)
daily_sales = df.groupby("Date")["Total Amount"].sum()
plt.figure(figsize=(10,5))
daily_sales.plot()
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Over Time")
plt.grid()
plt.savefig("sales_over_time.png")
plt.show()

#Monthly and Quarterly Aggregation
monthly_sales=df.resample("ME", on="Date")["Total Amount"].sum()
print(monthly_sales)
monthly_sales.plot(kind="bar")
plt.xlabel("Monthly Sales")
plt.ylabel("Total Sales")
plt.title("Monthly sales")
plt.savefig("monthly_sales.png")
plt.show()
quarterly_sales=df.resample("QE", on="Date")["Total Amount"].sum()
print(quarterly_sales)
quarterly_sales.plot(kind="bar")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.title("Quarterly Sales")
plt.savefig("quarterly_sales.png")
plt.show()

#Comparison Category(Bar Chart)
category_sales=df.groupby("Product Category")["Total Amount"].sum()
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.title("Sales by Category")
plt.savefig("category_sales.png")
plt.show()

#Category Share(Pie Chart)
plt.figure(figsize= (8,8))
category_sales.plot(kind="pie" , autopct="%1.1f")
plt.title("Category Share")
plt.savefig("category_share.png")
plt.show()

#Summary
total_sales=df["Total Amount"].sum()
best_category= category_sales.idxmax()
summary= f""" Sales Analysis Report

=====================================
Total Sales:
{total_sales}
Best Performing Category:
{best_category}
Monthly Sales:
{monthly_sales}
Quarterly Sales:
{quarterly_sales}
=====================================
Project Completed  Successfully!
Charts saves as PNG files.
Summary saved as summary.txt"""
with open("summary.txt", "w") as file:
    file.write(summary) 