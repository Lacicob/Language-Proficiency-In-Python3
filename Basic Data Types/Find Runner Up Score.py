if __name__ == '__main__' :
	n = int(input())
	arr = list(map(int,input().split()))
	
	arr.sort()

	i = n-2
	while arr[i] == arr[n-1] :
		i -= 1

	print(arr[i])