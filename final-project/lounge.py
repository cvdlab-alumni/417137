

domain = INTERVALS(1)(32)
controlpoints =   [[0.31,0, -0.57],[0.70,0, -0.97] ,[0.05,0, -0.9],[0.92,0, -1.90]]  # togli il - alle z
curveMapping = BEZIER(S1)(controlpoints)

curve = MAP(curveMapping)(domain)

#VIEW(curve)


domain = INTERVALS(1)(32)
controlpoints =   [[0.31,1.7, -0.57],[0.70,1.7, -0.97] ,[0.05,1.7, -0.9],[0.92,1.7, -1.90]]  # togli il - alle z
curveMapping2 = BEZIER(S1)(controlpoints)

curve2 = MAP(curveMapping2)(domain)

#VIEW(curve2)





domain = INTERVALS(1)(32)
controlpoints =   [[0.21,0, -0.57],[0.60,0, -0.97] ,[-0.05,0, -0.9],[0.82,0, -1.90]]  # togli il - alle z
curveMapping11 = BEZIER(S1)(controlpoints)

curve11 = MAP(curveMapping11)(domain)

#VIEW(curve11)


domain = INTERVALS(1)(32)
controlpoints =   [[0.21,1.7, -0.57],[0.60,1.7, -0.97] ,[-0.05,1.7, -0.9],[0.82,1.7, -1.90]]  # togli il - alle z
curveMapping12 = BEZIER(S1)(controlpoints)

curve12 = MAP(curveMapping12)(domain)

#VIEW(curve12)






#ctx.moveTo(88, 193)
#ctx.bezierCurveTo(178, 321, 174, 250, 244, 231)


domain = INTERVALS(1)(32)
controlpoints =   [[0.92,0, -1.90],[1.78,0, -3.11] ,[1.74,0, -2.6],[2.44,0, -2.31]]  # togli il - alle z
curveMapping3 = BEZIER(S1)(controlpoints)

curve3 = MAP(curveMapping3)(domain)

#VIEW(curve3)



domain = INTERVALS(1)(32)
controlpoints =   [[0.92,1.7, -1.90],[1.78,1.7, -3.11] ,[1.74,1.7, -2.6],[2.44,1.7, -2.31]]  # togli il - alle z
curveMapping4 = BEZIER(S1)(controlpoints)

curve4 = MAP(curveMapping4)(domain)

#VIEW(curve4)


domain = INTERVALS(1)(32)
controlpoints =   [[0.82,0, -1.90],[1.78,0, -3.21] ,[1.74,0, -2.7],[2.44,0, -2.41]]  # togli il - alle z
curveMapping13 = BEZIER(S1)(controlpoints)

curve13 = MAP(curveMapping13)(domain)

#VIEW(curve13)


domain = INTERVALS(1)(32)
controlpoints =   [[0.82,1.7, -1.90],[1.78,1.7, -3.21] ,[1.74,1.7, -2.7],[2.44,1.7, -2.41]]  # togli il - alle z
curveMapping14 = BEZIER(S1)(controlpoints)

curve14 = MAP(curveMapping14)(domain)

#VIEW(curve14)





#ctx.moveTo(246, 233)
#ctx.bezierCurveTo(333, 171, 346, 213, 398, 217)


domain = INTERVALS(1)(32)
controlpoints =   [[2.44,0, -2.31],[3.33,0, -1.81] ,[3.46,0, -2.03],[4.21,0, -2.17]]  # togli il - alle z
curveMapping5 = BEZIER(S1)(controlpoints)

curve5 = MAP(curveMapping5)(domain)

#VIEW(curve5)


domain = INTERVALS(1)(32)
controlpoints =   [[2.44,1.7, -2.31],[3.33,1.7, -1.81] ,[3.46,1.7, -2.03],[4.21,1.7, -2.17]]  # togli il - alle z
curveMapping6 = BEZIER(S1)(controlpoints)

curve6 = MAP(curveMapping6)(domain)

#VIEW(curve6)



