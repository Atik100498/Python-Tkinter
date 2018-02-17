from Tkinter import *
import json
import matplotlib.pyplot as plt
from datetime import *


class DataBase(object):
    filename = 'static1.json'
    filename1 = 'pass1.json'
    filename2 = 'week.json'
    filename3 = 'attendence.json'
    with open(filename, 'r') as file_object:
        subject = json.load(file_object)
    with open(filename1, 'r') as file_object:
        password = json.load(file_object)
    with open(filename2, 'r') as file_object:
        table = json.load(file_object)
    with open(filename3, 'r') as file_object:
        ap = json.load(file_object)

    def __init__(self):
        self.root = Tk()
        self.root.title("menu".upper())
        self.var = IntVar
        self.root.geometry("280x250")
        Label(self.root, text="choose option".upper()).pack()
        self.c1 = Radiobutton(self.root, text="see subjects".upper(), command=self.message1, variable=self.var,
                              value=1).pack(anchor=W)
        self.c2 = Radiobutton(self.root, text="see marks".upper(), command=self.message2, variable=self.var,
                              value=2).pack(anchor=W)
        self.c3 = Radiobutton(self.root, text="see score".upper(), command=self.message3, variable=self.var,
                              value=3).pack(anchor=W)
        self.c4 = Radiobutton(self.root, text="update marks".upper(), command=self.message4, variable=self.var,
                              value=4).pack(anchor=W)
        self.c6 = Radiobutton(self.root, text="change marks".upper(), command=self.login, variable=self.var,
                              value=5).pack(anchor=W)
        self.c5 = Radiobutton(self.root, text="compare marks".upper(), command=self.compare_graph, variable=self.var,
                              value=6).pack(anchor=W)
        self.c7 = Radiobutton(self.root, text="time table".upper(), command=self.table1, variable=self.var,
                              value=7).pack(anchor=W)
        Button(self.root, text="close", command=self.root.quit).pack(anchor=E)
        self.root.mainloop()

    def message1(self):
        root1 = Tk()
        root1.title("subjects".upper())
        root1.geometry("150x145")
        for item in self.subject:
            Label(root1, text=item).pack(anchor=W)
        Button(root1, text="close".upper(), command=root1.quit).pack()
        root1.mainloop()

    def message2(self):
        root2 = Tk()
        root2.title("marks".upper())
        root2.geometry("175x160")
        message = "==================== \n ------subjects------".upper()
        Label(root2, text=message).pack()
        dic = self.subject
        list_ = "C.T 1 C.T 2 C.T 3 C.T 4"
        Label(root2, text=list_).pack()
        for item in dic:
            list_subject = dic[item]
            Label(root2, text=item + str(list_subject)).pack(anchor=W)
        Button(root2, text="close", command=root2.quit).pack()
        root2.mainloop()

    def message3(self):
        root3 = Tk()
        root3.title("score".upper())
        root3.geometry("300x250")
        Label(root3, text="choose subject").pack()
        e1 = Entry(root3)
        e1.pack()

        def get_sub():
            option = e1.get()
            cap_option = option.upper()
            try:
                sub = self.subject[cap_option]
            except KeyError:
                Label(root3, text="enter valid subject".upper()).pack()
            else:
                sum1 = 0
                for item in sub:
                    sum1 += int(item)
                total_marks = sum1
                avg = total_marks / len(sub)
                Label(root3, text=cap_option).pack()
                for item in sub:
                    msg = Message(root3, text=item)
                    msg.pack()
                Label(root3, text="total: ".upper() + str(total_marks)).pack()
                Label(root3, text="average: ".upper() + str(avg)).pack()
                Button(root3, text="close", command=root3.quit).pack()
        Button(root3, text="add", command=get_sub).pack()
        root3.mainloop()

    def message4(self):
        log = Tk()
        log.title("user login".upper())
        Label(log, text="login".upper()).grid()
        Label(log, text="enter id".upper()).grid(row=1, column=0)
        Label(log, text="enter password".upper()).grid(row=2, column=0)
        e1 = Entry(log)
        e2 = Entry(log)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)

        def get():
            dic1 = self.password
            name = str(e1.get())
            e1.delete(0, END)
            e2.delete(0, END)
            for item in dic1:
                if name in dic1:
                    root1 = Tk()
                    root1.title("update marks".upper())
                    root1.geometry("600x575")
                    Label(root1, text="subjects".upper()).pack()
                    for item in self.subject:
                        Label(root1, text=item).pack()
                    Label(root1, text="append subject".upper()).pack()
                    e = Entry(root1)
                    e.pack()

                    def change():
                        a = e.get()
                        cap_a = a.upper()
                        if cap_a in self.subject:
                            list_sub = self.subject[cap_a]
                            for item in list_sub:
                                Label(root1, text=item).pack()
                            Label(root1, text="enter the test no to remove.".upper()).pack()
                            e1 = Entry(root1)
                            e1.pack()

                            def change_sub():
                                a = int(e1.get())
                                try:
                                    del (list_sub[a - 1])
                                except IndexError:
                                    Label(root1, text="enter correct exam number".upper()).pack()
                                else:
                                    Label(root1, text="new marks".upper()).pack()
                                    e2 = Entry(root1)
                                    e2.pack()

                                    def get_new():
                                        new = int(e2.get())
                                        list_sub.insert(a - 1, new)
                                        self.subject[cap_a] = list_sub
                                        with open(self.filename, 'w') as file_object:
                                            json.dump(self.subject, file_object)
                                        for item in list_sub:
                                            Label(root1, text=item).pack()
                                        sum1 = 0
                                        for item in list_sub:
                                            sum1 += int(item)
                                        sum_sub = sum1
                                        avg = sum_sub / (len(list_sub))
                                        Label(root1, text="total: ".upper() + str(sum_sub)).pack()
                                        Label(root1, text="average: ".upper() + str(avg)).pack()

                                    Button(root1, text="enter new marks".upper(), command=get_new).pack()

                            Button(root1, text="change", command=change_sub).pack()
                        else:
                            Message(root1, text="number do not exist".upper()).pack()

                    Button(root1, text="change".upper(), command=change).pack()
                    Button(root1, text="close".upper(), command=root1.quit).pack()
                else:
                    Label(log, text="invalid user".upper()).grid(row=4, column=1)

        Button(log, text="login".upper(), command=get).grid(row=3, column=1)
        log.mainloop()
        root1.mainloop()

    def login(self):
        log = Tk()
        log.title("user login".upper())
        Label(log, text="login".upper()).grid()
        Label(log, text="enter id".upper()).grid(row=1, column=0)
        Label(log, text="enter password".upper()).grid(row=2, column=0)
        e1 = Entry(log)
        e2 = Entry(log)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)

        def get():
            dic1 = self.password
            name = str(e1.get())
            e1.delete(0, END)
            e2.delete(0, END)

        for item in dic1:
            if name in dic1:
                print("============students database============".upper())
                print("enter 'q' to exit.")
                while 5 == 5:
                    ask = raw_input("if new semester enter 'y' or 'n':")
                    if ask == 'y':
                        static = {}
                        while 6 == 6:
                            try:
                                num = input("enter the length: ")
                            except NameError or SyntaxError:
                                print("enter numeric value".upper())
                                continue
                            else:
                                break
                        while 7 == 7:
                            try:
                                num_len = input("enter the number of test: ")
                            except NameError:
                                if num_len == 'q':
                                    break
                                else:
                                    print("enter numeric value".upper())
                                continue
                            else:
                                break
                        for item in range(int(num)):
                            subject_name = raw_input("enter the the name of the subject: ")
                        list_mark = []
                        for item1 in range(int(num_len)):
                            marks = input("enter mark: ")
                            list_mark.append(marks)
                        static[subject_name] = list_mark
                        filename = 'static1.json'
                        with open(filename, 'w') as file_object:
                            json.dump(static, file_object)
                        with open(filename, 'r') as file_object:
                            print(json.load(file_object))
                    elif ask == 'n':
                        print("===================exit=================".upper())
                    elif ask == 'q':
                        break
                    else:
                        print ("invalid input".upper())
                        continue
            else:
                Label(log, text="invalid user".upper()).grid(row=4, column=1)

        Button(log, text="login".upper(), command=get).grid(row=3, column=1)
        log.mainloop()

    def compare_graph(self):
        with open(self.filename, 'r') as file_object:
            dic = json.load(file_object)
        for item in dic:
            list_marks = dic[item]
            y = [1, 2, 3, 4]
        plt.plot(list_marks, y)
        plt.ylabel("c.t(s)".upper())
        plt.xlabel("marks".upper())
        plt.title("compare".upper())
        plt.show()

    def table1(self):
        var = IntVar
        time = Tk()
        time.title("time table".upper())
        dic_table = self.table

        def see():
            Label(time, text=datetime.now()).pack(anchor=E)
            Label(time, text="Enter day").pack()
            e1 = Entry(time)
            e1.pack()

            def get():
                day = e1.get()
                caps_day = day.upper()
                for item in (dic_table[caps_day]):
                    Label(time, text=item).pack(anchor=W)
            Button(time, text="show".upper(), command=get).pack()

        def attandence():
            master = Tk()
            master.title("Attendance")
            for item in self.ap:
                list_at = self.ap[item]
                Label(master, text=item).pack(anchor=W)
                for i in range(len(list_at)):
                    if i == 0:
                        att = float(list_at[0] / list_at[1] * 100)
                        Label(master, text="Present:   " + str(att) + "%").pack(anchor=W)
                    elif i == 1:
                        Label(master, text="total(days):          " + str(list_at[i])).pack(anchor=W)
            master.mainloop()

        def new():
            log = Tk()
            Label(log, text="login".upper()).grid()
            Label(log, text="enter id".upper()).grid(row=1, column=0)
            Label(log, text="enter password".upper()).grid(row=2, column=0)
            e1 = Entry(log)
            e2 = Entry(log)
            e1.grid(row=1, column=1)
            e2.grid(row=2, column=1)

        def get():
            dic1 = self.password
            name = str(e1.get())
            e1.delete(0, END)
            e2.delete(0, END)
            for item in dic1:
                if name in dic1:
                    print("New subjects".upper())
                    sub_num = input("Enter the number of subjects: ")
                    work_day = input("enter the number of working days: ")
                    week = {}
                    list_sub = []
                    for item in range(work_day):
                        day = raw_input("enter day: ")
                        caps_day = day.upper()
                        list_sub = []
                        for item1 in range(sub_num):
                            sub_name = raw_input("enter the subject name: ")
                            caps_sub_name = sub_name.upper()
                            list_sub.append(caps_sub_name)
                            week[caps_day] = list_sub
                    filename = 'week.json'
                    with open(filename, 'w') as file_object:
                        json.dump(week, file_object)
                    print(week)
                    print("New attandence database".upper())
                    atain = []
                    dic = {}
                    sub_num = input("enter the number of subjects: ")
                    for item in range(sub_num):
                        sub_name = raw_input("enter subject name: ".upper())
                        atain = []
                        for i in range(1):
                            a = input("enter period attained: ")
                            b = input("enter the total number of periods: ")
                            atain.append(a)
                            atain.append(b)
                        dic[sub_name.upper()] = atain
                    with open('attendence.json', 'w') as file_object:
                        json.dump(dic, file_object)
                else:
                    Label(log, text="invalid user".upper()).grid(row=4, column=1)
            Button(log, text="login".upper(), command=get).grid(row=3, column=1)
            log.mainloop()

        def update():
            up = Tk()
            up.title("update attandence".upper())
            Label(up, text="Day").grid(row=1)
            e1 = Entry(up)
            e1.grid(row=1, column=1)

            def get_day():
                day = e1.get()
                caps_day = day.upper()
                if caps_day in self.table:
                    list_day = self.table[caps_day]
                    sum1 = 0
                    for item in range(len(list_day)):
                        Label(up, text=list_day[item - 1]).grid(row=item + 2, column=1)
                        sum1 += item
                Label(up, text="Enter Subject").grid(row=sum1 + 2, column=0)
                e4 = Entry(up)
                e4.grid(row=sum1 + 2, column=1)

                def get_sub():
                    sub_name = e4.get()
                    caps_sub_name = sub_name.upper()
                    if caps_sub_name in self.ap:
                        Label(up, text="Subject".upper()).grid(row=sum1 + 3, column=0)
                        Label(up, text=caps_sub_name).grid(row=sum1 + 4, column=0)
                        list_sub_name = self.ap[caps_sub_name]
                        present = float((list_sub_name[0] / list_sub_name[1]) * 100)
                        total = list_sub_name[1]
                        Label(up, text="present (%)".upper()).grid(row=sum1 + 3, column=1)
                        Label(up, text="Total (days)".upper()).grid(row=sum1 + 3, column=2)
                        Label(up, text=str(present) + "%").grid(row=sum1 + 4, column=1)
                        Label(up, text=total).grid(row=sum1 + 4, column=2)
                        Label(up, text=datetime.now()).grid(row=0, column=3)

                        def today_present():
                            list_sub_name.insert(0, int(list_sub_name[0] + 1))
                            list_sub_name.insert(1, int(list_sub_name[1] + 1))
                            list_sub_name.remove(list_sub_name[2])
                            list_sub_name.remove(list_sub_name[2])
                            self.ap[caps_sub_name] = list_sub_name
                            with open(self.filename3, 'w') as file_object:
                                json.dump(self.ap, file_object)

                        def today_absent():
                            list_sub_name.insert(1, int(list_sub_name[1] + 1))
                            print(list_sub_name)
                            del (list_sub_name[2])
                            self.ap[caps_sub_name] = list_sub_name
                            with open(self.filename3, 'w') as file_object:
                                json.dump(self.ap, file_object)

                        Radiobutton(up, text="present".upper(), command=today_present).grid(row=sum1 + 5, column=0)
                        Radiobutton(up, text="absent".upper(), command=today_absent).grid(row=sum1 + 5, column=1)
                    else:
                        Label(up, text="invalid subject!!".upper()).grid(row=sum1 + 4, column=0)

                Button(up, text="get".upper(), command=get_sub).grid(row=sum1 + 2, column=2)
            Button(up, text="Get".upper(), command=get_day).grid(row=1, column=2)

        Radiobutton(time, text="time table".upper(), command=see, variable=var, value=1).pack(anchor=W)
        Radiobutton(time, text="update attandence".upper(), command=update, variable=var, value=2).pack(anchor=W)
        Radiobutton(time, text="attandence".upper(), command=attandence, variable=var, value=3).pack(anchor=W)
        Radiobutton(time, text="new semester".upper(), command=new, variable=var, value=3).pack(anchor=W)
        time.mainloop()

a = DataBase()
