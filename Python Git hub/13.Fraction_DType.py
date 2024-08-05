from CFD import Fraction
x=Fraction(2,3)
print("x=",x)
print(type(x))
x._Fraction__numerator=12
x._Fraction__denominator=13
print("x=",x)
y=Fraction(5,2)
print("y=",y)
print("x+y will be:",x+y)
print("x-y will be:",x-y)
print("x*y will be:",x*y)
print("x/y will be:",x/y)