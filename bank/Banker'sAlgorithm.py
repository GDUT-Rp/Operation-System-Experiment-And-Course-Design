# -*- coding: utf-8 -*-
# @File   : Banker'sAlgorithm.py
# @Author : Runpeng Zhang
# @Date   : 2020/1/1
# @Desc   : None


Max = [[7, 5, 3],
       [3, 2, 2],
       [9, 0, 2],
       [2, 2, 2],
       [4, 3, 3]]

Allocation = [[0, 1, 1],
              [2, 0, 0],
              [3, 0, 2],
              [2, 1, 1],
              [0, 0, 2]]

Need = [[7, 4, 3],
        [1, 2, 2],
        [6, 0, 0],
        [0, 1, 1],
        [4, 3, 1]]

Available = [3, 3, 2]


def re2Need(request: list, index: int, nd: list):
    ND = nd[index]
    for j in range(len(request)):
        if request[j] <= ND[j]:
            continue
        else:
            print('请求失败，所需资源超过所宣布最大值')
            return False
    return True


def re2Available(re: list, av: list):
    for j in range(len(re)):
        if re[j] <= av[j]:
            continue
        else:
            print('请求失败，当前可用资源不足，请等待')
            return False
    return True


def PreAllocate(Need: list, Available: list, Allocation: list, Request: list, index: int):
    Need_p = Need
    Available_p = Available
    Allocation_p = Allocation
    re_p = Request
    for j in range(len(re_p)):
        Allocation_p[index][j] += re_p[j]
        Need_p[index][j] -= re_p[j]
        Available_p[j] -= re_p[j]
    # print(Allocation_p)
    # print(Need_p)
    # print(Available_p)
    if SafetyDetect(Need_p, Available_p, Allocation_p):
        Need = Need_p
        Available = Available_p
        Allocation = Allocation_p
        print('请求成功，已分配')
        return True
    else:
        print('预分配失败，不安全状态')
        return False


def SafetyDetect(need: list, available: list, allocation: list):
    # step 1
    work = list(available)  # 获得值，而不是引用
    finish = [False] * len(need)
    all_true_flag = False

    print('work:', work)
    print('allocation:', allocation)
    print('need:', need)
    change = True

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
                        finish[i] = True  # 标记该进程已完成
                        change = True
        print(finish)
    for f in finish:
        if not f:
            return False
    return True


if __name__ == '__main__':
    index = 0
    Request = [1, 0, 3]
    index_test = [4]
    request_test = [[3, 3, 0]]
    # Request = [0, 1, 1]
    if re2Need(Request, index, Need) and re2Available(Request, Available):
        PreAllocate(Need, Available, Allocation, Request, index)
