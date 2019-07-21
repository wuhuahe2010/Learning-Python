#-*- coding:utf8 -*-

age = 30
print('my age is %d' % age)

name = "makes"
print("my namge is %s." % name)

print('%6.3f' % 2.3)
print('%f' % 2.3)

print("============= format type =================")
print("{}:{}".format('192.168.0.100', 8888))

print('{server}{1}:{0}'.format(8888,'192.168.0.100',server='Web Server Info: '))

print("{0[0]}.{0[1]}".format(('baidu','com')))

print('{0[0]}.{1[0]}.{1[1]}'.format(('www','sss'),('baidu','com')))

# {2:0>2} 右对齐，两位，前用0填充
print('{0}*{1}={2:0>2}'.format(3,2,2*3))

# ^ 居中对齐
print("{:*^30}".format('centered'))

for i in range(1,10):
    a = 1
    while a <= i:
        print('{0}*{1}={2:>2}'.format(a,i, a*i),end='\t')
        a += 1
    print()

print("{:.3f}".format(2.1415))
print("{:.10f}".format(3.1415))












