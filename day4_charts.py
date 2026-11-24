
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv("employees.csv",sep="\t")

# Display the data
print(df.head())

# ---------------------------------
# TASK 1: BAR CHART
# Average salary per department
# ---------------------------------

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(avg_salary.index, avg_salary.values)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()


# ---------------------------------
# TASK 2: HISTOGRAM
# Salary distribution with 5 bins
# ---------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("histogram.png")
plt.show()


# ---------------------------------
# TASK 3: SCATTER PLOT
# Employee ID vs Salary
# Coloured by department
# ---------------------------------

plt.figure(figsize=(8, 5))

for department in df["department"].unique():

    department_data = df[
        df["department"] == department
    ]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")

plt.legend(title="Department")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()


# ---------------------------------
# TASK 4: LINE CHART
# Monthly sales from January to June
# ---------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    linestyle="-",
    label="Monthly Sales"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

print("All four charts created successfully!")




# BONUS: Display all charts in one figure

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# 1. Bar chart
axes[0, 0].bar(avg_salary.index, avg_salary.values)
axes[0, 0].set_title("Average Salary by Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Salary")

# 2. Histogram
axes[0, 1].hist(df["salary"], bins=5, edgecolor="black")
axes[0, 1].set_title("Salary Distribution")
axes[0, 1].set_xlabel("Salary")
axes[0, 1].set_ylabel("Employees")

# 3. Scatter plot
for department in df["department"].unique():
    data = df[df["department"] == department]

    axes[1, 0].scatter(
        data["id"],
        data["salary"],
        label=department
    )

axes[1, 0].set_title("Employee ID vs Salary")
axes[1, 0].set_xlabel("Employee ID")
axes[1, 0].set_ylabel("Salary")
axes[1, 0].legend()

# 4. Line chart
axes[1, 1].plot(months, sales, marker="o")
axes[1, 1].set_title("Monthly Sales")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales")

plt.tight_layout()

plt.savefig("all_charts.png")

plt.show()
