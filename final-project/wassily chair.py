#tubo curvo
domain=Plasm.power(INTERVALS(1)(14),INTERVALS(1)(14))

c1 = CUBICHERMITE(S1)([[1,0,0],[0,1,0],[0,2,0],[-3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0.75,0,0],[0,0.75,0],[0,1.75,0],[-2.5,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,0,0.5],[0,0,-0.5]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0,-0.5],[0,0,0.5]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo=STRUCT([out,out2])
#VIEW(tubo)





#cilindro dritto
cyl=CYLINDER([0.125,5.5])(16)  #############5.5--------------------->3.5
cyl=R([2,3])(PI/2)(cyl)
cyl=T([1])([0.875])(cyl)
#VIEW(cyl);

#tubo curvo2
tub2=R([1,2])(3*PI/2)(tubo)
tub2=T([2])([-5.5])(tub2)
#VIEW(tub2)
tuboRicurvo=STRUCT([tubo,cyl,tub2])

tuboRicurvo=T([1])([1.75])(tuboRicurvo)###########/
#VIEW(tuboRicurvo);

tuboide=STRUCT([tubo,cyl])
tuboide=T([1])([2.5])(tuboide)
tub2=R([1,2])(3*PI/2)(tubo)
#tub2=T([1,2])([2.5,-3.5])(tub2)
tub2=R([1,3])(-3*PI/2)(tub2)
tub2=T([1,2,3])([3.375,-5.5,-0.875])(tub2)######----------------->-5.5--------------------->-3.5


tub2cur=STRUCT([tuboide,tub2])
tub2cur=R([2,3])(3*PI/2)(tub2cur)

tub2cur=T([1,2,3])([0.75,0.75,0.75])(tub2cur)    #traslo di più


#VIEW(tub2cur)



cyl=CYLINDER([0.125,3.25])(16)   #tubo più lungo
cyl=R([1,3])(PI/2)(cyl)
cyl=T([2,3])([0.75,-0.125])(cyl)
#VIEW(cyl)

#/ribalto
rib=STRUCT([tub2cur,cyl])

rib=S([1])([-1])(rib)
#VIEW(rib);

mezz=STRUCT([cyl,rib])

#mezz=T([2])([1.75])(mezz)########################/


#VIEW(mezz)


#rib
rib2=STRUCT([mezz,tub2cur])
rib2=T([2])([1.75])(rib2)

#VIEW(rib2)





#tubo curvo alto vicino bracciolo

cyl=tubo
cyl=R([1,3])(-3*PI/2)(cyl)
cyl=R([1,2])(2*PI/2)(cyl)
cyl=T([1,2,3])([-4.125,1.75,6.25])(cyl)############/7---->5

cyl2=T([1])([8.25])(cyl)

cyls=STRUCT([cyl,cyl2])
#VIEW(cyls);  #commento tubo dritto in alto prima del bracciolo


#mezz=STRUCT([cyls,rib2])  ###########
#mezz=S([2])([-1])(mezz)
#VIEW(mezz);





#cilindro più corto dietro
cyl4=CYLINDER([0.125,0.3])(16)
cyl4=T([1,2,3])([-4.125,0.875,6.2])(cyl4)############/7---->5


#cilindro più lungo anteriore
cyl5=CYLINDER([0.125,0.8])(16)
cyl5=T([1,2,3])([4.125,0.875,5.5])(cyl5)############/7---->5







v2=T([3])([-1.5])(cyl)
v2=R([1,2])(2*PI/2)(v2)
v2=R([1,3])(PI)(v2)


v3=T([1])([8.25])(v2)
#cyl=R([1,2])([2*PI/2])()


v3=T([2,3])([2,10.25])(v3)
v2=T([2,3])([2,11])(v2)


vs=STRUCT([v2,v3])
vs=T([2])([-0.25])(vs)


model1=STRUCT([rib2,cyls,cyl5,cyl4,vs])


tube=CYLINDER([0.125,2.15])(16)   #1.4



tubo2=R([2,3])(PI/2)(tube)
tubo2=T([1,2,3])([-4.125,0,5.375])(tubo2)


tubo3=R([2,3])(PI/2)(tube)

tubo3=T([1,2,3])([4.125,0,4.625])(tubo3)




model=STRUCT([model1,tubo2,tubo3])
model=T([2])([2.15])(model)  #1.4

mirrorModel=S([2])([-1])(model)


xtub=CYLINDER([0.125,8.5])(16)   
xtub=R([1,3])(-PI/2)(xtub)
xtub=T([1,2,3])([-4.25,4.415,6.2])(xtub) 

xtub2=T([2])([-8.825])(xtub) 


modelF=STRUCT([model,xtub2,xtub,mirrorModel])

#VIEW(modelF)

##############################################
tubSchienale=CYLINDER([0.125,6])(16)
#tubSchienale=R([2,3])([PI/2])(tubSchienale)
#tubSchienale=T([2])([4.25])(tubSchienale)


#VIEW(tubSchienale)

tubCurvSchienale=R([2,3])(PI)(tubo)
tubCurvSchienale=R([1,3])(-PI/2)(tubCurvSchienale)


#VIEW(tubCurvSchienale)


xtub=CYLINDER([0.125,8.5])(16)   
xtub=R([1,3])(PI/2)(xtub)
xtub=T([1,2,3])([-4.25,4.415,5.625])(xtub) 

#tubo vertical
tubSchienale8=T([2])([-0.875])(tubSchienale)
#VIEW(tubSchienale8)


#tubo orizz
tubSchienale7=CYLINDER([0.125,0.65])(16)
tubSchienale7=R([2,3])(PI/2)(tubSchienale7)
tubSchienale7=T([2,3])([0.65,-0.875])(tubSchienale7)
#VIEW(tubSchienale7)


#tubb curvo 2 schien
tubbbb=R([1,2])(PI)(tubo)
#VIEW(tubbbb)



xtub3=CYLINDER([0.125,6.5])(16)     #lunghezza stecca sedia 
xtub3=R([1,3])(-PI/2)(xtub3)
xtub3=T([1,2,3])([0,-0.875,0])(xtub3) 

#VIEW(xtub3)





tubSchienale5=CYLINDER([0.125,4.5])(16)
tubSchienale5=R([2,3])(PI/2)(tubSchienale5)
tubSchienale5=T([1,2,3])([-0.875,4.4,0])(tubSchienale5) 
#VIEW(tubSchienale5)



sed=STRUCT([tubbbb,xtub3,tubSchienale5])
#VIEW(sed)
sed=T([2])([-0.375])(sed) 


schi=STRUCT([tubCurvSchienale,tubSchienale7,tubSchienale8])
schi=T([2,3])([-1.75,0.625])(schi)           #1.75    0.3
#VIEW(schi)

tot=STRUCT([schi,sed])
tot=T([1,2,3,])([-0.88,-2,3.7])(tot)                     #verde 0.3                                 blu ok + 4 

tot=R([1,3])(0.3)(tot)




#VIEW(tot)


tot2=S([2])([-1])(tot)
tott=STRUCT([tot,tot2,modelF])
#VIEW(tott)



































cubo=CUBOID([8.2,0.05,1])
cubo=T([1,2,3])([-4.1,-3,5.75])(cubo)
#VIEW(cubo)



cubo2=CUBOID([8.2,0.75,0.05])
cubo2=T([1,2,3])([-4.1,-4.2,7.15])(cubo2)
#VIEW(cubo2)



cubo3=CUBOID([5.4,6.5,0.05])
cubo3=T([1,2,3])([-0.3,-3.25,3.7])(cubo3)
cubo3=R([1,3])(0.3)(cubo3)

#VIEW(cubo3)


cubo4=CUBOID([0.05,9.22,2])
cubo4=T([1,2,3])([-0.95,-4.6,8.13])(cubo4)
cubo4=R([1,3])(0.3)(cubo4)

#VIEW(cubo4)




cubo5=CUBOID([0.05,9.22,1.8])
cubo5=T([1,2,3])([-0.95,-4.6,4.1])(cubo5)
cubo5=R([1,3])(0.3)(cubo5)

#VIEW(cubo5)


cubo6=S([2])([-1])(cubo)
cubo7=S([2])([-1])(cubo2)


cuboidi=STRUCT([cubo,cubo2,cubo3,cubo4,cubo5,cubo6,cubo7])
cuboidi=COLOR([0.1,0.1,0.1])(cuboidi)
VIEW(STRUCT([cuboidi,tott]))








DISK