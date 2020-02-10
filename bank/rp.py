# -*- coding: utf-8 -*-
# @File   : rp.py
# @Author : Runpeng Zhang
# @Date   : 2020/1/1
# @Desc   : None


from tkinter import *
from tkinter import ttk
import tkinter.messagebox  # 这个是消息框，对话框的关键


class banker:
    def __init__(self):
        self.Max = [[7, 5, 3],
                    [3, 2, 2],
                    [9, 0, 2],
                    [2, 2, 2],
                    [4, 3, 3]]

        self.Allocation = [[0, 1, 0],
                           [2, 0, 0],
                           [3, 0, 2],
                           [2, 1, 1],
                           [0, 0, 2]]

        self.Need = [[7, 4, 3],
                     [1, 2, 2],
                     [6, 0, 0],
                     [0, 1, 1],
                     [4, 3, 1]]

        self.Available = [3, 3, 2]
        self.Work = [i for i in self.Available]
        self.Work_show = [self.Work, self.Work, self.Work, self.Work, self.Work]
        self.index_list = [i for i in range(5)]
        self.number_index = 0

        self.root = Tk()
        self.root.title("操作系统课程设计_银行家算法演示 3117004544 张润鹏")

        self.frame_left_top = Frame(width=500, height=200)
        self.frame_right_top = Frame(width=600, height=200)
        self.frame_center = Frame(width=1050, height=300)
        self.frame_bottom = Frame(width=1050, height=50)

        # 定义左上方区域
        self.left_top_title = Label(self.frame_left_top, text="进程:P0,P1,P2,P3,P4\n三类资源A:10,B:5,C:7", font=('Arial', 25))
        self.left_top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=30)

        # self.var_success = StringVar()  # 声明成功数
        # self.var_false = StringVar()  # 声明失败数
        self.var_message = StringVar()  # 声明失败数

        self.left_top_frame = Frame(self.frame_left_top)
        self.left_top_button = Button(self.frame_left_top, text="初始化", command=self.button_init,
                                      font=('Arial', 15))
        # self.left_top_frame_left1 = Label(self.frame_left_top, text="打印成功数", font=('Arial', 20))
        # self.left_top_frame_left2 = Label(self.frame_left_top, textvariable=self.var_success, font=('Arial', 15))
        # # self.get_success()  # 调用方法更新成功数
        # self.left_top_frame_right1 = Label(self.frame_left_top, text="打印失败数", font=('Arial', 20))
        # self.left_top_frame_right2 = Label(self.frame_left_top, textvariable=self.var_false, font=('Arial', 15))
        # self.get_false()  # 调用方法更新失败数

        self.left_top_frame_left = Entry(self.frame_left_top, textvariable=self.var_message, width=40)
        self.left_top_button.grid(row=1, column=0)
        self.left_top_frame_left.grid(row=1, column=1)

        # self.left_top_frame_left1.grid(row=1, column=0)
        # self.left_top_frame_left2.grid(row=1, column=1)
        # self.left_top_frame_right1.grid(row=2, column=0)
        # self.left_top_frame_right2.grid(row=2, column=1)

        # 定义右上方区域
        self.var_entry_P = StringVar()
        self.var_entry_A = StringVar()
        self.var_entry_B = StringVar()
        self.var_entry_C = StringVar()

        self.right_top_title = Label(self.frame_right_top, text="进程申请资源:", font=('Arial', 20))
        self.right_top_titleA = Label(self.frame_right_top, text="资源A:", font=('Arial', 20))
        self.right_top_titleB = Label(self.frame_right_top, text="资源B:", font=('Arial', 20))
        self.right_top_titleC = Label(self.frame_right_top, text="资源C:", font=('Arial', 20))
        self.right_top_entryA = Entry(self.frame_right_top, textvariable=self.var_entry_A)
        self.right_top_entryB = Entry(self.frame_right_top, textvariable=self.var_entry_B)
        self.right_top_entryC = Entry(self.frame_right_top, textvariable=self.var_entry_C)

        self.numberChosen = ttk.Combobox(self.frame_right_top, width=12, textvariable=self.var_entry_P,
                                         state='readonly')
        self.numberChosen['values'] = ('P0', 'P1', 'P2', 'P3', 'P4')  # 设置下拉列表的值
        self.numberChosen.current(0)

        self.number = int
        self.right_top_button = Button(self.frame_right_top, text="请求资源", command=self.button_restart,
                                       font=('Arial', 15))
        self.right_top_title.grid(row=0, column=0)
        self.numberChosen.grid(row=0, column=1)
        self.right_top_titleA.grid(row=1, column=0)
        self.right_top_titleB.grid(row=2, column=0)
        self.right_top_titleC.grid(row=3, column=0)
        self.right_top_entryA.grid(row=1, column=1)
        self.right_top_entryB.grid(row=2, column=1)
        self.right_top_entryC.grid(row=3, column=1)
        self.right_top_button.grid(row=2, column=2, padx=20, pady=20)

        # 定义中心列表区域
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=("a", "b", "c", "d",
                                                                                         "aa", "bb", "cc", "e", "f",
                                                                                         "g",
                                                                                         "h", "i", "j", "k", "l", "m",
                                                                                         "n"))
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("a", width=50, anchor="center")
        self.tree.column("b", width=50, anchor="center")
        self.tree.column("c", width=50, anchor="center")
        self.tree.column("d", width=50, anchor="center")
        self.tree.column("aa", width=60, anchor="center")
        self.tree.column("bb", width=60, anchor="center")
        self.tree.column("cc", width=60, anchor="center")
        self.tree.column("e", width=60, anchor="center")
        self.tree.column("f", width=60, anchor="center")
        self.tree.column("g", width=60, anchor="center")
        self.tree.column("h", width=50, anchor="center")
        self.tree.column("i", width=50, anchor="center")
        self.tree.column("j", width=50, anchor="center")
        self.tree.column("k", width=80, anchor="center")
        self.tree.column("l", width=80, anchor="center")
        self.tree.column("m", width=80, anchor="center")
        self.tree.column("n", width=80, anchor="center")

        self.tree.heading("a", text="进程")
        self.tree.heading("b", text="Max_A")
        self.tree.heading("c", text="Max_B")
        self.tree.heading("d", text="Max_C")
        self.tree.heading("aa", text="Need_A")
        self.tree.heading("bb", text="Need_B")
        self.tree.heading("cc", text="Need_C")
        self.tree.heading("e", text="Work_A")
        self.tree.heading("f", text="Work_B")
        self.tree.heading("g", text="Work_C")
        self.tree.heading("h", text="All_A")
        self.tree.heading("i", text="All_B")
        self.tree.heading("j", text="All_C")
        self.tree.heading("k", text="Work+All_A")
        self.tree.heading("l", text="Work+All_B")
        self.tree.heading("m", text="Work+All_C")
        self.tree.heading("n", text="Finish")

        # 调用方法获取表格内容插入
        # self.get_tree()
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.root.mainloop()

    def button_init(self):
        self.Max = [[7, 5, 3],
                    [3, 2, 2],
                    [9, 0, 2],
                    [2, 2, 2],
                    [4, 3, 3]]

        self.Allocation = [[0, 1, 0],
                           [2, 0, 0],
                           [3, 0, 2],
                           [2, 1, 1],
                           [0, 0, 2]]

        self.Need = [[7, 4, 3],
                     [1, 2, 2],
                     [6, 0, 0],
                     [0, 1, 1],
                     [4, 3, 1]]

        self.Available = [3, 3, 2]
        self.Work = [i for i in self.Available]
        self.Work_show = [self.Work, self.Work, self.Work, self.Work, self.Work]
        self.index_list = [i for i in range(5)]
        self.number_index = 0

        for _ in map(self.tree.delete, self.tree.get_children("")):
            pass
        # 更新插入新节点
        # for i in range(len(PrinterPywin32.get_enumjobs())):
        #     self.tree.insert("", "end", values=(i + 1, PrinterPywin32.get_enumjobs()[i]["Submitted"],
        #                                         PrinterPywin32.get_enumjobs()[i]["pPrinterName"],
        #                                         PrinterPywin32.get_enumjobs()[i]["JobId"],
        #                                         PrinterPywin32.get_enumjobs()[i]["Status"]))

        for i in self.index_list:
            self.tree.insert("", "end", values=(
                'P%d' % i, self.Max[i][0], self.Max[i][1], self.Max[i][2], self.Need[i][0], self.Need[i][1],
                self.Need[i][2], self.Work[0], self.Work[1], self.Work[2], self.Allocation[i][0], self.Allocation[i][1],
                self.Allocation[i][2], self.Work[0] + self.Allocation[i][0],
                self.Work[1] + self.Allocation[i][1], self.Work[2] + self.Allocation[i][2], 'False'))
            # self.tree.after(500, self.get_tree)
            self.var_message.set('初始化成功!')

    def button_restart(self):
        # if self.number_index > 0:
            # self.Available = Need
        index = int(self.var_entry_P.get()[1])
        requests = [int(self.var_entry_A.get()), int(self.var_entry_B.get()), int(self.var_entry_C.get())]
        if not self.re2Need(requests, index):
            # tkinter.messagebox.showinfo('提示', '因系统会进入不安全状态，故系统不分配资源!')
            tkinter.messagebox.showinfo('提示', '请求失败，所需资源超过所宣布最大值!')
            self.var_message.set('请求失败，所需资源超过所宣布最大值!')
        else:
            if not self.re2Available(requests, self.Available):
                tkinter.messagebox.showinfo('提示', '请求失败，当前可用资源不足，请等待!')
                self.var_message.set('请求失败，当前可用资源不足，请等待')
            else:
                if not self.PreAllocate(self.Need, self.Available, self.Allocation, requests, index):
                    print('分配失败')
                else:
                    self.number_index += 1  # 分配成功
                    self.tree.insert("", "end", values=(
                        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''))
                    for work_i, i in enumerate(self.index_list):
                        if work_i == 0:
                            self.tree.insert("", "end", values=(
                                'P%d' % i, self.Max[i][0], self.Max[i][1], self.Max[i][2], self.Need[i][0],
                                self.Need[i][1],
                                self.Need[i][2], self.Work[0], self.Work[1],
                                self.Work[2],
                                self.Allocation[i][0], self.Allocation[i][1], self.Allocation[i][2],
                                self.Work_show[work_i][0] + self.Allocation[i][0],
                                self.Work_show[work_i][1] + self.Allocation[i][1],
                                self.Work_show[work_i][2] + self.Allocation[i][2], 'True'))
                        else:
                            self.tree.insert("", "end", values=(
                                'P%d' % i, self.Max[i][0], self.Max[i][1], self.Max[i][2], self.Need[i][0], self.Need[i][1],
                                self.Need[i][2], self.Work_show[work_i - 1][0], self.Work_show[work_i - 1][1],
                                self.Work_show[work_i - 1][2],
                                self.Allocation[i][0], self.Allocation[i][1], self.Allocation[i][2],
                                self.Work_show[work_i - 1][0] + self.Allocation[i][0],
                                self.Work_show[work_i - 1][1] + self.Allocation[i][1],
                                self.Work_show[work_i - 1][2] + self.Allocation[i][2], 'True'))
                        # self.tree.after(500, self.get_tree)
        # self.get_tree()

    def get_message(self):
        print(self.var_message.get())

    # 表格内容插入
    def get_tree(self):
        # 删除原节点
        for _ in map(self.tree.delete, self.tree.get_children("")):
            pass
        # 更新插入新节点
        # for i in range(len(PrinterPywin32.get_enumjobs())):
        #     self.tree.insert("", "end", values=(i + 1, PrinterPywin32.get_enumjobs()[i]["Submitted"],
        #                                         PrinterPywin32.get_enumjobs()[i]["pPrinterName"],
        #                                         PrinterPywin32.get_enumjobs()[i]["JobId"],
        #                                         PrinterPywin32.get_enumjobs()[i]["Status"]))
        self.tree.insert("", "end", values=(
            self.var_entry_P.get(), 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.tree.insert("", "end", values=(
            self.var_entry_P.get(), 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.tree.insert("", "end", values=(
            self.var_entry_P.get(), 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.tree.insert("", "end", values=(
            self.var_entry_P.get(), 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.tree.insert("", "end", values=(
            self.var_entry_P.get(), 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.tree.after(500, self.get_tree)

    # Banker'sAlgorithm
    def re2Need(self, requests: list, index: int):
        ND = self.Need[index]
        for j in range(len(requests)):
            if requests[j] <= ND[j]:
                continue
            else:
                print('请求失败，所需资源超过所宣布最大值')
                return False
        return True

    def re2Available(self, requests: list, av: list):
        print('re2Available_requests:', requests)
        print('re2Available_available:', av)
        for j in range(len(requests)):
            if requests[j] <= av[j]:
                continue
            else:
                print('请求失败，当前可用资源不足，请等待')
                return False
        return True

    def PreAllocate(self, Need: list, Available: list, Allocation: list, Request: list, index: int):
        Need_p = [i for i in Need]
        Available_p = [i for i in Available]
        Allocation_p = [i for i in Allocation]
        re_p = Request
        for j in range(len(re_p)):
            Allocation_p[index][j] += re_p[j]
            Need_p[index][j] -= re_p[j]
            Available_p[j] -= re_p[j]
        # print(Allocation_p)
        # print(Need_p)
        # print(Available_p)
        if self.SafetyDetect(Need_p, Available_p, Allocation_p):
            self.Need = Need_p
            self.Available = Available_p
            self.Allocation = Allocation_p
            self.Work = [i for i in self.Available]
            print('self.Work:', self.Work)
            # for i in range(1, len(self.Need)):
            #     for j in range(len(re_p)):
            # self.Work_show[i][j] = self.Work_show[i - 1][j] + self.Allocation[i - 1][j]

            print('self.need:', self.Need)
            print('self.Available:', self.Available)
            print('self.Allocation:', self.Allocation)
            print('请求成功，已分配')
            tkinter.messagebox.showinfo('提示', '请求成功，已分配')
            self.var_message.set('请求成功，已分配')
            return True
        else:
            print('预分配失败，不安全状态')
            tkinter.messagebox.showinfo('提示', '预分配失败，不安全状态')
            self.var_message.set('预分配失败，不安全状态')
            return False

    def SafetyDetect(self, need: list, available: list, allocation: list):
        # step 1
        work = list(available)  # 获得值，而不是引用
        finish = [False] * len(need)
        all_true_flag = False

        print('work:', work)
        print('allocation:', allocation)
        print('need:', need)
        change = True
        update_list = []
        work_show = []

        # step 2
        while not all_true_flag and change:
            change = False  # 用来标记是否又找到满足条件的进程
            for i in range(len(need)):
                if not finish[i]:
                    miniflag = 0
                    for j in range(len(work)):
                        if need[i][j] <= work[j]:
                            miniflag += 1
                        else:
                            break
                    if miniflag == len(work):
                        # step 3    认为该进程获得资源，可顺利执行，直到完成
                        for j in range(len(work)):
                            work[j] += allocation[i][j]  # 释放该进程已分配的资源
                        print('workwork:', work)
                        # work_show[i] = work
                        work_show.append([i for i in work])
                        print('workshow:', work_show)
                        finish[i] = True  # 标记该进程已完成
                        change = True
                        update_list.append(i)
            print(finish)
        for f in finish:
            if not f:
                return False
        self.index_list = update_list
        self.Work_show = work_show
        print(self.Work_show)
        return True


if __name__ == '__main__':
    banker()
