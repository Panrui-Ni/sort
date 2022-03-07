def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp

inv=[1,2,3,4,5,6,7,8,9] # 逆序
for i in range (0,len(inv) // 2):
    inv[i],inv[len(inv)-1-i]=inv[len(inv)-1-i],inv[i]
#print(inv)

a=[6,5,4,4,3,2,1,2,3] # 插排
#print(a)
for i in range (1,len(a)):
    for j in range (i-1,-1,-1):
        if a[j]>a[j+1]:
            swap(a,j,j+1)
#print(a)

b=[5,4,4,3,2,1,2,3,6] # 选择
#print(b)
for i in range (0,len(b)-1):
    min=i
    for j in range (i+1,len(b)):
        if b[j]<b[min]:
            min=j
    b[i],b[min]=b[min],b[i]
#print(b)

c=[6,5,4,4,3,2,1,2,4] # 冒泡
#print(c)
for i in range (len(c),-1,-1):
    for j in range (0,i-1):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
#print(c)

d=[6,5,4,3,2,1,2,3,4] # 希尔
#print(d)
h=1
while h<=len(d)//3:
    h=h*3+1
step=h
while step>=1:
    for i in range (step,len(d)):
        for j in range (i-step,-1,-step):
            if d[j]>d[j+step]:
                d[j],d[j+step]=d[j+step],d[j]
    step=(step-1)//3
#print(d)

##归并

def sort1(arr, left, right): #左指针指在子序列左端，右指针指在中点
    if left==right: return #递归的初始条件，单个元素
    mid = left+(right-left)//2 # right-left 是为了防止大数溢出
    sort1(arr, left, mid) #递归，使得left-mid段排好序
    sort1(arr, mid+1, right)
    merge(arr, left, mid+1, right) #整合

def merge(arr, leftptr, rightptr, rightbd): # 两段子序列排好序后的归并函数，rightptr指向第二段子序列的第一个元素
    mid = rightptr - 1
    len = rightbd - leftptr + 1
    temp = [0]*len # 创建临时数据保存归并后的数组
    i = leftptr
    j = rightptr
    k=0
    while i<= mid and j<= rightbd:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k = k+1
            i = i+1
        else:
            temp[k] = arr[j]
            k = k+1
            j = j+1
    while i<=mid: # 归并后第一段多出来的都接着放在 temp 后面，因为第一段已经被排好序了，所以剩下的一定是大的
            temp[k]=arr[i]
            k = k + 1
            i = i + 1
    while j<= rightbd:
            temp[k] = arr[j]
            k = k + 1
            j = j + 1
    for i in range (0,len): arr [leftptr+i]=temp[i]

e=[6,5,4,3,2,1,2,3,3]
sort1(e,0,len(e)-1)
#print(e)

## 快排

def partition(arr, leftbd, rightbd):
    pivot = arr[rightbd]
    left = leftbd
    right = rightbd-1
    while left <= right:
        while left <= right and arr[left] <= pivot: left = left+1
        while left <= right and arr[right] > pivot: right = right-1
        if left < right: arr[left], arr[right] = arr[right], arr[left]

    arr[left], arr[rightbd] = arr[rightbd], arr[left]
    return left

def sort2(arr, leftbd, rightbd):
    if leftbd >= rightbd: return
    mid = partition(arr, leftbd, rightbd)
    sort2(arr, leftbd, mid-1)
    sort2(arr, mid+1, rightbd)

f=[7,3,2,6,8,1,9,5,4,10]
sort2(f,0,len(f)-1)
#print(f)

## 计数排序
g = [7,3,2,6,8,1,1,4,4,10]
result = [0]*len(g) # 存储结果数组
count = [0]*10 # 计数数组
for i in range(len(g)): # 先把 g 遍历一遍
    count[g[i]-1] += 1 # count[j] 对应 g[i] 的值j+1，出现一次j+1, count[j]+1
for i in range(1,len(count)): # 做 count 的累加，使得算法是稳定的
    count[i] += count[i-1]
for i in range(len(g)-1,-1,-1): # 逆序遍历一遍
    count[g[i] - 1] -= 1
    result[count[g[i]-1]] = g[i] # 累加后 count[g[i]-1]-1 指示的就是最后一个 g[i] 该放的位置
#print(result)

## 基数排序

h = [123, 321, 126, 130]
result = [0]*len(h)
count = [0]*7 # 各位上出现数字的范围是0-6，设置 7 位数组
for i in range(3):
    division = pow(10,i)
    for j in range(len(h)):
        num = h[j] // division % 10 #从个位开始取出各位上的数
        count[num] += 1 # 计数
    for k in range(1,len(count)): #对计数数组做累加
        count[k] += count[k-1]
    for l in range(len(h)-1,-1,-1):
        num = h[l] // division % 10 # 取出固定位数上 h[l] 的数字
        count[num] -= 1
        result[count[num]] = h[l]
    count=[0]*7
print(result)