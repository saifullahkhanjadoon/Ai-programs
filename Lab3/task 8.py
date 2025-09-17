import matplotlib.pyplot as plt

quiz_marks=float(input("Enter marks for Quiz: "))
mid_marks=float(input("Enter marks for Mid: "))
assi_marks=float(input("Enter marks for Assignment: "))

subjects=['Quiz', 'Mid', 'Assignment']
marks=[quiz_marks, mid_marks, assi_marks]
plt.figure(figsize=(10, 5))

plt.bar(subjects,marks,color='black')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()

plt.figure(figsize=(7, 7))
plt.pie(marks,labels=subjects,autopct='%1.1f%%',startangle=90,colors=['gold', 'red', 'orange'])
plt.show()