domain = INTERVALS(1)(32)
controlpoints =   [[2.44,0, -2.41],[3.33,0, -1.91] ,[3.46,0, -2.13],[4.21,0, -2.27]]  # togli il - alle z
curveMapping15 = BEZIER(S1)(controlpoints)

curve15 = MAP(curveMapping15)(domain)

#VIEW(curve15)


domain = INTERVALS(1)(32)
controlpoints =   [[2.44,1.7, -2.41],[3.33,1.7, -1.91] ,[3.46,1.7, -2.13],[4.21,1.7, -2.27]]  # togli il - alle z
curveMapping16 = BEZIER(S1)(controlpoints)

curve16 = MAP(curveMapping16)(domain)

#VIEW(curve16)





#ctx.moveTo(421, 218)
#ctx.bezierCurveTo(451, 225, 433, 234, 451, 236)
#z è -y

domain = INTERVALS(1)(32)
controlpoints =   [[4.21,0, -2.17],[4.33,0, -2.2] ,[4.33,0, -2.34],[4.33,0, -2.36]]  # togli il - alle z
curveMapping7 = BEZIER(S1)(controlpoints)

#curve7 = MAP(curveMapping7)(domain)

#VIEW(curve7)

domain = INTERVALS(1)(32)
controlpoints =   [[4.21,1.7, -2.17],[4.33,1.7, -2.2] ,[4.33,1.7, -2.34],[4.33,1.7, -2.36]]  # togli il - alle z
curveMapping8 = BEZIER(S1)(controlpoints)

curve8 = MAP(curveMapping8)(domain)

#VIEW(curve8)





domain = INTERVALS(1)(32)
controlpoints =   [[4.21,0, -2.27],[4.29,0, -2.3] ,[4.29,0, -2.44]]  # togli il - alle z
curveMapping17 = BEZIER(S1)(controlpoints)

curve17 = MAP(curveMapping17)(domain)

#VIEW(curve17)



domain = INTERVALS(1)(32)
controlpoints =   [[4.21,1.7, -2.27],[4.29,1.7, -2.3] ,[4.29,1.7, -2.44]]  # togli il - alle z
curveMapping18 = BEZIER(S1)(controlpoints)

curve18 = MAP(curveMapping18)(domain)

#VIEW(curve18)









domain2 = Plasm.power(INTERVALS(1)(14),INTERVALS(1)(14))



out = MAP(BEZIER(S2)([curveMapping,curveMapping2]))(domain2)
out2 = MAP(BEZIER(S2)([curveMapping3,curveMapping4]))(domain2)
out3= MAP(BEZIER(S2)([curveMapping5,curveMapping6]))(domain2)
out4 = MAP(BEZIER(S2)([curveMapping7,curveMapping8]))(domain2)

outs = MAP(BEZIER(S2)([curveMapping11,curveMapping12]))(domain2)
outs2 = MAP(BEZIER(S2)([curveMapping13,curveMapping14]))(domain2)
outs3= MAP(BEZIER(S2)([curveMapping15,curveMapping16]))(domain2)
outs4 = MAP(BEZIER(S2)([curveMapping17,curveMapping18]))(domain2)

outt=STRUCT([out,out2,out3,out4,outs,outs2,outs3,outs4])


outp = MAP(BEZIER(S2)([curveMapping,curveMapping11]))(domain2)
outp2 = MAP(BEZIER(S2)([curveMapping3,curveMapping13]))(domain2)
outp3= MAP(BEZIER(S2)([curveMapping5,curveMapping15]))(domain2)
outp4 = MAP(BEZIER(S2)([curveMapping7,curveMapping17]))(domain2)

outp6 = MAP(BEZIER(S2)([curveMapping2,curveMapping12]))(domain2)
outp7 = MAP(BEZIER(S2)([curveMapping4,curveMapping14]))(domain2)
outp8= MAP(BEZIER(S2)([curveMapping6,curveMapping16]))(domain2)
outp9 = MAP(BEZIER(S2)([curveMapping8,curveMapping18]))(domain2)

