
import turtle

def square(t,l):
 for i in range(4):
  t.fd(l)
  t.lt(90)

bob = turtle.Turtle()
print(bob)
square(bob,1000)
turtle.mainloop()


