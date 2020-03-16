a = '笑哈哈哈123456哦豁1'
b = [i for i in a if i.isdigit()]
print('type of b:',type(b))
c =''
for j in b:
    c+=j
print('c:',c)