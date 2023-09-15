import random



for i in range(5):
    randInt = random.randint(0,5)
    print(randInt)
    # randRange = random.randrange(1,5)
    # print(randRange)
    # print("\r\n")

print('\n')

pets = ['Dog',  'Cat',  'Moose']

#   两者类似，堆积查找列表中的值
for i in range(5):
    print(random.choice(pets))
    print(pets[random.randint(0,len(pets) - 1)])

#   列表重新排序
random.shuffle(pets)
print(pets)
