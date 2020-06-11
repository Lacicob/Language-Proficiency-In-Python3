n = int(input())

if n&1 == 1 or (n&1 == 0 and n in range(6,21)) :
	print("Weird")

elif n in range(2,6) or n > 20 :
	print("Not Weird")
