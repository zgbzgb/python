import copy

def zifuwangluo(grid):
	newList = copy.copy(grid)
	listLen = len(grid)
	cycLen = len(grid[0])
	for i in range(cycLen):				#控制行
		for j in range(listLen):		#控制列
			print(newList[j][i],end='')
		print('\n')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

zifuwangluo(grid)