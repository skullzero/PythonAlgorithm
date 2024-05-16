"""
「冒泡排序 bubble sort」通过连续地比较与交换相邻元素实现排序。这个过程就像气泡从底部升到顶部一样，
因此得名冒泡排序。
冒泡过程可以利用元素交换操作来模拟：从数组最左端开始向右遍历，依次比较相邻元素大
小，如果“左元素 > 右元素”就交换它俩。遍历完成后，最大的元素会被移动到数组的最右端。
"""


def bubble_sort(numbers: list[int]):
    n = len(numbers)
    # i的范围从数列的最大序号开始，直到0，逐次减1
    for i in range(n-1, 0, -1):
        for j in range(i):
            # j的取值范围每次都是从0到i，逐次加1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2, 7, 11, 6, 20, 99, 43, 200, 8]
    bubble_sort(nums)
    print("冒泡排序完成后 nums =", nums)
