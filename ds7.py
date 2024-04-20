import time
start=time.time()
def bubblesort(a):
    n=len(a)
    for i in range(n-2):
      for j in range(n-2-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
alist=[34,46,27,57,41,45,21,70]
print("before sorting:",alist)
bubblesort(alist)
print("after sorting:",alist)
end=time.time()
print(f"runtime of the program is{end-start}")
