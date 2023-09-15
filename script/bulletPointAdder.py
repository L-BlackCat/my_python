import pyperclip

text = pyperclip.paste()


# TODO: Separate lines and add stars.
lines = text.split('\n')

ret = []
for msg in lines:
    ret.append('* ' + msg)



pyperclip.copy('\n'.join(ret))

print(pyperclip.paste())