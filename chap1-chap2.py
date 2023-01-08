#une fonction qui supprime les doublons
def elimine1(L):
    P=[]
    for e in L:
        if e not in P:
            P.append(e)
    return P
#une seconde option

def elimine2(L):
    for e in L:
        if L.count(e)>1:
            for i in range(L.count(e)-1):
              L.remove(e)
    return L
#créer un vide tuple
x=()
print(x)
# un programme pour additionner les tuples
x=(1,2,4)
y=(4,2,3)
z=(1,6,4)
result=tuple(map(sum,zip(x,y,z)))
print(result)
# veifier un element dans un tuple
def check_in_tuples(colors,c):
    result=any(c in tu for tu in colors )
    return result
colors=(('red','white','blue'),('green','pink','purple'),('orange','yellow','lime'))
print(check_in_tuples(colors,'white'))
print(check_in_tuples(colors,'khazi'))
# resoudre un systeme

"""
f(x)=x^2 +5*x+3 if x>2
    = x+3 if x<=2
"""
x=int(input('enter the value of x :'))
if x >2 :
      f=x^2+5*x+3
else :
      f=x+3
print('value of function f(x)=%d'%f)
# 2 equation parallele
a1=int(input('enter the value of a1='))
a2=int(input('enter the value of a2='))
b1=int(input('enter the value of b1='))
b2=int(input('enter the value of b2='))
if (a1/a2) == (b1/b2):
    print('lines are parallel')
else:
    print('lines are not parallel')
a=5
b=7
c=9
if ((a>b) & (a>c)):
  print(a)
elif ((b>a) &(b>c)):
  print(b)
else:
  print(c)
       