#pythonsheets.com code shippet 

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