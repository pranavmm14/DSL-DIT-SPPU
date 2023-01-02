# 5. Write a python program to store first year percentage of students in array. 
# Write function for sorting array of floating point
# numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.

def selectionSort(array):
    for i in range(len(array)):
        min_arr = array[i]
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < min_arr:
                min_arr = array[j]
                idx_min = j
        array[i], array[idx_min] = array[idx_min], array[i]

    return array


def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array


def top_five_marks(array):
    for i in range(5):
        print(array[-i-1])

marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = float(input())
    marks.append(ele)  # adding the element

print("The marks of",n,"students are : ")
print(marks)

flag=1
while flag==1:
    print("\n---------------MENU---------------")
    print("1. Selection Sort of the marks")
    print("2. Bubble Sort of the marks")
    print("3. Exit")
    ch=int(input("\n\nEnter your choice (from 1 to 3) : "))

    if ch==1:
        selectionSort(marks)
        a=input("\nDo you want to display top marks from the list (yes/no) : ").capitalize()
        if a=='YES' or a == 'Y':
            top_five_marks(marks)
        elif a=='NO' or a == 'N':
            flag=0
            print("\nThanks for using this program!\nProgram by Pranav Mehendale\n")
        else:
            flag=1

    elif ch==2:
        bubbleSort(marks)
        a = input("\nDo you want to display top five marks from the list (yes/no) : ").capitalize()
        if a=='YES' or a == 'Y':
            top_five_marks(marks)
        elif a=='NO' or a == 'N':
            flag=0
            print("\nThanks for using this program!\nProgram by Pranav Mehendale\n")
        else:
            flag=1

    elif ch==3:
        print("\nThanks for using this program!\nProgram by Pranav Mehendale\n")
        flag=0

    else:
        print("\nThanks for using this program!\nProgram by Pranav Mehendale\n")
        flag=1
