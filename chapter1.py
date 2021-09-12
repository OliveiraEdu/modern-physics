#Chapter 1

#constants
qe = 1.6E-19 #charge of the electron
qp = qe #charge of the proton
me = 9.1E-31 #mass of the electron
mp = 1.7E-27 #mass of the proton
em_e = 1.76E11 #charge mass ratio for the electron
em_p = 1.76E11 #charge mass ratio for the electron
c = 3E8 #speed of light
b_earth = 10E-4 #Earth's magnetc field

#Ex1
ddp = 1E2
s = 10E-3

ec = qe*ddp #Eq 1.5

print("---- Ex1")
print(ec)

#Ex2
v = ((2*qe*ddp)/me)**0.5 #Eq 1.5, solving for v
vr = v/c #v relative to the speed of light

print("---- Ex2")
print(vr)

#Ex3
print("---- Ex3")
print ('A energia cinética será,apenas uma função do valor da diferença de potencial entre os dois pontos, independentemente dos detalhes do campo e da trajetória percorrida')

#Ex4
ddp = (((c*0.1)**2)*me)/(2*qe) #Eq 1.5, solving for ddp

print("---- Ex4")
print(ddp)

#Ex5
v = ((2*qp*ddp)/mp)**0.5 #Eq 1.5, solving for v
vr = v/c #v relative to the speed of light

print("---- Ex5")
print(v)
print(vr)


#Ex6
ddp = 100
r = (2*ddp/(qe/me)/b_earth**2)**0.5 #Eq 1.9, solving for r
print("---- Ex6")
print(r)

#Ex7
ddp = 100
r = (2*ddp/(qp/mp)/b_earth**2)**0.5 #Eq 1.9, solving for r
print("---- Ex7")
print(r)
