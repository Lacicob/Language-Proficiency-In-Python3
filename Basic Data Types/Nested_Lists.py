l = []
second_lowest_names = []
scores = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
    scores.append(score)
        
scores.sort()

j = 1

while scores[j] == scores[0] :
 	j += 1
 	
second_lowest = scores[j]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

second_lowest_names.sort()

for name in second_lowest_names:
    print(name, end='\n')
