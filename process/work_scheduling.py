# -*- coding: utf-8 -*-
# @File   : view.py
# @Author : Runpeng Zhang
# @Date   : 2020/1/3
# @Desc   : None


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import functools
from time import sleep
import time
from threading import Thread


class Process:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.begin = 0
        self.commit = 0
        self.need = 0
        self.service = 0
        self.source = 0
        self.priority = 0
        self.state = 'Wait'
        self.end = 0
        self.circle = 0
        self.quan = 0
        self.flag = False


class Experiment:
    def __init__(self):
        """model"""
        self.process_finish_list = []
        self.process_ready_list = []
        self.time = 0
        self.algorithm = '先来先服务(FCFS)'

        self.var_id = ' '
        self.var_name = ' '
        self.var_begin = ' '
        self.var_run = ' '
        self.var_need = ' '
        self.var_source = ' '
        self.var_state = ' '

        self.q = 3

        """下面是视图代码"""

        self.root = Tk()
        self.root.title("操作系统实验_作业调度_3117004544_张润鹏")

        self.frame_left_top = Frame(width=600, height=80)
        self.frame_right_top = Frame(width=600, height=80)
        self.frame_middle = Frame(width=1050, height=30)
        # self.frame_center = Frame(width=1050, height=80)
        self.frame_bottom = Frame(width=1050, height=150)
        self.frame_bottom_2 = Frame(width=1050, height=150)
        self.frame_bottom_3 = Frame(width=1050, height=150)

        # 定义左上方区域
        self.left_top_title = Label(self.frame_left_top, text="作业调度算法选择：", font=('Arial', 20))
        self.left_top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

        self.alg_button = IntVar()
        button_1 = Radiobutton(self.frame_left_top, variable=self.alg_button, text='先来先服务(FCFS)', value=0,
                               font=('Arial', 14))
        button_2 = Radiobutton(self.frame_left_top, variable=self.alg_button, text='短作业优先(SJF)', value=1,
                               font=('Arial', 14))
        button_3 = Radiobutton(self.frame_left_top, variable=self.alg_button, text='高响应比优先', value=2,
                               font=('Arial', 14))
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

        # self.var_shijianpian = StringVar()
        # self.right_top_times = ttk.Combobox(self.frame_left_top, width=12, textvariable=self.var_shijianpian,
        #                                      state='readonly')
        # self.right_top_times['values'] = ('1', '2', '3', '4', '5')  # 设置下拉列表的值
        # self.right_top_times.current(2)
        # self.right_top_times.grid(row=1, column=3)

        self.left_top_frame = Frame(self.frame_left_top)
        self.left_top_button1 = Button(self.frame_left_top, text="初始化", command=self.button_init,
                                       font=('Arial', 15))
        self.left_top_button1.grid(row=0, column=2)

        self.left_top_button2 = Button(self.frame_left_top, text="开始运行", command=self.button_run,
                                       font=('Arial', 15))
        self.left_top_button2.grid(row=0, column=3)

        # 定义右上方区域
        self.var_entry_name = StringVar()
        self.var_entry_service = StringVar()
        self.var_entry_source = StringVar()
        self.var_entry_priority = StringVar()

        self.right_top_title = Label(self.frame_right_top, text="添加新作业名字:", font=('Arial', 14))
        self.right_top_titleA = Label(self.frame_right_top, text="服务时间:", font=('Arial', 14))
        self.right_top_titleB = Label(self.frame_right_top, text="所需资源:", font=('Arial', 14))
        self.right_top_titleC = Label(self.frame_right_top, text="优先级:", font=('Arial', 14))

        self.right_top_entryA = ttk.Combobox(self.frame_right_top, width=12, textvariable=self.var_entry_service,
                                             state='readonly')
        self.right_top_entryA['values'] = ('1', '2', '3', '4', '5')  # 设置下拉列表的值
        self.right_top_entryA.current(0)

        self.right_top_entryB = ttk.Combobox(self.frame_right_top, width=12, textvariable=self.var_entry_source,
                                             state='readonly')
        self.right_top_entryB['values'] = ('1', '2', '3', '4', '5')  # 设置下拉列表的值
        self.right_top_entryB.current(0)

        self.right_top_entryC = ttk.Combobox(self.frame_right_top, width=12, textvariable=self.var_entry_priority,
                                             state='readonly')
        self.right_top_entryC['values'] = ('1', '2', '3', '4', '5')  # 设置下拉列表的值
        self.right_top_entryC.current(0)

        self.numberChosen = ttk.Combobox(self.frame_right_top, width=12, textvariable=self.var_entry_name,
                                         state='readonly')
        self.numberChosen['values'] = ('P0', 'P1', 'P2', 'P3', 'P4')  # 设置下拉列表的值
        self.numberChosen.current(0)

        self.right_top_button = Button(self.frame_right_top, text="添加作业", command=self.button_get_value,
                                       font=('Arial', 15))
        self.right_top_title.grid(row=0, column=0)
        self.numberChosen.grid(row=0, column=1)
        self.right_top_titleA.grid(row=1, column=0)
        self.right_top_titleB.grid(row=2, column=0)
        self.right_top_titleC.grid(row=0, column=2)
        self.right_top_entryA.grid(row=1, column=1)
        self.right_top_entryB.grid(row=2, column=1)
        self.right_top_entryC.grid(row=0, column=3)
        self.right_top_button.grid(row=2, column=2, padx=20, pady=20)

        # 定义中间区域
        # self.var_id = StringVar()  # 声明id
        # self.var_name = StringVar()  # 声明name
        # self.var_begin = StringVar()  # 声明开始运行时间
        # self.var_run = StringVar()  # 声明已运行时间
        # self.var_need = StringVar()  # 声明还需要时间
        # self.var_source = StringVar()  # 声明所需资源
        # self.var_service = StringVar()  # 声明服务时间
        # self.var_state = StringVar()  # 声明状态

        self.middle_frame = Frame(self.frame_middle)
        self.middle_frame_title = Label(self.frame_middle, text='正在运行的进程', font=('Arial', 14))
        # self.middle_frame_id = Label(self.frame_middle, text="ID", font=('Arial', 12))
        # self.middle_frame_id_ = Label(self.frame_middle, textvariable=self.var_id, font=('Arial', 12))
        # self.get_id()  # 调用方法更新id
        # self.middle_frame_name = Label(self.frame_middle, text="进程名", font=('Arial', 12))
        # self.middle_frame_name_ = Label(self.frame_middle, textvariable=self.var_name, font=('Arial', 12))
        # self.get_name()  # 调用方法更新name
        # self.middle_frame_begin = Label(self.frame_middle, text="开始运行时间", font=('Arial', 12))
        # self.middle_frame_begin_ = Label(self.frame_middle, textvariable=self.var_begin, font=('Arial', 12))
        # self.get_begin()  # 调用方法更新begin
        # self.middle_frame_run = Label(self.frame_middle, text="已运行时间", font=('Arial', 12))
        # self.middle_frame_run_ = Label(self.frame_middle, textvariable=self.var_run, font=('Arial', 12))
        # self.get_run()  # 调用方法更新run
        # self.middle_frame_need = Label(self.frame_middle, text="还需运行时间", font=('Arial', 12))
        # self.middle_frame_need_ = Label(self.frame_middle, textvariable=self.var_need, font=('Arial', 12))
        # self.get_need()  # 调用方法更新need
        # self.middle_frame_source = Label(self.frame_middle, text="所需资源", font=('Arial', 12))
        # self.middle_frame_source_ = Label(self.frame_middle, textvariable=self.var_source, font=('Arial', 12))
        # self.get_source()  # 调用方法更新source
        # self.middle_frame_service = Label(self.frame_middle, text="服务时间", font=('Arial', 12))
        # self.middle_frame_service_ = Label(self.frame_middle, textvariable=self.var_service, font=('Arial', 12))
        # self.get_service()  # 调用方法更新service
        # self.middle_frame_state = Label(self.frame_middle, text="当前状态", font=('Arial', 12))
        # self.middle_frame_state_ = Label(self.frame_middle, textvariable=self.var_state, font=('Arial', 12))
        # self.get_state()  # 调用方法更新state
        # self.middle_frame = Frame(self.frame_middle)
        self.middle_frame_title1 = Label(self.frame_middle, text='就绪队列', font=('Arial', 14))

        self.middle_frame_title.grid(row=0, column=0)
        # self.middle_frame_id.grid(row=1, column=0)
        # self.middle_frame_id_.grid(row=2, column=0)
        # self.middle_frame_name.grid(row=1, column=1)
        # self.middle_frame_name_.grid(row=2, column=1)
        # self.middle_frame_begin.grid(row=1, column=2)
        # self.middle_frame_begin_.grid(row=2, column=2)
        # self.middle_frame_run.grid(row=1, column=3)
        # self.middle_frame_run_.grid(row=2, column=3)
        # self.middle_frame_need.grid(row=1, column=4)
        # self.middle_frame_need_.grid(row=2, column=4)
        # self.middle_frame_source.grid(row=1, column=5)
        # self.middle_frame_source_.grid(row=2, column=5)
        # self.middle_frame_state.grid(row=1, column=6)
        # self.middle_frame_state_.grid(row=2, column=6)
        self.middle_frame_title1.grid(row=0, column=2)

        # 定义中心列表区域（当前状态）
        self.tree0 = ttk.Treeview(self.frame_middle, show="headings", height=5, columns=("ID", "name", "begin", "run",
                                                                                         "need", "source", "state"))
        self.vbar0 = ttk.Scrollbar(self.frame_middle, orient=VERTICAL, command=self.tree0.yview)
        # 定义树形结构与滚动条
        self.tree0.configure(yscrollcommand=self.vbar0.set)

        # 表格的标题
        self.tree0.column("ID", width=60, anchor="center")
        self.tree0.column("name", width=80, anchor="center")
        self.tree0.column("begin", width=80, anchor="center")
        self.tree0.column("run", width=80, anchor="center")
        self.tree0.column("need", width=80, anchor="center")
        self.tree0.column("source", width=80, anchor="center")
        self.tree0.column("state", width=80, anchor="center")

        self.tree0.heading("ID", text="ID")
        self.tree0.heading("name", text="作业名字")
        self.tree0.heading("begin", text="开始运行时间")
        self.tree0.heading("run", text="已运行时间")
        self.tree0.heading("need", text="还需时间")
        self.tree0.heading("source", text="所需资源")
        self.tree0.heading("state", text="当前状态")

        # 调用方法获取表格内容插入
        self.get_tree0()  # todo
        self.tree0.grid(row=1, column=0, sticky=NSEW)
        self.vbar0.grid(row=1, column=1, sticky=NS)

        # 定义中心列表区域（就绪队列）
        self.tree = ttk.Treeview(self.frame_middle, show="headings", height=5, columns=("ID", "name", "time", "service",
                                                                                        "source", "priority", "state"))
        self.vbar = ttk.Scrollbar(self.frame_middle, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("name", width=80, anchor="center")
        self.tree.column("time", width=80, anchor="center")
        self.tree.column("service", width=80, anchor="center")
        self.tree.column("source", width=80, anchor="center")
        self.tree.column("state", width=80, anchor="center")
        self.tree.column("priority", width=80, anchor="center")

        self.tree.heading("ID", text="ID")
        self.tree.heading("name", text="作业名字")
        self.tree.heading("time", text="提交时间")
        self.tree.heading("service", text="服务时间")
        self.tree.heading("source", text="所需资源")
        self.tree.heading("state", text="状态")
        self.tree.heading("priority", text="优先级")

        # 调用方法获取表格内容插入
        self.get_tree()
        self.tree.grid(row=1, column=2, sticky=NSEW)
        self.vbar.grid(row=1, column=3, sticky=NS)

        """定义中心列表区域（先来先服务调度结果）"""

        # self.middle_bottom = Frame(self.frame_bottom)
        self.bottom_frame_title1 = Label(self.frame_bottom, text='先来先服务调度结果', font=('Arial', 14))
        self.var_fcfs_pin_ = StringVar()
        self.var_fcfs_pin_quan_ = StringVar()
        self.bottom_frame_fcfs_pin = Label(self.frame_bottom, text='平均周转时间:', font=('Arial', 12))
        self.bottom_frame_fcfs_pin_quan = Label(self.frame_bottom, text='平均带权周转时间:', font=('Arial', 12))
        self.bottom_frame_fcfs_pin_ = Label(self.frame_bottom, textvariable=self.var_fcfs_pin_, font=('Arial', 12))
        self.bottom_frame_fcfs_pin_quan_ = Label(self.frame_bottom, textvariable=self.var_fcfs_pin_quan_,
                                                 font=('Arial', 12))

        self.tree2 = ttk.Treeview(self.frame_bottom, show="headings", height=5,
                                  columns=("ID", "name", "begin", "service", "end",
                                           "source", "state", "circle", "quan"))
        self.vbar2 = ttk.Scrollbar(self.frame_bottom, orient=VERTICAL, command=self.tree2.yview)
        # 定义树形结构与滚动条
        self.tree2.configure(yscrollcommand=self.vbar2.set)

        # 表格的标题
        self.tree2.column("ID", width=80, anchor="center")
        self.tree2.column("name", width=100, anchor="center")
        self.tree2.column("begin", width=100, anchor="center")
        self.tree2.column("end", width=100, anchor="center")
        self.tree2.column("service", width=100, anchor="center")
        self.tree2.column("source", width=100, anchor="center")
        self.tree2.column("state", width=100, anchor="center")
        self.tree2.column("circle", width=100, anchor="center")
        self.tree2.column("quan", width=100, anchor="center")

        self.tree2.heading("ID", text="ID")
        self.tree2.heading("name", text="作业名字")
        self.tree2.heading("begin", text="开始时间")
        self.tree2.heading("end", text="完成时间")
        self.tree2.heading("service", text="服务时间")
        self.tree2.heading("source", text="所需资源")
        self.tree2.heading("state", text="状态")
        self.tree2.heading("circle", text="周转时间")
        self.tree2.heading("quan", text="带权周转时间")

        # 调用方法获取表格内容插入
        # self.get_tree()
        self.bottom_frame_title1.grid(row=0, column=0)
        self.bottom_frame_fcfs_pin.grid(row=0, column=2)
        self.bottom_frame_fcfs_pin_.grid(row=0, column=3)
        self.bottom_frame_fcfs_pin_quan.grid(row=1, column=2)
        self.bottom_frame_fcfs_pin_quan_.grid(row=1, column=3)
        self.tree2.grid(row=1, column=0, sticky=NSEW)
        self.vbar2.grid(row=1, column=1, sticky=NS)

        """定义中心列表区域（短作业优先级调度结果）"""

        # self.middle_bottom = Frame(self.frame_bottom)
        self.bottom_frame_title2 = Label(self.frame_bottom_2, text='短作业优先调度结果', font=('Arial', 14))

        self.tree3 = ttk.Treeview(self.frame_bottom_2, show="headings", height=5,
                                  columns=("ID", "name", "begin", "service", "end",
                                           "source", "state", "circle", "quan"))
        self.vbar3 = ttk.Scrollbar(self.frame_bottom_2, orient=VERTICAL, command=self.tree3.yview)
        # 定义树形结构与滚动条
        self.tree3.configure(yscrollcommand=self.vbar3.set)

        # 定义平均周转
        self.var_priority_pin_ = StringVar()
        self.var_priority_pin_quan_ = StringVar()
        self.bottom_frame_priority_pin = Label(self.frame_bottom_2, text='平均周转时间:', font=('Arial', 12))
        self.bottom_frame_priority_pin_quan = Label(self.frame_bottom_2, text='平均带权周转时间:', font=('Arial', 12))
        self.bottom_frame_priority_pin_ = Label(self.frame_bottom_2, textvariable=self.var_priority_pin_,
                                                font=('Arial', 12))
        self.bottom_frame_priority_pin_quan_ = Label(self.frame_bottom_2, textvariable=self.var_priority_pin_quan_,
                                                     font=('Arial', 12))

        # 表格的标题
        self.tree3.column("ID", width=80, anchor="center")
        self.tree3.column("name", width=100, anchor="center")
        self.tree3.column("begin", width=100, anchor="center")
        self.tree3.column("end", width=100, anchor="center")
        self.tree3.column("service", width=100, anchor="center")
        self.tree3.column("source", width=100, anchor="center")
        self.tree3.column("state", width=100, anchor="center")
        self.tree3.column("circle", width=100, anchor="center")
        self.tree3.column("quan", width=100, anchor="center")

        self.tree3.heading("ID", text="ID")
        self.tree3.heading("name", text="进程名字")
        self.tree3.heading("begin", text="开始时间")
        self.tree3.heading("end", text="完成时间")
        self.tree3.heading("service", text="服务时间")
        self.tree3.heading("source", text="所需资源")
        self.tree3.heading("state", text="状态")
        self.tree3.heading("circle", text="周转时间")
        self.tree3.heading("quan", text="带权周转时间")

        # 调用方法获取表格内容插入
        # self.get_tree()
        self.bottom_frame_title2.grid(row=0, column=0)
        self.bottom_frame_priority_pin.grid(row=0, column=2)
        self.bottom_frame_priority_pin_.grid(row=0, column=3)
        self.bottom_frame_priority_pin_quan.grid(row=1, column=2)
        self.bottom_frame_priority_pin_quan_.grid(row=1, column=3)
        self.tree3.grid(row=1, column=0, sticky=NSEW)
        self.vbar3.grid(row=1, column=1, sticky=NS)

        """定义中心列表区域（高响应比优先调度结果）"""

        # self.middle_bottom = Frame(self.frame_bottom)
        self.bottom_frame_title3 = Label(self.frame_bottom_3, text='高响应比优先调度结果', font=('Arial', 14))

        self.tree4 = ttk.Treeview(self.frame_bottom_3, show="headings", height=5,
                                  columns=("ID", "name", "begin", "service", "end",
                                           "source", "state", "circle", "quan"))
        self.vbar4 = ttk.Scrollbar(self.frame_bottom_3, orient=VERTICAL, command=self.tree4.yview)
        # 定义树形结构与滚动条
        self.tree4.configure(yscrollcommand=self.vbar4.set)

        # 定义平均周转
        self.var_rr_pin_ = StringVar()
        self.var_rr_pin_quan_ = StringVar()
        self.bottom_frame_rr_pin = Label(self.frame_bottom_3, text='平均周转时间:', font=('Arial', 12))
        self.bottom_frame_rr_pin_quan = Label(self.frame_bottom_3, text='平均带权周转时间:', font=('Arial', 12))
        self.bottom_frame_rr_pin_ = Label(self.frame_bottom_3, textvariable=self.var_rr_pin_,
                                          font=('Arial', 12))
        self.bottom_frame_rr_pin_quan_ = Label(self.frame_bottom_3, textvariable=self.var_rr_pin_quan_,
                                               font=('Arial', 12))

        # 表格的标题
        self.tree4.column("ID", width=80, anchor="center")
        self.tree4.column("name", width=100, anchor="center")
        self.tree4.column("begin", width=100, anchor="center")
        self.tree4.column("end", width=100, anchor="center")
        self.tree4.column("service", width=100, anchor="center")
        self.tree4.column("source", width=100, anchor="center")
        self.tree4.column("state", width=100, anchor="center")
        self.tree4.column("circle", width=100, anchor="center")
        self.tree4.column("quan", width=100, anchor="center")

        self.tree4.heading("ID", text="ID")
        self.tree4.heading("name", text="进程名字")
        self.tree4.heading("begin", text="开始时间")
        self.tree4.heading("end", text="完成时间")
        self.tree4.heading("service", text="服务时间")
        self.tree4.heading("source", text="所需资源")
        self.tree4.heading("state", text="状态")
        self.tree4.heading("circle", text="周转时间")
        self.tree4.heading("quan", text="带权周转时间")

        # 调用方法获取表格内容插入
        # self.get_tree()
        self.bottom_frame_title3.grid(row=0, column=0)
        self.bottom_frame_rr_pin.grid(row=0, column=2)
        self.bottom_frame_rr_pin_.grid(row=0, column=3)
        self.bottom_frame_rr_pin_quan.grid(row=1, column=2)
        self.bottom_frame_rr_pin_quan_.grid(row=1, column=3)
        self.tree4.grid(row=1, column=0, sticky=NSEW)
        self.vbar4.grid(row=1, column=1, sticky=NS)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=3, pady=5)
        # self.frame_center.grid(row=2, column=0, columnspan=2, padx=4, pady=5)
        self.frame_middle.grid(row=1, column=0, columnspan=4)
        self.frame_bottom.grid(row=3, column=0, columnspan=2)
        self.frame_bottom_2.grid(row=4, column=0, columnspan=2)
        self.frame_bottom_3.grid(row=5, column=0, columnspan=2)

        self.root.mainloop()  # 最后一行

    def ing_init(self):
        self.var_id = ' '
        self.var_name = ' '
        self.var_begin = ' '
        self.var_run = ' '
        self.var_need = ' '
        self.var_source = ' '
        self.var_state = ' '
        self.get_tree0()

    def button_init(self):
        print('button_init!')
        self.time = 0
        self.process_ready_list.clear()
        self.process_finish_list.clear()
        self.ing_init()

    def async(f):
        def wrapper(*args, **kwargs):
            thr = Thread(target=f, args=args, kwargs=kwargs)
            thr.start()

        return wrapper

    @async
    def run_fcfs(self):
        self.process_ready_list.sort(key=functools.cmp_to_key(lambda x, y: x.commit < y.commit))
        tmp_ = self.process_ready_list.copy()
        self.get_tree_fcfs()
        for process in tmp_:
            self.var_id = process.id
            self.var_name = process.name
            self.var_begin = self.time
            self.var_source = process.source
            self.var_state = 'Run'
            del (self.process_ready_list[0])
            tmp = process.need
            process.begin = self.time
            for i in range(int(process.need)):
                self.time += 1
                tmp -= 1
                self.var_need = tmp
                self.var_run = (process.need - tmp)
                self.get_tree0()
                sleep(1)
            process.end = self.time
            process.circle = process.end - process.commit
            process.quan = process.circle / process.service
            process.state = 'Finish'
            self.process_finish_list.append(process)
        self.process_ready_list.clear()
        self.get_tree_fcfs()
        self.ing_init()

    @async
    def run_priority(self):
        self.process_ready_list.sort(key=functools.cmp_to_key(lambda x, y: x.service - y.service))
        tmp_ = self.process_ready_list.copy()
        self.get_tree_priority()
        for process in tmp_:
            self.var_id = process.id
            self.var_name = process.name
            self.var_begin = self.time
            self.var_source = process.source
            self.var_state = 'Run'
            del (self.process_ready_list[0])
            tmp = process.need
            process.begin = self.time
            for i in range(int(process.need)):
                self.time += 1
                tmp -= 1
                self.var_need = tmp
                self.var_run = (process.need - tmp)
                self.get_tree0()
                sleep(1)
            process.end = self.time
            process.circle = process.end - process.commit
            process.quan = process.circle / process.service
            process.state = 'Finish'
            self.process_finish_list.append(process)
        self.process_ready_list.clear()
        self.get_tree_priority()
        self.ing_init()

    @async
    def run_rr(self):
        self.process_ready_list.sort(key=functools.cmp_to_key(lambda x, y: x.commit - y.commit))
        tmp_ = self.process_ready_list.copy()
        self.get_tree_rr()
        while len(tmp_) > 0:
            tmp_.sort(key=functools.cmp_to_key(lambda x, y: (self.time - x.commit + x.service) / x.service - (
                        self.time - y.commit + y.service) / y.service))
            process = tmp_[0]
            self.var_id = process.id
            self.var_name = process.name
            self.var_begin = self.time
            self.var_source = process.source
            self.var_state = 'Run'
            del (self.process_ready_list[0])
            tmp = process.need
            process.begin = self.time
            for i in range(int(process.need)):
                self.time += 1
                tmp -= 1
                self.var_need = tmp
                self.var_run = (process.need - tmp)
                self.get_tree0()
                sleep(1)
            process.end = self.time
            process.circle = process.end - process.commit
            process.quan = process.circle / process.service
            process.state = 'Finish'
            self.process_finish_list.append(process)
            del (tmp_[0])
        self.process_ready_list.clear()
        self.get_tree_rr()
        self.ing_init()

    def button_run(self):
        algorithm_dict = {}
        algorithm_dict[0] = '先来先服务(FCFS)'
        algorithm_dict[1] = '短作业优先(SJF)'
        algorithm_dict[2] = '高响应比优先'
        self.algorithm = algorithm_dict[self.alg_button.get()]
        print('algorithm:', self.algorithm)
        if len(self.process_ready_list) == 0:
            tkinter.messagebox.showinfo('提示', '运行失败，当前就绪队列为空！')
        else:
            if self.algorithm == '先来先服务(FCFS)':
                self.run_fcfs()
            elif self.algorithm == '短作业优先(SJF)':
                self.run_priority()
            elif self.algorithm == '高响应比优先':
                self.run_rr()

    def button_get_value(self):
        """
        按钮“添加进程”，用于获取各项函数选择
        """
        self.time += 1
        process = Process()
        process.name = self.var_entry_name.get()
        process.id = len(self.process_ready_list) + 1
        process.service = int(self.var_entry_service.get())
        process.need = int(self.var_entry_service.get())
        process.source = int(self.var_entry_source.get())
        process.priority = int(self.var_entry_priority.get())
        process.commit = 1 + len(self.process_ready_list)
        process.begin = self.time
        flag = True
        for elem in self.process_ready_list:
            if elem.name == process.name:
                tkinter.messagebox.showinfo('提示', '添加失败，当前作业已在就绪队列')
                flag = False
        if flag:
            self.process_ready_list.append(process)
        print('button_get_value!')
        print('process:', process)

    def get_tree0(self):
        # 删除原节点
        try:
            for _ in map(self.tree0.delete, self.tree0.get_children("")):
                pass
        except Exception as e:
            print(e)
        self.tree0.insert("", "end", values=(
            self.var_id, self.var_name, self.var_begin, self.var_run, self.var_need,
            self.var_source, self.var_state))
        self.tree0.after(500, self.get_tree)

    def get_tree(self):
        # 删除原节点
        try:
            for _ in map(self.tree.delete, self.tree.get_children("")):
                pass
        except Exception as e:
            print(e)
        for i in range(len(self.process_ready_list)):
            self.tree.insert("", "end", values=(
                self.process_ready_list[i].id, self.process_ready_list[i].name, self.process_ready_list[i].begin,
                self.process_ready_list[i].service, self.process_ready_list[i].source,
                self.process_ready_list[i].priority,
                self.process_ready_list[i].state))
        self.tree.after(500, self.get_tree)

    def get_tree_fcfs(self):
        # 删除原节点
        try:
            for _ in map(self.tree2.delete, self.tree2.get_children("")):
                pass
        except Exception as e:
            print(e)
        pin = 0
        pin_quan = 0
        for i in range(len(self.process_finish_list)):
            self.tree2.insert("", "end", values=(
                self.process_finish_list[i].id, self.process_finish_list[i].name, self.process_finish_list[i].commit,
                self.process_finish_list[i].service, self.process_finish_list[i].end,
                self.process_finish_list[i].source,
                self.process_finish_list[i].state, self.process_finish_list[i].circle,
                self.process_finish_list[i].quan))
            pin += self.process_finish_list[i].circle
            pin_quan += self.process_finish_list[i].quan
        if len(self.process_finish_list) > 0:
            self.var_fcfs_pin_.set(format(float(pin) / float(len(self.process_finish_list)), '.2f'))
            self.var_fcfs_pin_quan_.set(format(float(pin_quan) / float(len(self.process_finish_list)), '.2f'))
            self.get_fcfs()
        self.tree2.after(500, self.get_tree_fcfs)

    def get_tree_priority(self):
        # 删除原节点
        try:
            for _ in map(self.tree3.delete, self.tree3.get_children("")):
                pass
        except Exception as e:
            print(e)
        pin = 0
        pin_quan = 0
        for i in range(len(self.process_finish_list)):
            self.tree3.insert("", "end", values=(
                self.process_finish_list[i].id, self.process_finish_list[i].name, self.process_finish_list[i].commit,
                self.process_finish_list[i].service, self.process_finish_list[i].end,
                self.process_finish_list[i].source,
                self.process_finish_list[i].state, self.process_finish_list[i].circle,
                self.process_finish_list[i].quan))
            pin += self.process_finish_list[i].circle
            pin_quan += self.process_finish_list[i].quan
        if len(self.process_finish_list) > 0:
            self.var_priority_pin_.set(format(float(pin) / float(len(self.process_finish_list)), '.2f'))
            self.var_priority_pin_quan_.set(format(float(pin_quan) / float(len(self.process_finish_list)), '.2f'))
            self.get_priority()
        self.tree3.after(500, self.get_tree_priority)

    def get_tree_rr(self):
        # 删除原节点
        try:
            for _ in map(self.tree4.delete, self.tree4.get_children("")):
                pass
        except Exception as e:
            print(e)
        pin = 0
        pin_quan = 0
        for i in range(len(self.process_finish_list)):
            self.tree4.insert("", "end", values=(
                self.process_finish_list[i].id, self.process_finish_list[i].name, self.process_finish_list[i].commit,
                self.process_finish_list[i].service, self.process_finish_list[i].end,
                self.process_finish_list[i].source,
                self.process_finish_list[i].state, self.process_finish_list[i].circle,
                self.process_finish_list[i].quan))
            pin += self.process_finish_list[i].circle
            pin_quan += self.process_finish_list[i].quan
        if len(self.process_finish_list) > 0:
            self.var_rr_pin_.set(format(float(pin) / float(len(self.process_finish_list)), '.2f'))
            self.var_rr_pin_quan_.set(format(float(pin_quan) / float(len(self.process_finish_list)), '.2f'))
            self.get_rr()
        self.tree4.after(500, self.get_tree_rr)

    def get_fcfs(self):
        self.bottom_frame_fcfs_pin_.after(500, self.get_fcfs)
        self.bottom_frame_fcfs_pin_quan_.after(500, self.get_fcfs)

    def get_priority(self):
        self.bottom_frame_priority_pin_.after(500, self.get_priority)
        self.bottom_frame_priority_pin_quan_.after(500, self.get_priority)

    def get_rr(self):
        self.bottom_frame_rr_pin_.after(500, self.get_rr)
        self.bottom_frame_rr_pin_quan_.after(500, self.get_rr)


# class Model:
#     def __init__(self):
#         self.algorithm_index = 0
#         self.algorithm_name = ''
#
#     def update_algorithm(self, index):
#         algorithm_dict = {0: '先来先服务(FCFS)', 1: '优先级调度算法', 2: '轮转调度算法'}
#         self.algorithm_name = algorithm_dict[index]
#         self.algorithm_index = index
#
#
# class Control:
#     def __init__(self):
#         self.view = Experiment()
#         self.model = Model()
#
#     def get_algorithm(self):
#         self.view.button_run.bind("")


if __name__ == '__main__':
    Experiment()
