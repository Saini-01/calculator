def add():  
   x = input()
   y = input()
   print(int(x) + int(y))

def sub():
    s = input()
    u = input()
    print(int(s) - int(u))

def multiply():
    m = input()
    u = input()
    print(int(m)*int(u))

def divide():
    d = input()
    i = input()
    print(int(d) / int(i))

print("choose operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ui = input()
if ui == "1":
    add()
if ui == "2":
    sub()
if ui == "3":
    multiply()
if ui == "4":
    divide()




