import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("students.csv")


data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)

print("Student Data:\n", data)


top_student = data.loc[data["Average"].idxmax()]
print("\nTop Performer:\n", top_student)


subject_avg = data[["Maths", "Science", "English"]].mean()
print("\nSubject Averages:\n", subject_avg)


subject_avg.plot(kind='bar', title="Subject Average Scores")
plt.ylabel("Marks")
plt.show()
