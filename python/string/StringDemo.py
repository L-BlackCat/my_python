spam = 'This is China'
print(spam)

#   如何在字符串中使用单引号

spam = "This's China"
print(spam)

spam = 'This\'s China'
print(spam)


spam = 'This\'s China\tWelcome to China'
print(spam)

spam = 'This\'s China\nWelcome to China'
print(spam)


spam = '''This's China\tWelcome to China'''
print(spam)

"""
This's China\tWelcome to China
"""

#   字符串的索引和切片
spam = 'Hello World!'
print(spam[1])
print(spam[0:4])
print(spam[:5])
print(spam[:])
print(spam[2:])
print(spam[-1])
print(spam[-5:-1])


#   int和not in的使用
print('e' in spam)
print('Hell' in spam)
print('hell' not in spam)


#   字符串中输入其他数据
name = 'li'
age = 23

print("My name is %s and my age is %s" % (name, age))

print(f'My name is {name} and my age is {age}')

#   字符串的相关方法，转大小写,检测是否大小写

spam = 'Hello world'

print(spam.upper())
print(spam.lower())

print(spam.isupper())
print(spam.islower())

print(spam.upper().isupper())

#   字符串相关方法，只包含字母且非空
print('isalpha()')
print('helloworld'.isalpha())
print('hello world123'.isalpha())
print('hello world'.isalpha())

print('')
print('isalnum()')
print('helloworld'.isalnum())
print('hello world123'.isalnum())
print('helloworld123'.isalnum())


print('')
print('isdecimal()')
print('helloworld'.isdecimal())
print('hello world123'.isdecimal())
print('helloworld123'.isdecimal())
print('1234 '.isdecimal())
print('1234'.isdecimal())


print('')
print('isspace()')
print('helloworld'.isspace())
print('hello world123'.isspace())
print('helloworld123'.isspace())
print(' \t\n'.isspace())


print('')
print('isspace()')
print('Helloworld'.istitle())
print('hello world123'.isspace())
print('helloworld123'.isspace())


#   startWith and endWith   检测字符首部和尾部是否以设置字符串开头
print()
print('startWith and endWith')
print(spam.startswith("hello"))
print(spam.startswith("Hello"))

print(spam.endswith("world"))
print(spam.endswith("d"))
print(spam.endswith("wor"))


# join  使用设置字符串作为列表元素之间的连接字符
print()
print('join()')
list = ['cat','dog','tiger','mouse']
print(','.join(list))
print(' '.join(list))


# split 根据设置字符串进行分离字符串，设置字符串删除
print()
print('split()')
word = 'This is a good day!'
print(word.split(' '))

print(word.split('a'))


# partition() 根据设置字符串进行分离字符串，将字符串分成3个部分
print()
print('partition()')
print(word.partition('s'))
print(word.partition('H'))

print("split()")
before,sep,after = word.split('s')
print(before)
print(sep)
print(after)

print("partition()")
before,sep,after = word.partition('s')
print(before)
print(sep)
print(after)

#   ljust()、rjust()、center(),左边、右边、左右两边填充字符，未设置，默认填充' '
print('ljust()、rjust() and center()')
print(spam.ljust(30))
print(spam.ljust(30,'='))
print(spam.rjust(30))
print(spam.rjust(30,'*'))

print(spam.center(30))
print(spam.center(30,'-'))


pens = {'red_pen':4,'blue_pen':5,'yellow_pen':10}

def printPens(pens,leftWidth,rightWidth):
    print('PENS ITEMS'.center(12 + 6,'-'))
    for key,value in pens.items():
        print(key.ljust(leftWidth,'.') + str(value).rjust(rightWidth))

printPens(pens,12,6)
printPens(pens,10,5)


#   删除左、右、左右两边的字符串，默认字符串为' '
print('strip()、lstrip() and rstrip()')
spam = '          Hello world!      '

print(spam.strip())

print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSmapBaconEggsBuyamSppSamp'

print(spam.strip('ampS'))


#   ord()将单个字符转换成unicode，chr()将数字转换成单字符字符串
print('ord() and chr()')
print(ord('!'))
print(ord('A'))
print(ord('B'))
print(ord('4'))
print(chr(111))
print(ord('A') < ord('B'))
print(chr(ord('A') + 1))



print('hello\tworld\t!')
print('hello   world   !')


print('Remember, remember, the fifth of November.'.split())
print('-'.join('There can be only one.'.split()))