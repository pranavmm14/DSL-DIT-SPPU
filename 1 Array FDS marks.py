# 1.  Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N  students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency


# Average Score marks score claculation function
def averageMarks(marksList):
    global n
    try:
        total_marks = 0
        for i in range(len(marksList)):
            total_marks += marksList[i]
        return total_marks/n
    except:
        print("Averge Except called!")
        return sum(marksList)/n


# Highest And Lowest score
def highLow(marksList):
    try:
        max = 0
        for i in range(len(marksList)):
            if marksList[i] > max:
                max = marksList[i]

        min = max
        for i in range(len(marksList)):
            if marksList[i] < min:
                min = marksList[i]

        print(("Highest is {} and lowest is {}!").format(max, min))

    except:
        print("Highest Lowest Except called!")
        marksList.sort()
        print(("Highest is {} and lowest is {}!").format(
            marksList[0], marksList[len(marksList)-1]))


# highest Frequency
def highFrequency(marks_list):
    highest_value = 0
    highest_frequency = 0
    frequency_dict = {}

    for value in marks_list:
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    for key, value in frequency_dict.items():
        if value > highest_value:
            highest_frequency = value
            highest_value = key

    print(("Highest frequency is of {} which is {}").format(
        highest_value, highest_frequency))

    return highest_value, highest_frequency


# Main Code
global n
n = int(input("Enter no. of students: "))
FDS_marks = []
present_FDS_marks = []
print("For absent students enter AB!")
absent_count = 0
for i in range(n):
    mark = input(("Enter marks for student {}:").format(i+1)).upper()
    if (mark != 'AB'):
        mark = float(mark)
        present_FDS_marks.append(mark)
    else:
        absent_count += 1

    FDS_marks.append(mark)

# Average marks
print("Average marks of students in the class are:",
      averageMarks(present_FDS_marks))

# Highest and lowest of the list
highLow(present_FDS_marks)

# No. of Absent
print("No. of absent students: ", n-len(present_FDS_marks))

# Highest Frequency of Marks
highFrequency(present_FDS_marks)

print(FDS_marks)
print("\nThanks for using the program. \nProgram by Pranav Mehendale\n")
