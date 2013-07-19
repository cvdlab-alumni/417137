
domain=Plasm.power(INTERVALS(1)(14),INTERVALS(1)(14))
c1 = CUBICHERMITE(S1)([[1,0,0],[0,0,-1],[0,0,-2],[-3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0.8,0,0],[0,0,-0.8],[0,0,-1.8],[-2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain);
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain);
tubo=STRUCT([out,out2])

#VIEW(tubo)



cyl=CYLINDER([0.1,4])(16)
cyl=R([1,3])(PI/2)(cyl)
cyl=T([1,3])([0,-0.9])(cyl)
#VIEW(cyl)




c1 = CUBICHERMITE(S1)([[-1,0,0],[0,0,-1],[0,0,-2],[3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[-0.8,0,0],[0,0,-0.8],[0,0,-1.8],[2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo2=STRUCT([out,out2])

tubo2=T([1,3])([-4,-0])(tubo2)
#VIEW(tubo2)





cyl2=CYLINDER([0.1,5.5])(16)
#cyl=R([1,3])([PI/2])(cyl)
cyl2=T([1, 3])([0.9,0])(cyl2)
#VIEW(cyl2)



#############################################################################################qui qui 

c1 = CUBICHERMITE(S1)([[0,-1,0],[0,0,1],[0,0,2],[0,3,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0,-0.8,0],[0,0,0.8],[0,0,1.8],[0,2.6,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[-0.4,0,0],[0.4,0,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0.4,0,0],[-0.4,0,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo3=STRUCT([out,out2])

tubo3=T([1,2,3])([0.9,0.9,5.5])(tubo3)
#VIEW(tubo3)



cyl3=CYLINDER([0.1,2])(16)
cyl3=R([2,3])(PI/2)(cyl3)
cyl3=T([1,2,3])([0.9,2.9,6.4])(cyl3)
#VIEW(cyl3)




cyl4=CYLINDER([0.1,5.5])(16)
#cyl=R([1,3])([PI/2])(cyl)
cyl4=T([1,3])([-4.9,-0])(cyl4)
#VIEW(cyl4)





c1 = CUBICHERMITE(S1)([[0,-1,0],[0,0,1],[0,0,2],[0,3,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0,-0.8,0],[0,0,0.8],[0,0,1.8],[0,2.6,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[-0.4,0,0],[0.4,0,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0.4,0,0],[-0.4,0,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo4=STRUCT([out,out2])

tubo4=T([1,2,3])([-4.9,0.9,5.5])(tubo4)
#VIEW(tubo4)



cyl5=CYLINDER([0.1,2])(16)
cyl5=R([2,3])(PI/2)(cyl5)
cyl5=T([1,2,3])([-4.9,2.9,6.4])(cyl5)
#VIEW(cyl5)




half=STRUCT([cyl,cyl2,cyl3,cyl4,cyl5,tubo,tubo2,tubo3,tubo4])
half=T([1,2])([0.4,-2.9])(half)


half2=S([2])([-1])(half)











c1 = CUBICHERMITE(S1)([[1,0,0],[0,1,0],[0,2,0],[-3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0.8,0,0],[0,0.8,0],[0,1.8,0],[-2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,0,0.4],[0,0,-0.4]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0,-0.4],[0,0,0.4]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo20=STRUCT([out,out2])

tubo20=T([1,2,3])([1.4,1.8,5.2])(tubo20)
#VIEW(tubo20)




cyl20=CYLINDER([0.1,6])(16)
cyl20=R([1,3])(PI/2)(cyl20)
cyl20=T([1,2,3])([1.45,2.7,5.2])(cyl20)
#VIEW(cyl20)







cyl21=CYLINDER([0.1,1.8])(16)
cyl21=R([2,3])(PI/2)(cyl21)
cyl21=T([1,2,3])([2.3,1.8,5.2])(cyl21)
#VIEW(cyl21)


cyl22=CYLINDER([0.1,1.8])(16)
cyl22=R([2,3])(PI/2)(cyl22)
cyl22=T([1,2,3])([-5.5,1.8,5.2])(cyl22)
#VIEW(cyl22)







c1 = CUBICHERMITE(S1)([[-1,0,0],[0,1,0],[0,2,0],[3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[-0.8,0,0],[0,0.8,0],[0,1.8,0],[2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,0,0.4],[0,0,-0.4]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0,-0.4],[0,0,0.4]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo21=STRUCT([out,out2])

tubo21=T([1,2,3])([-4.6,1.8,5.2])(tubo21)
#VIEW(tubo21)




half22=STRUCT([tubo20,tubo21,cyl20,cyl21,cyl22]);

half23=S([2])([-1])(half22)




model=STRUCT([half,half2,half22,half23])
VIEW(model)