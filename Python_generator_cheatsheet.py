#Glossary of Generator
def gen_func():
    yield 5566

try:
    g = gen_func()
    print(type(g))
    print(next(g))
    print(next(g))
except Exception as ex:
    print(ex)

try:
    h = (_ for _ in range(2))
    print(next(h))
except Exception as ex:
    print(ex)

#Produce value via generator
print("----------------------------")
def prime(n):
    p = 2
    while n > 0:
        for _ in range(2,p):
            if p % _ == 0:
                break
        else:
            yield p
            n-=1
        p+=1

p = prime(10)
print(next(p))
print(next(p))
print(next(p))

#Implement Iterable object via generator
class count(object):
    def __init__(self,n):
        self._n = n
    def __iter__(self):
        n = self._n
        while n > 0:
            yield n
            n-=1
    def __reversed__(self):
        n = 0
        while n < self._n:
            yield n
            n+=1
for _ in count(5):
    print(_, end=" ")
print('')
for _ in reversed(count(5)):
    print(_, end=" ")
print('')

#Send message to generator
def spam():
    msg = yield
    print("Message:",msg)

try:
    g = spam()
    #start generator
    next(g)
    #send message to generator
    g.send("Hello World!")
except StopIteration:
    pass

#"yield from" expression
def subgen():
    try:
        yield 9527
    except ValueError:
        print("get value error")

def delegating_gen():
    yield from subgen()

g = delegating_gen()

try:
    next(g)
    g.throw(ValueError)
except StopIteration:
    print("gen stop")


#Check Generator State
import inspect
def subgen2():
    yield from range(5)
def delegating_gen2():
    yield from subgen2()
g = delegating_gen2()
print(inspect.getgeneratorstate(g))
next(g)
print(inspect.getgeneratorstate(g))
g.close()
print(inspect.getgeneratorstate(g))

#Check Generator type
from types import GeneratorType
def gen_func():
    yield 5566
g = gen_func()
print(isinstance(g, GeneratorType))
print(isinstance(123, GeneratorType))

#yield(from) EXPR return RES
def average():
    total = .0
    count = 0
    avg = None
    while True:
        var = yield
        if not var:
            break
        total += var
        count += 1
        avg = total / count
    return  avg
g = average()
next(g) #start gen
g.send(3)
g.send(5)
try:
    g.send(None)
except StopIteration as e:
    ret = e.value
print(ret)

def subgen3():
    yield 9257
def delegating_gen3():
    yield from subgen3()
    return 5566
try:
    g = delegating_gen3()
    print(next(g))
    print(next(g))
except StopIteration as _e:
    print(_e.value)
    

#Generator sequences
def chain():
    for _ in 'ab':
        yield _
    for _ in range(3):
        yield _
a = list(chain())
print(a)

#What "RES = yield from EXP" actually do?
def subgen4():
    for _ in range(3):
        yield _
EXP = subgen4()
def delegating_gen4():
    RES = yield from EXP
g = delegating_gen4()
print(next(g))
print(next(g))

#Simple compiler