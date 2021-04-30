from tkinter import Tk

x = [7,8]

print(x)

x.append(5)


print(x)

class Try:
    def show(self, name = "unknown"):
        print('hello, '+ name)


x = Try()
y = Try()
x.show()
y.show("Den")