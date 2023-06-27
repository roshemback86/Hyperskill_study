import re

average = dict()
courses_list = ["Python", "DSA", "Databases", "Flask"]
points = [600, 400, 480, 550]

student_notified = dict()
student_name = dict()
python = dict()
dsa = dict()
databases = dict()
flask = dict()

student_list = dict()
student_progress = dict()
ID = 20000

enrolled = {
           "Python" : 0,
           "DSA" : 0,
           "Databases" : 0,
           "Flask" : 0
}

submissions = {
           "Python" : 0,
           "DSA" : 0,
           "Databases" : 0,
           "Flask" : 0
}

def main():
    print("Learning progress tracker")
    menu()

def menu():
    while True:
        s = input().strip()
        if s == '':
            print('No input.')
            continue
        elif s == 'exit':
            print('Bye!')
            break
        elif s == 'add students':
            add_students()
            continue
        elif s == 'back':
            print("Enter 'exit' to exit the program")
        elif s == 'list':
            if bool(student_list):
                print("Students: ")
                for key in student_list.keys():
                    print(key)
            else:
                print("No students found")
        elif s == 'add points':
            add_points()
        elif s == 'find':
            find_student()
        elif s == 'statistics':
            statistics_menu()
        elif s == 'notify':
            notify()
        else:
            print("Unknown command!")
            continue

def notify():
    n = 0
    for key in student_progress:
        count = 0

        if student_notified[key] == False:
            for i in range(4):
                if student_progress[key][i] == points[i]:
                    print(f"To: {student_list[key]}")
                    print(f"Re: Your Learning Progress")
                    print(f"Hello, {student_name[key]}! You have accomplished our {courses_list[i]} course!")
                    count +=1
            if count > 0:
                student_notified[key] = True
                n +=1

    print(f"Total {n} students have been notified.")

def statistics_menu():
    print("Type the name of a course to see details or 'back' to quit:")
    print_overall()
    while True:
        s = input().strip().lower()
        if s == '':
            print('Unknown course.')
            continue
        elif s == 'back':
            break
        elif s == 'python':
            for key in student_progress.keys():
                if student_progress[key][0] != 0:
                    python[key] = student_progress[key][0]
            newlist = sorted(python.items(), key=lambda item: item[1], reverse=True)
            print("Python")
            print("id    points    completed")
            for el in newlist:
                print(f"{el[0]} {el[1]}        {(el[1] / points[0])*100:.1f}%")

        elif s == 'dsa':
            for key in student_progress.keys():
                if student_progress[key][1] != 0:
                    dsa[key] = student_progress[key][1]
            newlist = sorted(dsa.items(), key=lambda item: item[1], reverse=True)
            print("DSA")
            print("id    points    completed")
            for el in newlist:
                print(f"{el[0]} {el[1]}        {(el[1] / points[1])*100:.1f}%")
        elif s == 'databases':
            for key in student_progress.keys():
                if student_progress[key][2] != 0:
                    databases[key] = student_progress[key][2]
            newlist = sorted(databases.items(), key=lambda item: item[1], reverse=True)
            print("Databases")
            print("id    points    completed")
            for el in newlist:
                print(f"{el[0]} {el[1]}        {(el[1] / points[2])*100:.1f}%")
        elif s == 'flask':
            for key in student_progress.keys():
                if student_progress[key][3] != 0:
                    flask[key] = student_progress[key][3]
            newlist = sorted(flask.items(), key=lambda item: item[1], reverse=True)
            print("Flask")
            print("id    points    completed")
            for el in newlist:
                print(f"{el[0]} {el[1]}        {(el[1] / points[3])*100:.1f}%")
        else:
            print('Unknown course.')
            continue

def print_overall():
    global enrolled
    global submissions
    global student_progress



    max_enrolled = [key for key, value in enrolled.items() if value == max(enrolled.values())]
    min_enrolled = [key for key, value in enrolled.items() if value == min(enrolled.values())]
    max_submissions = [key for key, value in submissions.items() if value == max(submissions.values())]
    min_submissions = [key for key, value in submissions.items() if value == min(submissions.values())]

    if len(max_enrolled) == 4 and enrolled["Python"] == 0:
        print('Most popular: n/a')
        print(f'Least popular: : n/a')
        print(f'Highest activity: : n/a')
        print(f'Lowest activity: : n/a')
        print(f'Easiest course: : n/a')
        print(f'Hardest course: : n/a')

    else:
        l = [0, 0, 0, 0]
        for value in student_progress.values():
            for i in range(4):
                l[i] = l[i] + value[i]
        average = dict()
        for i in range(4):
            if submissions[courses_list[i]] != 0:
                average[courses_list[i]] = l[i] / submissions[courses_list[i]]

        max_average = [key for key, value in average.items() if value == max(average.values())]
        min_average = [key for key, value in average.items() if value == min(average.values())]


        print('Most popular: ', end = '')
        print(*max_enrolled, sep = ", ")
        if len(max_enrolled) == 4:
            print(f'Least popular: : n/a')
        else:
            print(f'Least popular: {min_enrolled[0]}')
        print(f'Highest activity: ', end = '')
        print(*max_submissions)
        if len(max_submissions) == 4:
            print(f'Lowest activity: : n/a')
        else:
            print(f'Lowest activity: {min_submissions[0]}')
        print(f'Easiest course: {max_average[0]}')
        print(f'Hardest course: {min_average[0]}')



