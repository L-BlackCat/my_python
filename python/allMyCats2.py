
# cats = []
#
# while True:
#     print('Enter the name of cat ' + str(len(cats) + 1) + ' (Or enter nothing to stop.):')
#     cat = input()
#
#     if cat == '':sdfa
#         break
#
#     cats = cats + [cat]
#
# print('The cat names are:')
# for name in cats:
#     print(name ,end=' ')



colors = ['red','blue','green','yellow']
print('enter you like color:')
color = input()
if color not in colors:
    print('my shop not have ' + color)
else:
    print('here you are,color is' + color)