outt2=STRUCT([outp,outp2,outp3,outp4,outp6,outp7,outp8,outp9])



outttot=STRUCT([outt,outt2])

outttot=COLOR([0,0,0.15])(outttot)

#VIEW(outttot)























#braccioli

#(33, 147)
#ctx.bezierCurveTo(79, 149, 78, 229, 122, 198)

domain = INTERVALS(1)(32)
controlpoints =   [[0.33,-0.23, -1.47],[0.79,-0.23, -1.49] ,[0.78,-0.23, -2.29],[1.22,-0.23, -1.98]]  # togli il - alle z
curveMapping20 = BEZIER(S1)(controlpoints)

curve20 = MAP(curveMapping20)(domain)

#VIEW(curve20)


domain = INTERVALS(1)(32)
controlpoints =   [[0.33,-0.46, -1.47],[0.79,-0.46, -1.49] ,[0.78,-0.46, -2.29],[1.22,-0.46, -1.98]]  # togli il - alle z
curveMapping20b = BEZIER(S1)(controlpoints)

curve20b = MAP(curveMapping20b)(domain)

#VIEW(curve20b)



domain = INTERVALS(1)(32)
controlpoints =   [[0.33,-0.23, -1.37],[0.79,-0.23, -1.39] ,[0.78,-0.23, -2.19],[1.22,-0.23, -1.88]]  # togli il - alle z
curveMapping30 = BEZIER(S1)(controlpoints)

curve30 = MAP(curveMapping30)(domain)

#VIEW(curve30)


domain = INTERVALS(1)(32)
controlpoints =   [[0.33,-0.46, -1.37],[0.79,-0.46, -1.39] ,[0.78,-0.46, -2.19],[1.22,-0.46, -1.88]]  # togli il - alle z
curveMapping30b = BEZIER(S1)(controlpoints)

curve30b = MAP(curveMapping30b)(domain)

#VIEW(curve30b)










#(118, 198)
#ctx.bezierCurveTo(185, 153, 207, 166, 178, 273)


domain = INTERVALS(1)(32)
controlpoints =   [[1.22,-0.23, -1.98],[1.85,-0.23, -1.53] ,[2.07,-0.23, -1.66],[1.78,-0.23, -2.73]]  # togli il - alle z  
curveMapping22 = BEZIER(S1)(controlpoints)

curve22 = MAP(curveMapping22)(domain)

#VIEW(curve22)

domain = INTERVALS(1)(32)
controlpoints =   [[1.22,-0.46, -1.98],[1.85,-0.46, -1.53] ,[2.07,-0.46, -1.66],[1.78,-0.46, -2.73]]  # togli il - alle z  
curveMapping22b = BEZIER(S1)(controlpoints)

curve22b = MAP(curveMapping22b)(domain)

#VIEW(curve22b)




domain = INTERVALS(1)(32)
controlpoints =   [[1.22,-0.23, -1.88],[1.85,-0.23, -1.43] ,[2.17,-0.23, -1.66],[1.88,-0.23, -2.73]]  # togli il - alle z  
curveMapping32 = BEZIER(S1)(controlpoints)

curve32 = MAP(curveMapping32)(domain)

#VIEW(curve32)



domain = INTERVALS(1)(32)
controlpoints =   [[1.22,-0.46, -1.88],[1.85,-0.46, -1.43] ,[2.17,-0.46, -1.66],[1.88,-0.46, -2.73]]  # togli il - alle z  
curveMapping32b = BEZIER(S1)(controlpoints)

curve32b = MAP(curveMapping32b)(domain)

#VIEW(curve32b)






#(178, 265)
#ctx.bezierCurveTo(173, 312, 177, 334, 79, 324)



domain = INTERVALS(1)(32)
controlpoints =   [[1.78,-0.23, -2.73],[1.68,-0.23, -3.17] ,[1.65,-0.23, -3.2],[0.79,-0.23, -3.17]]  # togli il - alle z       ultima z 3.24   penul   3.34  
curveMapping24 = BEZIER(S1)(controlpoints)

