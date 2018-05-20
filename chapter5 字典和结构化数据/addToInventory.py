#遍历字典中的所有键
def displavInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))

#返回一个字典，表示更新过的物品清单
def addToInventory(inventory, addedItems):
	for add in addedItems:
		inventory.setdefault(add, 0)
		inventory[add]+=1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displavInventory(inv)