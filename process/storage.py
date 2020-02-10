# -*- coding: utf-8 -*-
# @File   : storage.py
# @Author : Runpeng Zhang
# @Date   : 2020/1/5
# @Desc   : None


from tkinter import *
from tkinter import ttk
import random
import functools


class Mcb:
    def __init__(self):
        self.id = 0
        self.original_size = 0
        self.rest_size = 0
        self.head_address = 0
        self.work = ' '


class Storage:
    def __init__(self):
        self.rand1 = [0 for i in range(10)]
        self.rand2 = [0 for i in range(10)]
        self.rand3 = [0 for i in range(10)]
        self.stringgrid_memory = [[0 for i in range(5)] for j in range(15)]
        self.stringgrid_work = [[0 for i in range(5)] for j in range(15)]
        self.memory = [Mcb() for i in range(15)]

        """"""
        self.root = Tk()
        self.root.title("操作系统实验_存储管理_3117004544_张润鹏")
        self.frame_left_top = Frame(width=600, height=200)
        self.frame_right_top = Frame(width=600, height=200)
        self.frame_left_bottom = Frame(width=600, height=450)
        self.frame_right_bottom = Frame(width=600, height=450)

        # 定义左上方区域

        # Radiobutton
        # self.alg_button = IntVar()
        # button_1 = Radiobutton(self.frame_left_top, variable=self.alg_button, text='先来先服务(FCFS)', value=0,
        #                        font=('Arial', 14))
        # button_2 = Radiobutton(self.frame_left_top, variable=self.alg_button, text='优先级调度算法', value=1,
        #                        font=('Arial', 14))
        # button_3 = Radiobutton(self.frame_left_top, variable=self.alg_button, text='轮转调度算法', value=2,
        #                        font=('Arial', 14))
        # button_1.grid(row=1, column=0)
        # button_2.grid(row=1, column=1)
        # button_3.grid(row=1, column=2)

        self.left_top_title = Label(self.frame_left_top, text="操作选择：", font=('Arial', 20))
        self.left_top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

        self.left_top_frame = Frame(self.frame_left_top)
        self.left_top_button1 = Button(self.frame_left_top, text="随机生成空闲分区", command=self.button_1,
                                       font=('Arial', 15))
        self.left_top_button1.grid(row=1, column=0)

        self.left_top_button2 = Button(self.frame_left_top, text="随机生成作业", command=self.button_2,
                                       font=('Arial', 15))
        self.left_top_button2.grid(row=1, column=1)

        self.left_top_button3 = Button(self.frame_left_top, text="开始分配", command=self.button_3,
                                       font=('Arial', 15))
        self.left_top_button3.grid(row=1, column=2)

        self.left_top_button4 = Button(self.frame_left_top, text="二次分配", command=self.button_4,
                                       font=('Arial', 15))
        self.left_top_button4.grid(row=2, column=0)

        self.left_top_button5 = Button(self.frame_left_top, text="回收所有资源", command=self.button_5,
                                       font=('Arial', 15))
        self.left_top_button5.grid(row=2, column=1)

        self.left_top_button6 = Button(self.frame_left_top, text="清空", command=self.button_6,
                                       font=('Arial', 15))
        self.left_top_button6.grid(row=2, column=2)

        # 定义右上方区域

        self.right_top_title = Label(self.frame_right_top, text="选择算法:", font=('Arial', 20))

        self.right_top_title.grid(row=0, column=0)

        self.alg_button = IntVar()
        button_1 = Radiobutton(self.frame_right_top, variable=self.alg_button, text='首次适应算法', value=0,
                               font=('Arial', 14))
        button_2 = Radiobutton(self.frame_right_top, variable=self.alg_button, text='循环首次适应算法', value=1,
                               font=('Arial', 14))
        button_3 = Radiobutton(self.frame_right_top, variable=self.alg_button, text='最佳适应算法', value=2,
                               font=('Arial', 14))
        button_4 = Radiobutton(self.frame_right_top, variable=self.alg_button, text='最差适应算法', value=3,
                               font=('Arial', 14))

        self.left_top_button = Button(self.frame_right_top, text="选择", command=self.button_alg,
                                      font=('Arial', 15))
        self.left_top_button.grid(row=3, column=2)

        button_1.grid(row=1, column=1)
        button_2.grid(row=2, column=1)
        button_3.grid(row=3, column=1)
        button_4.grid(row=4, column=1)

        """下方第一个表格"""
        self.tree1 = ttk.Treeview(self.frame_left_bottom, show="headings", height=11,
                                  columns=("ID", "name", "begin", "run", "need"))
        self.vbar1 = ttk.Scrollbar(self.frame_left_bottom, orient=VERTICAL, command=self.tree1.yview)
        # 定义树形结构与滚动条
        self.tree1.configure(yscrollcommand=self.vbar1.set)

        # 表格的标题
        self.tree1.column("ID", width=60, anchor="center")
        self.tree1.column("name", width=80, anchor="center")
        self.tree1.column("begin", width=80, anchor="center")
        self.tree1.column("run", width=80, anchor="center")
        self.tree1.column("need", width=80, anchor="center")

        self.tree1.heading("ID", text="ID")
        self.tree1.heading("name", text="原始空间大小")
        self.tree1.heading("begin", text="剩余空间大小")
        self.tree1.heading("run", text="首地址")
        self.tree1.heading("need", text="分配的作业")

        # 调用方法获取表格内容插入
        self.get_tree1()
        self.tree1.grid(row=0, column=0, sticky=NSEW)
        self.vbar1.grid(row=0, column=1, sticky=NS)

        """下方第二个表格"""
        self.tree2 = ttk.Treeview(self.frame_right_bottom, show="headings", height=11,
                                  columns=("ID", "name", "begin", "run"))
        self.vbar2 = ttk.Scrollbar(self.frame_right_bottom, orient=VERTICAL, command=self.tree2.yview)
        # 定义树形结构与滚动条
        self.tree2.configure(yscrollcommand=self.vbar2.set)

        # 表格的标题
        self.tree2.column("ID", width=60, anchor="center")
        self.tree2.column("name", width=80, anchor="center")
        self.tree2.column("begin", width=80, anchor="center")
        self.tree2.column("run", width=80, anchor="center")

        self.tree2.heading("ID", text="ID")
        self.tree2.heading("name", text="作业大小")
        self.tree2.heading("begin", text="对应区块")
        self.tree2.heading("run", text="状态")

        # 调用方法获取表格内容插入
        self.get_tree2()
        self.tree2.grid(row=0, column=0, sticky=NSEW)
        self.vbar2.grid(row=0, column=1, sticky=NS)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=3, pady=5)
        self.frame_left_bottom.grid(row=1, column=0, columnspan=4)
        self.frame_right_bottom.grid(row=2, column=0, columnspan=2)

        self.root.mainloop()  # 最后一行

    def button_1(self):
        """
        随机生成空闲分区
        :rtype: object
        """
        self.rand1.clear()
        self.rand2.clear()
        for i in range(10):
            self.rand1.append(random.randint(1, 100))
            self.rand2.append(random.randint(1, 100))

        for i in range(10):
            self.stringgrid_memory[i][0] = i
            self.stringgrid_memory[i][1] = self.rand1[i]
            self.stringgrid_memory[i][2] = self.rand1[i]
            self.stringgrid_memory[i][3] = self.rand2[i]

            self.memory[i].id = i
            self.memory[i].original_size = self.rand1[i]
            self.memory[i].rest_size = self.rand1[i]
            self.memory[i].head_address = self.rand2[i]
            self.memory[i].work = self.stringgrid_work[i][3]
        for _ in map(self.tree1.delete, self.tree1.get_children("")):
            pass
        for i in range(10):
            self.tree1.insert("", "end", values=(
                self.stringgrid_memory[i][0], self.stringgrid_memory[i][1], self.stringgrid_memory[i][3],
                self.stringgrid_memory[i][3], ''))

    def button_2(self):
        """
        随机生成作业
        :rtype: object
        """
        self.rand3.clear()
        for i in range(10):
            self.rand3.append(random.randint(1, 100))
            self.stringgrid_work[i][0] = i
            self.stringgrid_work[i][1] = self.rand3[i]
            self.stringgrid_work[i][2] = ''
            self.stringgrid_work[i][3] = "N"
        for _ in map(self.tree2.delete, self.tree2.get_children("")):
            pass
        for i in range(10):
            self.tree2.insert("", "end", values=(
                self.stringgrid_work[i][0], self.stringgrid_work[i][1], self.stringgrid_work[i][2],
                self.stringgrid_work[i][3]))

    def button_3(self):
        """
        开始分配
        :rtype: object
        """
        temp = 1
        if self.alg_button.get() == 0:
            for i in range(10):
                j = 0
                while j < 11:
                    if self.stringgrid_memory[j][2] < self.rand3[i]:
                        break
                    j += 1
                if j > 10:
                    self.stringgrid_work[i][2] = "未分配"
                    self.stringgrid_work[i][3] = "N"
                elif self.stringgrid_memory[j][2] >= self.stringgrid_memory[j][2] - self.rand3[i]:
                    self.stringgrid_memory[j][4] = str(self.stringgrid_memory[j][4]) + "|" + str(j)
                    self.stringgrid_work[i][2] = j
                    self.stringgrid_work[i][3] = "Y"
            self.get_tree1()
            self.get_tree2()
        elif self.alg_button.get() == 1:
            sum = 0
            for i in range(10):
                j = temp
                sum = 1
                while sum < 10:
                    k = j % 10
                    if k == 0:
                        k = k + 10
                    j += 1
                    sum += 1
                    if self.stringgrid_memory[k][2] >= self.rand3[i]:
                        break
                if sum == 10:
                    self.stringgrid_work[i][2] = "未分配"
                    self.stringgrid_work[i][3] = "N"
                elif int(self.stringgrid_memory[k][2]) >= self.rand3[i]:
                    temp = k + 1
                    self.stringgrid_memory[k][2] = self.stringgrid_memory[k][2] - self.rand3[i]
                    self.stringgrid_memory[k][4] = str(self.stringgrid_memory[k][4]) + "|" + str(i)
                    self.stringgrid_work[i][2] = k
                    self.stringgrid_work[i][3] = "Y"
            self.get_tree1()
            self.get_tree2()
        elif self.alg_button.get() == 2:
            for i in range(10):
                j = 0
                while j < 11:
                    if self.memory[j].rest_size >= self.rand3[i]:
                        break
                    j += 1
                if j >= 10:
                    self.stringgrid_work[i][2] = "未分配"
                    self.stringgrid_work[i][3] = "N"
                elif self.memory[j].rest_size >= self.rand3[i]:
                    self.stringgrid_memory[j][2] = int(self.stringgrid_memory[j][2]) - self.rand3[i]
                    self.stringgrid_memory[j][4] = str(self.stringgrid_memory[j][4]) + "|" + str(i)
                    self.memory[j].rest_size = int(self.stringgrid_memory[j][2])
                    self.memory[j].work = self.stringgrid_memory[j][4]
                    self.stringgrid_work[i][2] = self.memory[j].id
                    self.stringgrid_work[i][3] = "Y"
                    self.bullblesort(self.memory)
                    for z in range(10):
                        self.stringgrid_memory[z][0] = self.memory[z].id
                        self.stringgrid_memory[z][1] = self.memory[z].original_size
                        self.stringgrid_memory[z][2] = self.memory[z].rest_size
                        self.stringgrid_memory[z][4] = self.memory[z].head_address
            self.get_tree1()
            self.get_tree2()
        elif self.alg_button.get() == 3:
            self.memory.sort(key=functools.cmp_to_key(lambda x, y: y.rest_size - x.rest_size))
            for i in range(10):
                j = 0
                while j < 11:
                    if int(self.stringgrid_memory[j][2]) < self.rand3[i]:
                        break
                    j += 1
                if j > 10:
                    self.stringgrid_work[i][2] = "未分配"
                    self.stringgrid_work[i][3] = "N"
                elif self.stringgrid_memory[j][2] >= self.stringgrid_memory[j][2] - self.rand3[i]:
                    self.stringgrid_memory[j][4] = str(self.stringgrid_memory[j][4]) + "|" + str(j)
                    self.stringgrid_work[i][2] = j
                    self.stringgrid_work[i][3] = "Y"
            self.get_tree1()
            self.get_tree2()

    def button_4(self):
        """
        二次分配
        :rtype: object
        """
        temp = 1
        for i in range(10):
            if self.stringgrid_work[i][3] == "N":
                if self.alg_button.get() == 1:
                    j = 0
                    while j <= 11:
                        if self.stringgrid_memory[j][2] < self.rand3[i]:
                            break
                        j += 1
                    if j > 10:
                        self.stringgrid_work[i][2] = "未分配"
                        self.stringgrid_work[i][3] = "N"
                    elif int(self.stringgrid_memory[j][2]) >= self.rand3[i]:
                        self.stringgrid_memory[j][2] = int(self.stringgrid_memory[j][2]) - self.rand3[i]
                        self.stringgrid_memory[j][4] = self.stringgrid_memory[j][4] + "|" + i
                        self.stringgrid_work[i][2] = j
                        self.stringgrid_work[i][3] = "Y"
                elif self.alg_button.get() == 2:
                    j = temp
                    sum = 1
                    while sum < 10:
                        k = j % 10
                        sum += 1
                        j += 1
                        if int(self.stringgrid_memory[k][2]) >= self.rand3[i]:
                            break
                    if sum == 10:
                        self.stringgrid_work[i][2] = "未分配"
                        self.stringgrid_work[i][3] = "N"
                    elif int(self.stringgrid_memory[k][2] >= self.rand3[i]):
                        temp = k + 1
                        self.stringgrid_memory[k][2] = int(self.stringgrid_memory[k][2]) - self.rand3[i]
                        self.stringgrid_memory[k][4] = str(self.stringgrid_memory[k][4]) + "|" + str(i)
                        self.stringgrid_work[i][2] = k
                        self.stringgrid_work[i][3] = "Y"
                elif self.alg_button.get() == 3:
                    j = 0
                    while j <= 10 and self.memory[j].rest_size < self.rand3[i]:
                        j += 1
                    if j > 10:
                        self.stringgrid_work[i][2] = "未分配"
                        self.stringgrid_work[i][3] = "N"
                    elif self.memory[j].rest_size >= self.rand3[i]:
                        self.stringgrid_memory[j][2] = int(self.stringgrid_memory[j][2] - self.rand3[i])
                        self.stringgrid_memory[j][4] = str(self.stringgrid_memory[j][4]) +"|" +str(i)
                        self.memory[j].rest_size = int(self.stringgrid_memory[j][2])
                        self.memory[j].work = self.stringgrid_memory[j][4]
                        self.stringgrid_work[i][2] = self.memory[j].id
                        self.stringgrid_work[i][3] = "Y"
                        self.bullblesort(self.memory)
                        for z in range(10):
                            self.stringgrid_memory[z][0] = self.memory[z].id
                            self.stringgrid_memory[z][1] = self.memory[z].original_size
                            self.stringgrid_memory[z][2] = self.memory[z].rest_size
                            self.stringgrid_memory[z][3] = self.memory[z].head_address
                            self.stringgrid_memory[z][4] = self.memory[z].work
        self.get_tree1()
        self.get_tree2()

    def button_5(self):
        """
        回收所有资源
        :rtype: object
        """
        for j in range(10):
            self.stringgrid_memory[j][0] = j
            self.stringgrid_memory[j][1] = self.rand1[j]
            self.stringgrid_memory[j][2] = self.rand1[j]
            self.stringgrid_memory[j][3] = self.rand2[j]
            self.stringgrid_memory[j][4] = ""
            self.memory[j].id = j
            self.memory[j].original_size = self.rand1[j]
            self.memory[j].rest_size = self.rand1[j]
            self.memory[j].head_address = self.rand2[j]
            self.memory[j].work = self.stringgrid_work[j][4]
        for k in range(10):
            self.stringgrid_work[k][0] = k
            self.stringgrid_work[k][1] = self.rand3[k]
            self.stringgrid_work[k][2] = ""
            if self.stringgrid_work[k][3] == "Y":
                self.stringgrid_work[k][3] = "已完成"
        self.get_tree2()
        self.get_tree1()

    def button_6(self):
        """
        清空
        :rtype: object
        """
        for i in range(11):
            for j in range(5):
                self.stringgrid_memory[i][j] = ""
        for i in range(11):
            for j in range(4):
                self.stringgrid_work[i][j] = ""
        self.get_tree1()
        self.get_tree2()

    def button_alg(self):
        if self.alg_button.get() == 0 or self.alg_button.get() == 1:
            for i in range(10):
                self.stringgrid_memory[i][0] = i
                self.stringgrid_memory[i][1] = self.rand1[i]
                self.stringgrid_memory[i][2] = self.rand1[i]
                self.stringgrid_memory[i][3] = self.rand2[i]
                self.stringgrid_memory[i][4] = ""
                self.stringgrid_work[i][0] = i
                self.stringgrid_work[i][1] = self.rand3[i]
                self.stringgrid_work[i][2] = ""
                self.stringgrid_work[i][3] = "N"
            self.get_tree1()
            self.get_tree2()
        elif self.alg_button.get() == 2:
            self.bullblesort(self.memory)
            for i in range(10):
                self.stringgrid_memory[i][0] = self.memory[i].id
                self.stringgrid_memory[i][1] = self.memory[i].original_size
                self.stringgrid_memory[i][2] = self.memory[i].rest_size
                self.stringgrid_memory[i][3] = self.memory[i].head_address
                self.stringgrid_memory[i][4] = self.memory[i].work
                self.stringgrid_work[i][2] = ""
                self.stringgrid_work[i][3] = "N"
                self.stringgrid_work[i][4] = ""
            self.get_tree1()
            self.get_tree2()
        elif self.alg_button.get() == 3:
            print('333')

    def bullblesort(self, alist):
        """
        按照属性排序
        :rtype: object
        """
        alist.sort(key=functools.cmp_to_key(lambda x, y: x.rest_size - y.rest_size))

    def get_tree1(self):
        """
        更新表格1
        :rtype: object
        """
        for _ in map(self.tree1.delete, self.tree1.get_children("")):
            pass
        for i in range(10):
            self.tree1.insert("", "end", values=(
                self.stringgrid_memory[i][0], self.stringgrid_memory[i][1], self.stringgrid_memory[i][3],
                self.stringgrid_memory[i][3], ''))

    def get_tree2(self):
        """
        更新表格2
        :rtype: object
        """
        for _ in map(self.tree2.delete, self.tree2.get_children("")):
            pass
        for i in range(10):
            self.tree2.insert("", "end", values=(
                self.stringgrid_work[i][0], self.stringgrid_work[i][1], self.stringgrid_work[i][2],
                self.stringgrid_work[i][3]))


if __name__ == '__main__':
    try:
        Storage()
    except Exception as e:
        print(e)