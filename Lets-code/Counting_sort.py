def counting_sort(a):
    n = len(a)
    output = [0 for i in range(0,n)]
    count = [0 for i in range(0,1000000)]
    max_n = max(a)
    for i in a:
        count[i]+=1

    for i in range(1,max_n+1):
        count[i]+=count[i-1]

    for i in range(n):
        output[count[a[i]]-1] = i
        count[a[i]]-=1

    return output

print counting_sort([1,4,1,2,7,5,2])