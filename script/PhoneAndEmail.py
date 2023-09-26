#! python3
# phoneAndEmail.py - 在剪贴板上查找电话号码和电子邮件地址

import pyperclip,re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)


emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[A-Za-z0-9.-]+
(\.[A-Za-z]{2,4})
)''',re.VERBOSE)

message = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(message):
    print(groups)
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

print(matches)

print(emailRegex.findall(message))
print(phoneRegex.findall(message))

print(emailRegex.search('events@abc-tech.com。'))
