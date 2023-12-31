def displayInventory(items):
    totalNum = 0
    print('Inventory:')
    for key,value in items.items():
        print('%s %s' % (value, key))
        totalNum += value

    print('Total number of items: %s' % totalNum)


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] = inventory[item] + 1
    return inventory



items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(items)
print('\n')

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)