if __name__ == '__main__' :
	N = int(input())
	
	List = [ ]
	for j in range(N) :
		str = input().split()
		
		if str[0] == 'insert' :
			List.insert(int(str[1]),int(str[2]))
	
		if str[0] == 'print' :
			print(List)
			
		if str[0] == 'remove' :
			List.remove(int(str[1]))
		
		if str[0] == 'append' :
			List.append(int(str[1]))
			
		if str[0] == 'sort' :
			List.sort()
			
		if str[0] == 'pop' :
			List.pop()
		
		if str[0] == 'reverse' :
			List.reverse()
		