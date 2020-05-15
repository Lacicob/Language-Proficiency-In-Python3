import textwrap

def wrap(str,Width) :
	return textwrap.fill(str,Width)
	
if __name__ == '__main__' :
	str ,Width = input() , int(input())
	result = wrap(str,Width)
	print(result)
