def count_substring(str,substr) :
	count = 0
	for i in range(0,len(str) - len(substr) + 1) :
		if str[i] == substr[0] :
			flag = 1
			for j in range(0,len(substr)) :
				if str[i+j] != substr[j] :
					flag = 0
					break
			if flag == 1 :
				count += 1
	
	return count
			
if __name__ == '__main__' :
	string = input().strip()
	sub_string = input().strip()
	count = count_substring(string,sub_string)
	print(count)