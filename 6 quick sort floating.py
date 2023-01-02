# 6. Write a python program to store first year percentage of students in array.
# Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores.

def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = []
    right = []
    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    return quickSort(left) + [pivot] + quickSort(right)


total_students = int(input("Enter to Total no. of student: "))
global stud_marks
stud_marks = []
for i in range(total_students):
    mark = float(input(("Enter percentage of Student {}: ").format(i+1)))
    stud_marks.append(mark)

print("Sorted marks are: ")
print(stud_marks)
stud_marks = quickSort(stud_marks)
print("Sorted marks are: \n", stud_marks)
print("Top five scores are: \n")
for i in range(5):
    print(stud_marks[-i-1])
print("\nThanks for using the program. \nProgram by Pranav Mehendale\n")