curve24 = MAP(curveMapping24)(domain)

#VIEW(curve24)


domain = INTERVALS(1)(32)
controlpoints =   [[1.78,-0.46, -2.73],[1.68,-0.46, -3.17] ,[1.65,-0.46, -3.2],[0.79,-0.46, -3.17]]  # togli il - alle z       ultima z 3.24   penul   3.34  
curveMapping24b = BEZIER(S1)(controlpoints)

curve24b = MAP(curveMapping24b)(domain)

#VIEW(curve24b)


domain = INTERVALS(1)(32)
controlpoints =   [[1.88,-0.23, -2.73],[1.78,-0.23, -3.17] ,[1.65,-0.23, -3.3],[0.79,-0.23, -3.22]]  # togli il - alle z       ultima z 3.24   penul   3.34  
curveMapping34 = BEZIER(S1)(controlpoints)

curve34 = MAP(curveMapping34)(domain)

#VIEW(curve34)


domain = INTERVALS(1)(32)
controlpoints =   [[1.88,-0.46, -2.73],[1.78,-0.46, -3.17] ,[1.65,-0.46, -3.3],[0.79,-0.46, -3.22]]  # togli il - alle z       ultima z 3.24   penul   3.34  
curveMapping34b = BEZIER(S1)(controlpoints)

curve34b = MAP(curveMapping34b)(domain)

#VIEW(curve34b)



#####################/


outp16 = MAP(BEZIER(S2)([curveMapping20,curveMapping20b]))(domain2)
outp17 = MAP(BEZIER(S2)([curveMapping22,curveMapping22b]))(domain2)
outp18= MAP(BEZIER(S2)([curveMapping24,curveMapping24b]))(domain2)

outt3=STRUCT([outp16,outp17,outp18])
#VIEW(outt3)


outp116 = MAP(BEZIER(S2)([curveMapping30,curveMapping30b]))(domain2)
outp117 = MAP(BEZIER(S2)([curveMapping32,curveMapping32b]))(domain2)
outp118= MAP(BEZIER(S2)([curveMapping34,curveMapping34b]))(domain2)

outt4=STRUCT([outp116,outp117,outp118])
#VIEW(outt4)


outp216 = MAP(BEZIER(S2)([curveMapping30,curveMapping20]))(domain2)
outp217 = MAP(BEZIER(S2)([curveMapping32,curveMapping22]))(domain2)
outp218= MAP(BEZIER(S2)([curveMapping34,curveMapping24]))(domain2)

outt5=STRUCT([outp216,outp217,outp218])
#VIEW(outt5)


outp316 = MAP(BEZIER(S2)([curveMapping30b,curveMapping20b]))(domain2)
outp317 = MAP(BEZIER(S2)([curveMapping32b,curveMapping22b]))(domain2)
outp318= MAP(BEZIER(S2)([curveMapping34b,curveMapping24b]))(domain2)
outt6=STRUCT([outp316,outp317,outp318])
#VIEW(outt6)



outt_tot1=STRUCT([outt3,outt4,outt5,outt6])

halfBracc=S([2])([-1])(outt_tot1)
halfBracc=T([2])([1.7+0.46+0.23])(outt_tot1)




#VIEW(outt_tot1)
#VIEW(halfBracc)

var2=(COLOR([235/256,181/256,95/256])(STRUCT([outt_tot1,halfBracc])))


#235 181 95























# cordolo
#(390, 252)
#ctx.bezierCurveTo(396, 204, 315, 193, 285, 213)

domain = INTERVALS(1)(32)
controlpoints =   [[3.9,0, -2.52],[3.96,0, -2.04] ,[3.15,0, -1.93],[2.85,0, -2.13]]  # togli il - alle z
curveMapping124 = BEZIER(S1)(controlpoints)

curve124 = MAP(curveMapping124)(domain)

#VIEW(curve124)

