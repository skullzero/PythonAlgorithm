"""
「选择排序 selection sort」的工作原理非常直接：开启一个循环，每轮从未排序区间选择最小的元素，将其
放到已排序区间的末尾。
设数组的长度为 𝑛 ，选择排序的算法流程如图 11‑2 所示。
1. 初始状态下，所有元素未排序，即未排序（索引）区间为 [0, 𝑛 − 1] 。
2. 选取区间 [0, 𝑛 − 1] 中的最小元素，将其与索引 0 处元素交换。完成后，数组前 1 个元素已排序。
3. 选取区间 [1, 𝑛 − 1] 中的最小元素，将其与索引 1 处元素交换。完成后，数组前 2 个元素已排序。
4. 以此类推。经过 𝑛 − 1 轮选择与交换后，数组前 𝑛 − 1 个元素已排序。
5. 仅剩的一个元素必定是最大元素，无须排序，因此数组排序完成
"""


def selection_sort(numbers: list[int]):
    n = len(numbers)
    for i in range(n - 1):
        # small_index用来记录没找的最小值的序号
        # 假设每次最小值的序号都是未排序部分的最左侧的那个的序号
        small_index = i
        # 外循环：未排序区间为 [i, n-1]
        for j in range(i, n - 1):
            # 内循环：找到未排序区间内的最小元素
            if numbers[small_index] > numbers[j + 1]:
                small_index = j + 1
            # print("index = ", small_index, "number = ", numbers[small_index])

        # 每次内循环结束，利用找到的序号，在外循环中，将该序号对应的最小元素交换到未排序部分的最左侧
        numbers[i], numbers[small_index] = numbers[small_index], numbers[i]
        print(numbers)


if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    selection_sort(nums)
    print("选择排序完成后 nums =", nums)
