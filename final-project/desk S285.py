cyl=CYLINDER([0.1,3])(16)  #############5.5--------------------->3.5
#cyl=R([1,3])([PI/2])(cyl)
cyl=T([1,3])([0.9,0])(cyl)
#VIEW(cyl)




domain=Plasm.power(INTERVALS(1)(14),INTERVALS(1)(14))

c1 = CUBICHERMITE(S1)([[1,0,0],[0,0,-1],[0,0,-2],[-3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0.8,0,0],[0,0,-0.8],[0,0,-1.8],[-2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo=STRUCT([out,out2])

#VIEW(tubo)




cyl2=CYLINDER([0.1,1.5])(16)  #############5.5--------------------->3.5
cyl2=R([1,3])(-PI/2)(cyl2)
cyl2=T([1,3])([-1.5,-0.9])(cyl2)
#VIEW(cyl2)






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
tubo2=T([1])([-1.5])(tubo2)

#VIEW(tubo2)



cyl3=CYLINDER([0.1,3.4])(16)  #############5.5--------------------->3.5
#cyl=R([1,3])([PI/2])(cyl)
cyl3=T([1,3])([-2.4,0])(cyl3)
#VIEW(cyl3)





c1 = CUBICHERMITE(S1)([[-1,0,0],[0,0,1],[0,0,2],[3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[-0.8,0,0],[0,0,0.8],[0,0,1.8],[2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo3=STRUCT([out,out2])
tubo3=T([1,3])([-1.5,3.4])(tubo3)
#VIEW(tubo3)





cyl4=CYLINDER([0.1,7.6])(16)  #############5.5--------------------->3.5
cyl4=R([1,3])(-PI/2)(cyl4)
cyl4=T([1,3])([-1.5,4.3])(cyl4)
#VIEW(cyl4)




c1 = CUBICHERMITE(S1)([[1,0,0],[0,0,1],[0,0,2],[-3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0.8,0,0],[0,0,0.8],[0,0,1.8],[-2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo4=STRUCT([out,out2])
tubo4=T([1,3])([6.1,3.4])(tubo4)

#VIEW(tubo4)





cyl5=CYLINDER([0.1,3.4])(16)  #############5.5--------------------->3.5
#cyl=R([1,3])([PI/2])(cyl)
cyl5=T([1,3])([7,0])(cyl5)
#VIEW(cyl5)





c1 = CUBICHERMITE(S1)([[-1,0,0],[0,0,-1],[0,0,-2],[3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[-0.8,0,0],[0,0,-0.8],[0,0,-1.8],[2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo5=STRUCT([out,out2])
tubo5=T([1])([7.9])(tubo5)

#VIEW(tubo5)




cyl6=CYLINDER([0.1,1.5])(16)  #############5.5--------------------->3.5
cyl6=R([1,3])(-PI/2)(cyl6)
cyl6=T([1,3])([7.9,-0.9])(cyl6)
#VIEW(cyl6)




c1 = CUBICHERMITE(S1)([[1,0,0],[0,0,-1],[0,0,-2],[-3,0,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0.8,0,0],[0,0,-0.8],[0,0,-1.8],[-2.6,0,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo6=STRUCT([out,out2])
tubo6=T([1])([9.4])(tubo6)
#VIEW(tubo6)






cyl7=CYLINDER([0.1,2.5])(16)  #############5.5--------------------->3.5
#cyl=R([1,3])([PI/2])(cyl)
cyl7=T([1,3])([10.3,0])(cyl7)
#VIEW(cyl7)





c1 = CUBICHERMITE(S1)([[0,-1,0],[0,0,1],[0,0,2],[0,3,0]]);
#VIEW(MAP(c1)(INTERVALS(1)(14)));

c2 = CUBICHERMITE(S1)([[0,-0.8,0],[0,0,0.8],[0,0,1.8],[0,2.6,0]]);
#VIEW(MAP(c2)(INTERVALS(1)(14)));

sur3 = CUBICHERMITE(S2)([c1,c2,[-0.4,0,0],[0.4,0,0]]);
out = MAP(sur3)(domain); #mezzo tubo
#VIEW(out);

sur31 = CUBICHERMITE(S2)([c1,c2,[0.4,0,0],[-0.4,0,0]]);
out2 = MAP(sur31)(domain); #mezzo tubo
tubo7=STRUCT([out,out2])
tubo7=T([1,2,3])([10.3,0.9,2.5])(tubo7)

#VIEW(tubo7)




cyl8=CYLINDER([0.1,1])(16)  #############5.5--------------------->3.5
cyl8=R([2,3])(PI/2)(cyl8)
cyl8=T([1,2,3])([10.3,1.8,3.4])(cyl8)
#VIEW(cyl8)




half=STRUCT([cyl,tubo2,cyl2,tubo3,cyl3,tubo4,cyl4,tubo5,cyl5,tubo6,cyl6,tubo7,cyl7,tubo,cyl8])


half=T([2])([-1.8])(half)

half2=S([2])([-1])(half)

tot=(STRUCT([half,half2]))

tot=T([2])([1.8])(tot)


cassetto=(CUBOID([3.2,3.6,1]))
cassetto=T([1])([-2.375])(cassetto)
cassetto=COLOR([0.1,0.1,0.1])(cassetto)
#VIEW(cassetto)
maniglia=(CUBOID([0.8,0.2,0.15]))
maniglia=T([1,2,3])([-1.19,-0.2,0.5])(maniglia)
#VIEW(maniglia)

cassetto2=(CUBOID([3.2,3.6,1]))
cassetto2=T([1,3])([-2.375,1.02])(cassetto2)
cassetto2=COLOR([0.1,0.1,0.1])(cassetto2)
maniglia2=(CUBOID([0.8,0.2,0.15]))
maniglia2=T([1,2,3])([-1.19,-0.2,1.5])(maniglia2)
#VIEW(maniglia2)
#VIEW(cassetto2)

cassetto3=(CUBOID([3.2,3.6,1]))
cassetto3=T([1,3])([-2.375,2.04])(cassetto3)
cassetto3=COLOR([0.1,0.1,0.1])(cassetto3)
maniglia3=(CUBOID([0.8,0.2,0.15]))
maniglia3=T([1,2,3])([-1.19,-0.2,2.5])(maniglia3)
#VIEW(maniglia3)
#VIEW(cassetto3)



cassetto2a=(CUBOID([3.2,3.6,0.9]))
cassetto2a=T([1,3])([7,1.1])(cassetto2a)
cassetto2a=COLOR([0.1,0.1,0.1])(cassetto2a)
maniglia4=(CUBOID([0.8,0.2,0.15]))
maniglia4=T([1,2,3])([8.3,-0.2,2.4])(maniglia4)
#VIEW(maniglia4)
#VIEW(cassetto2a)

cassetto2a2=(CUBOID([3.2,3.6,0.9]))
cassetto2a2=T([1,3])([7,2.02])(cassetto2a2)
cassetto2a2=COLOR([0.1,0.1,0.1])(cassetto2a2)
maniglia5=(CUBOID([0.8,0.2,0.15]))
maniglia5=T([1,2,3])([8.3,-0.2,1.5])(maniglia5)
#VIEW(maniglia5)
#VIEW(cassetto2a2)


tavola=(CUBOID([8.3,3.6,0.1]))
tavola=T([1,3])([-1.9,4.3])(tavola)
tavola=COLOR([0.1,0.1,0.1])(tavola)
#VIEW(tavola)


VIEW(STRUCT([tot,cassetto,maniglia,cassetto2,maniglia2,cassetto3,maniglia3,cassetto2a,maniglia4,cassetto2a2,maniglia5,tavola]))