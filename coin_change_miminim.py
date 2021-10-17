total_sum=20
coins=[5,6,2,1]
arr=[0]+([total_sum+1]*(total_sum))
for i in range(len(arr)):
    for j in coins:
        if i>=j and (arr[i-j]+1)<arr[i]:
            arr[i]=(arr[i-j]+1)
if arr[-1]==0 or arr[-1]==total_sum+1:
    print(-1)
else:
    print(arr[-1])