domain = INTERVALS(1)(32)
controlpoints =   [[3.9,-0.23, -2.52],[3.96,-0.23, -2.04] ,[3.15,-0.23, -1.93],[2.85,-0.23, -2.13]]  # togli il - alle z
curveMapping124b = BEZIER(S1)(controlpoints)

curve124b = MAP(curveMapping124b)(domain)

#VIEW(curve124b)



domain = INTERVALS(1)(32)
controlpoints =   [[3.83,0, -2.52],[3.86,0, -2.04] ,[3.15,0, -2.03],[2.85,0, -2.23]]  # togli il - alle z
curveMapping34 = BEZIER(S1)(controlpoints)

curve34 = MAP(curveMapping34)(domain)

#VIEW(curve34)


domain = INTERVALS(1)(32)
controlpoints =   [[3.83,-0.23, -2.52],[3.86,-0.23, -2.04] ,[3.15,-0.23, -2.03],[2.85,-0.23, -2.23]]  # togli il - alle z
curveMapping34b = BEZIER(S1)(controlpoints)

curve34b = MAP(curveMapping34b)(domain)

#VIEW(curve34b)




#(256, 315)
#ctx.bezierCurveTo(326, 313, 380, 345, 393, 253)

domain = INTERVALS(1)(32)
controlpoints =   [[2.56,0, -3.20],[3.26,0, -3.13] ,[3.80,0, -3.45],[3.9,0, -2.52]]  # togli il - alle z
curveMapping26 = BEZIER(S1)(controlpoints)

curve26 = MAP(curveMapping26)(domain)

#VIEW(curve26)


domain = INTERVALS(1)(32)
controlpoints =   [[2.56,-0.23, -3.20],[3.26,-0.23, -3.13] ,[3.80,-0.23, -3.45],[3.9,-0.23, -2.52]]  # togli il - alle z
curveMapping26b = BEZIER(S1)(controlpoints)

curve26b = MAP(curveMapping26b)(domain)

#VIEW(curve26b)


domain = INTERVALS(1)(32)
controlpoints =   [[2.56,0, -3.13],[3.26,0, -3.03] ,[3.70,0, -3.45],[3.83,0, -2.52]]  # togli il - alle z
curveMapping36 = BEZIER(S1)(controlpoints)

curve36 = MAP(curveMapping36)(domain)

#VIEW(curve36)

domain = INTERVALS(1)(32)
controlpoints =   [[2.56,-0.23, -3.13],[3.26,-0.23, -3.03] ,[3.70,-0.23, -3.45],[3.83,-0.23, -2.52]]  # togli il - alle z
curveMapping36b = BEZIER(S1)(controlpoints)

curve36b = MAP(curveMapping36b)(domain)

#VIEW(curve36b)






#2.56 -3.15

#(258, 313)
#ctx.bezierCurveTo(219, 310, 184, 315, 88, 317)


domain = INTERVALS(1)(32)
controlpoints =   [[2.56,0, -3.20],[2.18,0, -3.22] ,[1.84,0, -3.20],[0.79,0, -3.22]]  # togli il - alle z
curveMapping28 = BEZIER(S1)(controlpoints)

curve28 = MAP(curveMapping28)(domain)

#VIEW(curve28)


domain = INTERVALS(1)(32)
controlpoints =   [[2.56,-0.23, -3.20],[2.18,-0.23, -3.22] ,[1.84,-0.23, -3.20],[0.79,-0.23, -3.22]]  # togli il - alle z
curveMapping28b = BEZIER(S1)(controlpoints)

curve28b = MAP(curveMapping28b)(domain)

#VIEW(curve28b)



domain = INTERVALS(1)(32)
controlpoints =   [[2.56,0, -3.13],[2.18,0, -3.12] ,[1.84,0, -3.12],[0.79,0, -3.14]]  # togli il - alle z
curveMapping38 = BEZIER(S1)(controlpoints)

curve38 = MAP(curveMapping38)(domain)

#VIEW(curve38)

domain = INTERVALS(1)(32)
controlpoints =   [[2.56,-0.23, -3.13],[2.18,-0.23, -3.12] ,[1.84,-0.23, -3.12],[0.79,-0.23, -3.14]]  # togli il - alle z
curveMapping38b = BEZIER(S1)(controlpoints)

