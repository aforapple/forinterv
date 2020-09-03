def partion(nums, lo, hi):
    i = lo + 1
    j = hi
    v = nums[lo]
    while (True):
        while i < hi and nums[i] < v :   #左侧都应该 小于
            i = i + 1
        while j > lo and nums[j] >= v :  #右侧都应该 大于
            j = j - 1
        if i >=j :
            break

        nums[i], nums[j] = nums[j], nums[i]
    
    nums[lo], nums[j] = nums[j], v
    return j

def sort(nums, lo, hi):
    if hi <= lo:
        return
    j = partion(nums, lo, hi)
    sort(nums, lo, j-1)
    sort(nums, j+1, hi)

def quicksort(nums):
    print("in quicksort")
    sort(nums, 0, len(nums) - 1)
    print(nums)

def bubblesort(nums):
    print("in bubblesort")
    bswap = False
    for i in range(len(nums)):
        for j in range(0, len(nums) - i -1):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                bswap = True
        if bswap:
            bswap = False
        else:
            break

    print(nums)

def selectsort(nums):
    print("in selectsort")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[j] < nums[i]):
                nums[j], nums[i] = nums[i], nums[j]
    print(nums)

def insertsort(nums):
    print("in insertsort")
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    print(nums)

def shellsort(nums):
    print("in shellsort")
    h = 1
    while (h <= int(len(nums)/3)):
        h = h*3 + 1
    while (h >= 1):
        for i in range(h, len(nums)):
            for j in range(i, 0, -h):
                if nums[j] < nums[j-h]:
                    nums[j], nums[j-h] = nums[j-h], nums[j]
        h = int(h/3)
    print(nums)


def swim():
    pass

#下标从0开始的，需要转换
def sink(nums, k, N):
    l = 2*k + 1
    r = 2*k + 2
    large = k
    if l < N and nums[k] < nums[l]:
        large = l
    if r < N and nums[large] < nums[r]:
        large = r
    if large != k:
        nums[large], nums[k] = nums[k], nums[large]
        k = large
        sink(nums, k, N)    

def heapsort(nums):
    print("in heapsort")
    N = len(nums)

    #注意这里是-1，range是左闭右开区间
    #eg [i for i in range(0,5)], result is [0, 1, 2, 3, 4]
    for i in range(int(N/2), -1, -1):
        sink(nums, i, N)
    
    while N > 0:
        nums[0], nums[N-1] = nums[N-1], nums[0]
        sink(nums, 0, N-1)
        N = N-1
    print(nums)

def binsearch(nums, v):
    lo = 0
    hi = len(nums) - 1
    if (hi < lo):
        return -1    
    
    while (lo < hi):        
        mid = int(lo + (hi - lo)/2)
        if v < nums[mid]:
            hi = mid - 1
        elif v > nums[mid]:
            lo = mid + 1
        else:
            return mid

def binsearch2(nums, v):    
    return search(nums, v, 0, len(nums) - 1)

def search(nums, v, lo, hi):
    if lo > hi:
        return -1
    mid = int((lo + hi)/2)
    if v > nums[mid]:
        return search(nums, v, mid + 1, hi)
    elif v < nums[mid]:
        return search(nums, v, lo, mid-1)
    else:
        return mid


if __name__ == "__main__":
    nums = [2, 4, 3, 6, 9, 7, 8,  5]
    #bubblesort(nums)
    #selectsort(nums)
    #insertsort(nums)
    #shellsort(nums)
    #quicksort(nums)
    heapsort(nums)

    idx = binsearch(nums, 7)
    print(idx)
