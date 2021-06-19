Student_Height = input("Enter a list of students heights :\n").split()
print(Student_Height)

# calculating the sum of the heights
total_of_height = 0
for height in Student_Height:
    total_of_height += int(height)
print(f"total heights = {total_of_height}")

# calculating the number students
number_of_students = 0
for student in Student_Height:
    number_of_students += 1
print(f"Number of students = {number_of_students}")

# calculating the Average
Average = total_of_height//number_of_students
# // still acts like round function
print(f"Average of student height is: {Average}")