curve38b = MAP(curveMapping38b)(domain)

#VIEW(curve38b)




outp416 = MAP(BEZIER(S2)([curveMapping124,curveMapping124b]))(domain2)
outp417 = MAP(BEZIER(S2)([curveMapping26,curveMapping26b]))(domain2)
outp418= MAP(BEZIER(S2)([curveMapping28,curveMapping28b]))(domain2)

outt7=STRUCT([outp416,outp417,outp418])

#VIEW(outt7)



outp516 = MAP(BEZIER(S2)([curveMapping34,curveMapping34b]))(domain2)
outp517 = MAP(BEZIER(S2)([curveMapping36,curveMapping36b]))(domain2)
outp518= MAP(BEZIER(S2)([curveMapping38,curveMapping38b]))(domain2)

outt8=STRUCT([outp516,outp517,outp518])

#VIEW(outt8)


outp616 = MAP(BEZIER(S2)([curveMapping124,curveMapping34]))(domain2)
outp617 = MAP(BEZIER(S2)([curveMapping26,curveMapping36]))(domain2)
outp618= MAP(BEZIER(S2)([curveMapping28,curveMapping38]))(domain2)

outt9=STRUCT([outp616,outp617,outp618])

#VIEW(outt9)



outp716 = MAP(BEZIER(S2)([curveMapping124b,curveMapping34b]))(domain2)
outp717 = MAP(BEZIER(S2)([curveMapping26b,curveMapping36b]))(domain2)
outp718= MAP(BEZIER(S2)([curveMapping28b,curveMapping38b]))(domain2)

outt10=STRUCT([outp716,outp717,outp718])

#VIEW(outt10)

outt_tot2=STRUCT([outt7,outt8,outt9,outt10])

#VIEW(outt_tot2)

halfCordolo=S([2])([-1])(outt_tot2)
halfCordolo=T([2])([1.7+0.23])(outt_tot2)
#VIEW(halfCordolo)



var3=(COLOR([235/256,181/256,95/256])(STRUCT([outt_tot2,halfCordolo])))






















#(161, 183)
#ctx.bezierCurveTo(180, 176, 171, 319, 130, 317)



domain = INTERVALS(1)(32)
controlpoints =   [[1.61,-0.23, -1.83],[1.76,-0.23, -1.76] ,[1.71,-0.23, -3.19],[1.38,-0.23, -3.17]]  # togli il - alle z
curveMapping50 = BEZIER(S1)(controlpoints)

curve50 = MAP(curveMapping50)(domain)

#VIEW(curve50)



domain = INTERVALS(1)(32)
controlpoints =   [[1.71,-0.23, -1.83],[1.9,-0.23, -1.76] ,[1.86,-0.23, -3.19],[1.5,-0.23, -3.17]]  # togli il - alle z
curveMapping50b = BEZIER(S1)(controlpoints)

curve50b = MAP(curveMapping50b)(domain)

#VIEW(curve50b)


outp8716 = MAP(BEZIER(S2)([curveMapping50b,curveMapping50]))(domain2)
outp8716=S([1,3])([1.8,1.08])(outp8716)
outp8716=T([1,3])([-1.3,0.25])(outp8716)
#VIEW(outp8716)


halfSlice=S([2])([-1])(outp8716)
halfSlice=T([2])([1.7])(halfSlice)
#VIEW(halfSlice)


var4=(COLOR([235/256,181/256,95/256])(STRUCT([halfSlice,outp8716])))





cubo=CUBOID([0.08,1.7+0.46+0.3,0.3])
cubo=T([2,3])([-0.23-0.15,-2])(cubo)
cubo=R([1,3])(0.6)(cubo)
cubo=T([1,3])([-0.4,-0.25])(cubo)

cubo=(COLOR([235/256,181/256,95/256])(cubo))




VIEW(STRUCT([cubo,var4,var3,var2,outttot]))