def solve(str) :
	return ' '.join(j.capitalize() for j in str.split(" "))
	
if __name__ == '__main__' :
	str  = input() 
	result = solve(str)
	print(result)
