# f = open("test.txt", 'r')
# print(f.read())
# f.close()
#
# try:
#     f = open('test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# with open("test.txt", "r") as f:
#     print(f.read())
#
# # write file
# with open("test.txt", "a") as f:
#     f.write("---hello,world")
#

f = open("test1.txt", "r")
result = list()
for line in open("test1.txt"):
    line = f.readline()
    print(line)
    result.append(line)
f.close()
print(result)
open("test.txt", "w").write('%s' % '\n'.join(result))

f = open("test1.txt", 'r')
result = list()
for line in f.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'):
        continue
    result.append(line)
result.sort()
print(result)
open('test.txt', 'w').write('%s' % '\n'.join(result))

dd = ["d", "f", "e", "u"]

print("%s" % "ggg".join(dd))
