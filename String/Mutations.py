def mutate_string(str,pos,char) :
	L = list(str)
	L[pos] = char
	str = ''.join(L)
	
	return str
	
if __name__ == '__main__' :
	s = input()
	j,c = input().split()
	s_new = mutate_string(s,int(j),c)
	print(s_new)
