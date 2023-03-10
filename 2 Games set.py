'''In second year computer engineering class, group A students play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions)'''


class Student:
    cricket = []
    badminton = []
    football = []
    cNf = []  # Cricket and Football
    cNb = []  # Cricket and Badminton
    bNf = []  # Badminton and Football
    cNbNf = []  # Cricket and Badminton and Football

    def get_data(self):
        self.name = input("Enter Name of student: ")
        self.c = input("Do You Play Cricket [Y/n]: ").capitalize()
        self.b = input("Do You Play badminton [Y/n]: ").capitalize()
        self.f = input("Do You Play football [Y/n]: ").capitalize()
        if "Y" in self.c:
            Student.cricket.append(self.name)
        if "Y" in self.b:
            Student.badminton.append(self.name)
        if "Y" in self.f:
            Student.football.append(self.name)
        if ("Y" in self.c) and ("Y" in self.b) and ("Y" in self.f):
            Student.cNbNf.append(self.name)
        if ("Y" in self.c) and ("Y" in self.b):
            Student.cNb.append(self.name)
        if ("Y" in self.c) and ("Y" in self.f):
            Student.cNf.append(self.name)
        if ("Y" in self.b) and ("Y" in self.f):
            Student.bNf.append(self.name)


while True:
    print("""\
    1) Add Students
    2) List of students who play both cricket and badminton
    3) List of students who play either cricket or badminton but not both
    4) Number of students who play neither cricket nor badminton
    5) Number of students who play cricket and football but not badminton.
    6) Exit\
    """)
    option = int(input("Enter your Choice: "))
    if option == 1:
        obj = Student()
        obj.get_data()
    elif option == 2:
        # Condition a)
        print("List of students who play both cricket and badminton:", Student.cNb)
    elif option == 3:
        # Condition b)
        list_for_B = Student.cricket + Student.badminton
        for a in list_for_B:
            if a in Student.cNb:
                list_for_B.remove(a)
        for a in list_for_B:
            if a in Student.cNb:
                list_for_B.remove(a)
        print("List of students who play either cricket or badminton but not both:", list_for_B)
    elif option == 4:
        # Condition c)
        print("No. of students, neither cricket nor badminton:", len(
            Student.football) - len(Student.bNf) - len(Student.cNf) + len(Student.cNbNf))
    elif option == 5:
        # Condition d)
        print("Number of students who play cricket and football but not badminton:",
              len(Student.cNf) - len(Student.cNbNf))
    elif option == 6:
        print("\nThanks for using the program. \nProgram by Pranav Mehendale\n")
        exit()
    else:
        print('\n==================\nEnter valid input!\n==================')
        continue
