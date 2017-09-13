import turtle
import math

def lt(t,s):
 t.lt(s)


def polygon(t,l,n):
 for i in range(n):
  t.fd(l)
  lt(t,360/n)

bob = turtle.Turtle()
print(bob)

def circle(t,r):
 c = 2*math.pi*r
 n = int(c/10)+1
 l = c/n
 polygon(t,l,n)

circle(bob,50)
turtle.mainloop()


