
list_inf = ['China', 'English', 'America']
for i in range(len(list_inf)):
    word = list_inf[i]
    for j in range(len(word)):
        print(word[j])

''' some basic functions'''
count = 5
while count > 0:
    print("I")
    count = count - 1
    if count == 2:
        break

count = 5
while count > 0:
    print('I love python')
    count = count - 1
print("over")


f = open("foo.txt")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()
