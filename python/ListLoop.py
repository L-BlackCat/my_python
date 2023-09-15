supplies = ['pens', 'staplers', 'flamethrowers', 'binders', 'binders']

#   第一种方式
for i in range(len(supplies)):
    print('index : ' + str(i) + " value is " + supplies[i])

print("\r\n")
#   第二种方式
for value in supplies:
    #   列表中存在重复的值，返回第一次出现的值
    print('index : ' + str(supplies.index(value)) + ' value is :' + value)

print('\r\n')
for index, item in enumerate(supplies):
    print('index : ' + str(index) + " value is " + item)

print('\n')

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print(spam.index('cat'))

#   列表不存在这个值，报出ValueError
# print(spam.index('hello'))


spam.append('elephant')

print(spam)

spam.insert(1, 'hello')

print(spam)

spam.remove('hello')

spam.remove('bat')

print(spam)

print("\nsort used:")
#   sort的使用
spam.append("Hat")
spam.sort()

#   默认sort排序是根据ascii码进行排序，先排大写字母，再排小写字母，不知道原理？查一下ascii码表
print('sort:' + str(spam))

#   修改为字典排序
spam.sort(key=str.lower)

print('lower sort:' + str(spam))

#   方向排序
spam.sort(reverse=True)
print('reverse sort:' + str(spam))

# 字符串和数字不能进行排序
# spam.append(1)
# spam.sort()

#   翻转列表
spam.reverse()
print('reverse list:' + str(spam))

#   不可变列表，字符串，元组数据
name = 'This is a good day'

print('name[0,5]:' + name[0:5])

print('name[5]:' + name[5])

try:
    name[1] = 'i'
except TypeError:
    print('update name index 1 err')

temp_1 = ('cat', 'bat', 'rat', 'cat', 'hat', 'cat')

temp_2 = list(temp_1)

temp_2.append('hello')

temp_3 = tuple(temp_2)

print(temp_1)

print(temp_2)


print(type(('hello',)))
print(type(('hello')))
print(type(['hello']))
