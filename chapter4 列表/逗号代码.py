import copy

def douhao(List):
	listLen = len(List)
	newList = copy.copy(List)
	newList[-1] = 'and ' + newList[-1]
	for i in range(listLen):
		print(newList[i] + ',' , end='')
		#end='' 关闭在输出中自动包含换行的行为

spam = ['apple','banans','tofu','cats']
douhao(spam)
