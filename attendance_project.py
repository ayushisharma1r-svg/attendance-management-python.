import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------- Input Section ----------
n = int(input("Enter number of students: "))

names = []
status = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    att = input("Enter P for Present or A for Absent: ").upper()
    
    names.append(name)
    
    if att == 'P':
        status.append(1)   # Present = 1
    else:
        status.append(0)   # Absent = 0

# ---------- DataFrame ----------
data = {
    "Name": names,
    "Attendance": status
}

df = pd.DataFrame(data)

# ---------- Attendance Calculation ----------
total_classes = 1   # ek din ka example
df["Attendance %"] = (df["Attendance"] / total_classes) * 100

print("\n--- Attendance Record ---")
print(df)

# ---------- Summary ----------
present = np.sum(status)
absent = n - present

print("\nTotal Present:", present)
print("Total Absent:", absent)

# ---------- Visualization ----------
labels = ['Present', 'Absent']
values = [present, absent]

plt.figure()
plt.bar(labels, values)
plt.title("Attendance Report")
plt.xlabel("Status")
plt.ylabel("Number of Students")
plt.show()
df.to_csv("attendance_record.csv", index=False)
print("Attendance file saved successfully!")

