marks = []

for i in range(5):
    num = int(input("Enter marks: "))
    marks.append(num)

print("All Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))