def find_student():
    print("Enter an id or 'back' to return ")
    while True:
        s = input().strip()
        if s == 'back':
            return 1
        try:
            id_local = int(s)
            if id_local in student_progress.keys():
                s1 = f'{id_local} points:'
                s2 = f' Python={student_progress[id_local][0]};'
                s3 = f' DSA={student_progress[id_local][1]}'
                s4 = f' Databases={student_progress[id_local][2]};'
                s5 = f' Flask={student_progress[id_local][3]}'
                print(s1 + s2 + s3 + s4 + s5)
            else:
                print(f'No student is found for id={s}.')
        except ValueError:
            print(f'No student is found for id={s}.')
            continue



def add_points():
    global enrolled
    global submissions
    global student_progress

    print("Enter an id and points or 'back' to return: ")
    while True:
        s = input().strip()
        if s == 'back':
            for key in student_progress.keys():
                for i in range(4):
                    if student_progress[key][i] != 0:
                        enrolled[courses_list[i]] +=1
            return 1
        l = s.split()
        try:
            id_local = int(l[0])
        except ValueError:
            print(f"No student is found for id={l[0]}.")
        else:
            try:
                my_list = [int(x) for x in l]
            except ValueError:
                print("Incorrect points format.")
            else:
                my_list.pop(0)
                if id_local not in student_list.keys():
                    print(f"No student is found for id={id_local}.")
                elif len(my_list) != 4:
                    print("Incorrect points format.")
                elif positive_marks(my_list):
                    if id_local not in student_progress.keys():
                        student_progress[id_local] = my_list
                    else:
                        for i in range(4):
                            student_progress[id_local][i - 1] = student_progress[id_local][i - 1] + my_list[i - 1]

                    for i in range(4):
                        if my_list[i] != 0:
                            submissions[courses_list[i]] += 1
                    print("Points updated.")


def positive_marks(my_list):
    for el in my_list:
        if el < 0:
            print("Incorrect points format.")
            return False
    return True


def add_students():
    print("Enter student credentials or 'back' to return:")
    counter = 0
    while True:
        s = input().strip()
        l = s.split()
        if s == 'back':
            print(f'Total {counter} students have been added.')
            return 1
        elif valid_input(l):
            counter +=1
            print(f"The student has been added.")

def valid_input(l):
    if l == []:
        print('Incorrect credentials.')
        return False
    if len(l) < 3:
        print('Incorrect credentials.')
        return False
    email = l[len(l) - 1]
    l.pop()
    full_name = ' '.join(map(str, l))
    try:
        if  not valid_name(l[0]):
            print('Incorrect first name.')
            return False
        l.pop(0)
        for word in l:
            if not valid_name(word):
                print('Incorrect last name.')
                return False
        if not valid_email(email):
            print('Incorrect email.')
            return False
        if not email in student_list.values():
            global ID
            student_list[ID] = email
            student_name[ID] = full_name
            student_notified[ID] = False
            ID +=1
        else:
            print("This email is already taken.")
            return False

        return True
    except IndexError:
        print('Incorrect credentials.')
        return False


def valid_name(s):
    if len(s) < 2:
        return False

    prefixes = ["-", "'"]
    if s.endswith(tuple(prefixes)) or s.startswith(tuple(prefixes)):
        return False
    if "--" in s or "''" in s or "-'" in s or "'-" in s:
        return False
    try:
        s.encode('ascii')
        if s.replace('-','').replace("'","").isalpha():
            return True
    except UnicodeEncodeError:  # string is not ascii
        return False

def valid_email(s):
    counter = 0
    for letter in s:
        if letter == '@':
            counter +=1
        if counter > 1:
            return False
    if not re.match(r"^\S+@\S+\.\S+$", s):
        return False
    return True


if __name__=='__main__':
    main()
