d = {1:'one',2:'two',3:'three',4:'four'}
print(d)

d[5]= 'five'
print(d)

#-----------------------------
#del d[1]
#print(d)
#-----------------------------
#print(len(d))
#-----------------------------
print(d.get(5))
d.setdefault(6,'set de fault')
print(d)
d.pop(6)
print(d)
print(d.popitem())
print(d.popitem())
print(d.keys())
for key in d:
    print(key,d[key])
print(d.values())
print(d.items())
d.clear()
print(d)