#pythonsheets.com code snippet 

#1.Python Naming Rule-class
#good: MyClass
#bad: myClass myclass my_class

#2.Python Naming Rule-func, module, package, variables
#good: var_underscore_separate
#bad: varCamel VarCamel

#3.Python Naming Rule-summary
#for class
class MyClass:
    pass
#func, module, package, variables
var_underscore_separate = 100

#for public use
var = 'public'

#for internal use
_var = 'internal'

#convention to avoid conflict keyword
var_ = 'advoid conflict'

#for private use in class
__var = 'private'

#for protect use in class
_var_ = 'protect'

#"magic" method or attibutes
#ex: __init__, __file__, __main__, __var__

#for "internal" use throwaway variable
#usually used in loop
#ex: [_ for _ in range(10)]
#or variable not used
for _, a in[(1,2), (3,4)]:
    print(a)

#4.Check object attributes
print(dir(list))

#5. Define a function __doc__
def Example():
    """ This is an example function """
    print("Example function")

print(Example.__doc__)
#help(Example)

#6. Check instance type
ex = 10
print(isinstance(ex, int))

#7. Check, Get, Set attribute
class Example2(object):
    def __init__(self):
        self.name = 'ex'
    def printex(self):
        print("This is an example")
ex = Example2()
print(hasattr(ex, "name"))
print(hasattr(ex, "printex"))
print(hasattr(ex, "print"))

#getattr(obj, 'attr')
print(getattr(ex, 'name'))

#setattr(ex, 'name', 'example')
setattr(ex, 'name', 'example2')
print(ex.name)

#8. Check inheritance
class Example3(object):
    def __init__(self):
        self.name = 'ex'
    def printex(self):
        print("hiii")
print(issubclass(Example3, object))

#9. Check all global variables
print("globals: " + '\n'.join([str(_) for _ in globals().values()]))

#10. Check "Callable"
a=10
print(callable(a))
def myfun():
    print("hii")
print(callable(myfun))

#11. Get function/class name
class ExampleClass(object):
    pass
def example_function():
    pass

ex2 = ExampleClass()
print(ex2.__class__.__name__)
print(example_function.__name__)
