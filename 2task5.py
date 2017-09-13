import turtle

def lt(t,s):
 t.lt(s)


def polygon(t,l,n):
 for i in range(n):
  t.fd(l)
  lt(t,360/n)

bob = turtle.Turtle()
print(bob)
polygon(bob,100,6)
turtle.mainloop()


