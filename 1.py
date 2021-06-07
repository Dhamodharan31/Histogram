import matplotlib.pyplot as plt
labels=["TAMIL","ENGLISH","MATHS","PHYSICS","CHEMISTRY","CS"]
usuage=[80,90,89,90,89,89]
y_positions=range(len(labels))
plt.bar(y_positions,usuage)
plt.xticks(y_positions,labels)
plt.ylabel("RANGE")
plt.title("MARKS")
plt.shoe()