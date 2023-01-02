# 4. Write a python program to maintain club members, sort on roll numbers in ascending order.
# Write function “Ternary_Search” to search whether particular student is member of club or not.
# Ternary search is modified binary search that divides array into 3 halves instead of two.


def ternarySearch(data, l, r, key):
    if (r >= l):
        mid1 = l + (r - l)//3
        mid2 = r - (r - l)//3
        if (data[mid1] == key):
            return mid1
        if (data[mid2] == key):
            return mid2
        if (key < data[mid1]):
            return ternarySearch(data, l, mid1-1, key)
        elif (key > data[mid2]):
            return ternarySearch(data, mid2+1, r, key)
        else:
            return ternarySearch(data, mid1+1, mid2-1, key)
    return -1


# Main Function
club_member_data = []
club_member_data_dict = {}
while True:
    print("1. Add Member\n2. Sort \n3. Search \n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        try:
            rno, member = input(
                "Enter data in form RollNo <space> Name: ").split(" ")
            rno = int(rno)
        except:
            rno, member = input(
                "Enter data in form RollNo <space> Name: ").split(" ")
            rno = int(rno)
        club_member_data.append((rno, member))
        club_member_data_dict[rno] = member
    elif ch == 2:
        print("Data in unsorted form: ")
        for mem in club_member_data:
            print(mem)
        club_member_data.sort()
        print("Data in sorted form: ")
        for mem in club_member_data:
            print(mem)
    elif ch == 3:
        club_member_data.sort()
        rno_list = [t[0] for t in club_member_data]
        element = int(input("Enter Roll No to search: "))
        value = ternarySearch(rno_list, 0, len(rno_list)-1, element)
        if value == -1:
            print("No Member Found! :(\n")
        else:
            print("Value: ", value)
            print(("Member Found!\n{} => {}\n").format(
                element, club_member_data_dict[element]))
    elif ch == 4:
        print("\nThanks for using the program. \nProgram by Pranav Mehendale\n")
        exit()
    else:
        print("Enter Valid Input")
        continue
