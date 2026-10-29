
marks = [80, 70, 90]

print("Student marks:", marks)

total = sum(marks)
print("Total marks:", total)

average = total / len(marks)
print("Average marks:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
