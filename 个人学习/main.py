'''
a = 1\n
def fun(a):
    a = 2
fun(a)
print (a)
'''

"""
a = []
def fun(a):
    a.append(1)
fun(a)
print (a)
"""

"""
a  = [1,2,3]
print(a)
b = a[:]
print(b)
c = a[1:1]
print(c)

"""
"""
a = 1
b = 2
a,b = b,a
print (b)
"""

"""
array = [1, 2, 5, 3, 6, 8, 4]
print(array[2:])
print(array[2::])
"""

"""
t = (3.14, 'China', 'Jason', ['A', 'B'])
l = t[3]
l.append(1)
print(t)
"""

"""
d = {1:95,'a':1}
print(d[0])
"""
'''
a = ['a','b','c','d']
b = [1,2,3,4]
c = dict(zip(b,b))
print(c)
'''

'''
t = tuple(range(10))
print (t)
'''

'''
L = [75, 92, 59, 68]
print(sum(L) / 4)
'''

'''
sum = 0
x = 1
n = 1
while True:
    if n <= 20:
        sum+=x
        x=x*2
        n+=1
    else:
        break
print(sum)
'''

'''
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2 == 0:
        continue
    sum += x
print (sum)
'''

'''
for x in range(1,9):
    for y in range(10):
        if x<y:
            print(x*10+y)
'''

'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in ['Adam', 'Lisa', 'Bart']:
    print ("%s: %d"%(key, d[key]))
'''

'''
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72] = 'Paul'
print(d)
'''

'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print (key + ":",d[key])
'''

'''
months = set(('Feb','Sun'))
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print( 'x1: ok')
else:
    print( 'x1: error')

if x2 in months:
    print ('x2: ok')
else:
    print( 'x2: error')
'''

'''
s = set(['Adam', 'Lisa', 'Paul','a'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
m = set(L)
p = s -m
q = m -s
s = p | q
print (p)
print (q)
print (s)
'''

'''
L = range(1,100)

print (sum([i*i for i in L]))
'''

'''
def average(*args):
    if len(args) == 0:
        return 0.0
    else:
        return sum(args)/len(args)

print( average())
print( average(1, 2))
print( average(1, 2, 2, 3, 4))
'''

'''
for i in range(1,101):
    print(i)
'''

print ([x for x in range(1,101,7)])