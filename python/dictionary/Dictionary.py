import pprint


myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['color'])

newMyCat = {'size': 'fat', 'disposition': 'loud', 'color': 'gray'}

print(myCat == newMyCat)

print(id(myCat))
print(id(newMyCat))

newMyCat['disposition'] = 'whispered'

print(newMyCat)
print(id(myCat))
print(id(newMyCat))

print(myCat.keys())
print(myCat.values())
print(myCat.items())
print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))



for key in myCat.keys():
    print(key + ':' + myCat[key])

for key,value in myCat.items():
    print(key + ':' + value)

for value in myCat.values():
    print(value,end=' ')


print()
print(myCat['size'])
print(myCat.get('hello','not find'))


myCat.setdefault('hello','world')
print(myCat)
myCat.setdefault('size','18')
print(myCat)


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
pprint.pprint(count)


list = [
    ['size', 'color', 'disposition']
]

print('size' in myCat)
print('size' in myCat.keys())

print('fat' in myCat)
print('fat' in myCat.values())