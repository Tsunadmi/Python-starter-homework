STRING = "Hello World!"
result =''
i = 0
while i < len(STRING):
    if STRING[i] == 'o':
        result += "a"
    elif STRING[i] =='l':
        result += "e"
    else:
        result +=STRING[i]
    i += 1
print (result)