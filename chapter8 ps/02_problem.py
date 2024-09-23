'''
def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter temperature in F : "))

c = f_to_c(f)

'''

def c_to_f(c):
    return ((c*9)/5)+32

f = float(input("Enter temperature in C : "))

f = c_to_f(f)

print(f"{round(f,2)}")