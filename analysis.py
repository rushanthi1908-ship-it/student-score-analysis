import matplotlib.pyplot as plt


students = ["A", "B", "C", "D", "E"]
marks = [78, 85, 90, 66, 74]


average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

plt.bar(students, marks)
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")


plt.savefig("performance_graph.png")


plt.show()
