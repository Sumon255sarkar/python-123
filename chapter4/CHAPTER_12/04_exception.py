# Code which might might throw exception 

try:
    a =int (input("hey, Enter a number :"))
    print(a)

except ValueError  as V :
    print("Hey")
    print(V)

except Exception as e:
    print(e)
    print("Thank you ")

#We can raise custom exception  using the raise keywoed in Python .


