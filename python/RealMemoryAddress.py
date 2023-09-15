import copy

hello = 'hello'

print(id('hello'))
print(id(hello))

hello += ' world'
print(hello + ':' + str(id(hello)))
print('hello world' + ':' + str(id('hello world')))

temp_1 = ('cat', 'bat', 'rat')
print(id(temp_1))
temp_1 = list(temp_1)
temp_2 = temp_1
temp_3 = copy.copy(temp_2)

print(id(temp_1))
print(id(temp_2))
print(id(temp_3))

print('\r')
temp_1.append('tag')

print(id(temp_1))
print(id(temp_2))


temp_1 = ['cat','bat','rat']

print('\r')
print(id(temp_1))
print(id(temp_2))


print('\r')

list = ['cat', 'bat', 'rat',[1,2,3,4]]
print(list)

copy_list = copy.copy(list)
print(copy_list)

#   深复制，可以复制原列表，并创建一个新列表。而不是使用原列表的引用
deep_copy_list = copy.deepcopy(list)

print(id(list[3]))
print(id(copy_list[3]))
print(id(deep_copy_list[3]))