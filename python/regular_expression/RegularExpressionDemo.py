import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal:
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal:
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal:
            return False

    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print('Done')

#   ？？？？找到一个后，不在进行向下找了 findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


def isPhoneNumberByRegex(message):
    ret = phoneNumRegex.search(message)
    print('Phone number found: ' + ret.group())


isPhoneNumberByRegex(message)

"""
python中空格的作用：
1.括号在表达式当做普通字符，用于匹配和捕捉文本的字符串
2.括号用来分组表达式，括号中的表达式进行捕捉，不在括号中的表达式不进行捕捉
"""
kong_ge_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = kong_ge_regex.search('My number is 415-555-4242.')

print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
# print(mo.group(3))

print(mo.groups())


print('\r {num} 执行匹配次数')
kong_ge_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = kong_ge_regex.search('My number is 415-555-4242.')

print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
# print(mo.group(3))

print(mo.groups())

#   管道匹配多个分组    多个只取一个
heroRegex = re.compile(r'Batman|Tiny Fey')
mo1 = heroRegex.search('Batman and Tiny Fey')
print(mo1.group())

mo2 = heroRegex.search("Tiny Fey and Batman ")
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = batRegex.search('Batmobile lost a sell')
print(mo1.group())
print(mo1.group(1))
print(mo1.groups())

#   问号实现可选匹配,(wo)?部分表示wo是可选分组
print('\r ? ')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman!')
print(mo1.group())

mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

#   星号（*）匹配0次或多次
print('\r * ')
batRegex = re.compile(r'Bat(wo)*?man')
mo1 = batRegex.search('The Adventures of Batman!')
print(mo1.group())

mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo1 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo1.group())

#   加号（+）匹配1次或多次
print('\r + ')
batRegex = re.compile(r'Bat(wo)+?man')
# mo1 = batRegex.search('The Adventures of Batman!')
# print(mo1.group())

mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo1 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo1.group())

print('\r {}指定次数')
batRegex = re.compile(r'Bat(wo){2,}?man')
mo1 = batRegex.search('The Adventures of Batman!')
print(mo1 is None)

mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1 is None)
mo1 = batRegex.search('The Adventures of Batwowowowowowowowowoman')
print(mo1.group())

"""
贪心：现在有二义的情况下，尽可能选择最长的
非贪心：花括号后面写一个？，尽可能选择最短的
"""
print('\r 贪心和非贪心')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHa')
print(mo1.group())


print('\r findall():')
text = 'Cell: 415-555-9999 Work: 212-555-0000'
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search(text)
print(mo.group())

print(phoneNumRegex.findall(text))


phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

print(phoneNumRegex.findall(text))

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

print(phoneNumRegex.findall(text))

"""
\d:数字[0~9]
\D:除数字之外的字符
\w:数字、字母、下划线
\W:除数字、字母、下划线之外的字符
\s:空格、制表符、换行符
\S:除空格、制表符、换行符之外的字符
"""
print('\r \\d \\w \\s \\D \\W \\S')
text = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 ' \
       'swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(text))



#   方括号自定义字符分类
"""
a:[ei]
e:[i:]
i:[ai]
o:[eu]
u:[ju:]

方括号内普通的正则表达式符号是不会被解释的
"""
print('\r []')

text = 'RoboCop eats baby food. BABY FOOD.'
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(text))

text = 'ABC!#@$213fdkj320i.'
worldRegex = re.compile(r'[A-Za-z0-9.]')
print(worldRegex.findall(text))

print("中括号内的 插入字符[^] 代表非")
worldRegex = re.compile(r'[^a-zA-Z0-9]')
print(worldRegex.findall(text))

print('\r ^和$')
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.findall('Hello world'))
print(beginsWithHello.search('Hello world'))

print(beginsWithHello.search('He name is bibi') is None)

endsWithHello = re.compile(r'\d$')
print(endsWithHello.search('hello world') is None)
print(endsWithHello.search('hello world 121') is None)
print(endsWithHello.search('hello world 121'))

#   .匹配换行符之外的所有字符
print('\r 通配字符[.]')

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat. at'))

#   用点星（.*）匹配所有字符

print('\r [.*]')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

text = '<To serve man> for dinner.>'
nongreedyRegex = re.compile(r'<.*?>')
print(nongreedyRegex.search(text))

greedyRegex = re.compile(r'<.*>')
print(greedyRegex.search(text))


#   用句号字符匹配换行符
print('\r re.DOTALL 用句号匹配换行符')
text = 'Serve the public trust.\nProtect the innocent.'\
'\nUphold the law.'

noNewlineRegex = re.compile(r'.*')

print(noNewlineRegex.search(text).group())

noNewlineRegex = re.compile(r'.*',re.DOTALL)
print(noNewlineRegex.search(text).group())

#   不区分大小写的匹配
print('\r re.I')
robocop = re.compile(r'robocop',re.I)

print(robocop.search('RoboCop is part man, part machine, all cop.'))
print(robocop.search('ROBOCOP is part man, part machine, all cop.'))


#   sub()方法替代字符串
print('\r sub() 文本替代')

name = 'Agent Alice gave the secret documents to Agent Bob.'
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('Alim',name))

print('\r 使用\1和\2来替代匹配分组，\1和\2当做')
agentNameRegex = re.compile(r'Agent (\w)(\w)\w*')
print(agentNameRegex.sub(r'\1**\2--','Agent Alice told Agent Carol that Agent '\
'Eve knew Agent Bob was a double agent.'))

#   管理复杂的表达式
print('\r 管理复杂的表达式 re.VERBOSE')
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}' \
    '(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)

text = '123 3456 ext. 678'
text1 = '123-345-3456  ext   5789'
text2 = '123.345-5678   x  49509'
text3 = '123-345.5678    x   234'

print(phoneRegex.search(text))
print(phoneRegex.findall(text))
print(phoneRegex.findall(text1))
print(phoneRegex.findall(text2))
print(phoneRegex.findall(text3))

print('\r 组合只用使用re.IGNORECASE、re.DOTALL、re.VERBOSE')
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
