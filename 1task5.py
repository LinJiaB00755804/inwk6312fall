def do_twice(f):
 f()
 f()
def print_spam():
 print('spam')
do_twice(print_spam)




def do_twice(f,s):
 f(s)
 f(s)
def print_spam(s):
 print(s)
do_twice(print_spam, 'spam')




def print_twice(s):
 print(s)
 print(s)
print_twice('spam')





do_twice(print_twice, 'spam') 





def do_four(f,s):
 f(s)
 f(s)
 f(s)
 f(s)
def print_spam(s):
 print(s)
do_four(print_spam,'spam')






