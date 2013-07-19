T = function (dims) { 
  dims = dims.map(function(item){ 
    return item-1; 
  }); 
  return function (values) { 
    return function (object) { 
      return object.clone().translate(dims,values); 
    }; 
  }; 
} 
  
S = function (dims) { 
  dims = dims.map(function(item){ 
    return item-1; 
  }); 
    return function (values) { 
      return function (object) { 
        return object.clone().scale(dims, values); 
      }; 
    }; 
  } 
  
 R = function (dims) { 
  dims = dims.map(function(item){ 
    return item-1; 
  }); 
    return function (angle) { 
      return function (object) { 
        return object.clone().rotate(dims, angle); 
      }; 
    }; 
  } 

//cerchi per bezier
function circl (sel) {
return function (r) {
return function (d_z) {
return function (p) {
return [ r * COS(sel(p)), r * SIN(sel(p)), d_z ];
};
};
};
};

  
  S3 = S2; 
  S2 = S1; 
  S1 = S0; 
  
  GRID = SIMPLEX_GRID 
  
  VIEW = DRAW 
  
  redd =[1,0.5,0]
  red = [1,0,0]; 
  blue = [0,0,1]; 
  green = [0,1,0]; 
  yellow = [1,1,0]; 
  black = [0.3,0.3,0.3]; 
  white = [1,1,1]; 
  dark_grey = [41/256,41/256,41/256]; 
  gold = [205/256,173/256,0]; 
  glass_color = [185/256,211/256,238/256,0.6]; 






 // ctx.moveTo(3.1, 5.7);
// ctx.bezierCurveTo(7.0, 9.7, 0.5, 12.4, 9.2, 19.0);





var domain = INTERVALS(1)(32);
var controlpoints =   [[0.31,0, -0.57],[0.70,0, -0.97] ,[0.05,0, -0.9],[0.92,0, -1.90]];  // togli il - alle z
var curveMapping = BEZIER(S0)(controlpoints);

var curve = MAP(curveMapping)(domain);

//DRAW(curve)


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.31,1.7, -0.57],[0.70,1.7, -0.97] ,[0.05,1.7, -0.9],[0.92,1.7, -1.90]];  // togli il - alle z
var curveMapping2 = BEZIER(S0)(controlpoints);

var curve2 = MAP(curveMapping2)(domain);

//DRAW(curve2)





var domain = INTERVALS(1)(32);
var controlpoints =   [[0.21,0, -0.57],[0.60,0, -0.97] ,[-0.05,0, -0.9],[0.82,0, -1.90]];  // togli il - alle z
var curveMapping11 = BEZIER(S0)(controlpoints);

var curve11 = MAP(curveMapping11)(domain);

//DRAW(curve11)


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.21,1.7, -0.57],[0.60,1.7, -0.97] ,[-0.05,1.7, -0.9],[0.82,1.7, -1.90]];  // togli il - alle z
var curveMapping12 = BEZIER(S0)(controlpoints);

var curve12 = MAP(curveMapping12)(domain);

//DRAW(curve12)






//ctx.moveTo(88, 193);
//ctx.bezierCurveTo(178, 321, 174, 250, 244, 231);


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.92,0, -1.90],[1.78,0, -3.11] ,[1.74,0, -2.6],[2.44,0, -2.31]];  // togli il - alle z
var curveMapping3 = BEZIER(S0)(controlpoints);

var curve3 = MAP(curveMapping3)(domain);

//DRAW(curve3)



var domain = INTERVALS(1)(32);
var controlpoints =   [[0.92,1.7, -1.90],[1.78,1.7, -3.11] ,[1.74,1.7, -2.6],[2.44,1.7, -2.31]];  // togli il - alle z
var curveMapping4 = BEZIER(S0)(controlpoints);

var curve4 = MAP(curveMapping4)(domain);

//DRAW(curve4)


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.82,0, -1.90],[1.78,0, -3.21] ,[1.74,0, -2.7],[2.44,0, -2.41]];  // togli il - alle z
var curveMapping13 = BEZIER(S0)(controlpoints);

var curve13 = MAP(curveMapping13)(domain);

//DRAW(curve13)


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.82,1.7, -1.90],[1.78,1.7, -3.21] ,[1.74,1.7, -2.7],[2.44,1.7, -2.41]];  // togli il - alle z
var curveMapping14 = BEZIER(S0)(controlpoints);

var curve14 = MAP(curveMapping14)(domain);

//DRAW(curve14)





//ctx.moveTo(246, 233);
//ctx.bezierCurveTo(333, 171, 346, 213, 398, 217);


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.44,0, -2.31],[3.33,0, -1.81] ,[3.46,0, -2.03],[4.21,0, -2.17]];  // togli il - alle z
var curveMapping5 = BEZIER(S0)(controlpoints);

var curve5 = MAP(curveMapping5)(domain);

//DRAW(curve5)


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.44,1.7, -2.31],[3.33,1.7, -1.81] ,[3.46,1.7, -2.03],[4.21,1.7, -2.17]];  // togli il - alle z
var curveMapping6 = BEZIER(S0)(controlpoints);

var curve6 = MAP(curveMapping6)(domain);

//DRAW(curve6)



var domain = INTERVALS(1)(32);
var controlpoints =   [[2.44,0, -2.41],[3.33,0, -1.91] ,[3.46,0, -2.13],[4.21,0, -2.27]];  // togli il - alle z
var curveMapping15 = BEZIER(S0)(controlpoints);

var curve15 = MAP(curveMapping15)(domain);

//DRAW(curve15)


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.44,1.7, -2.41],[3.33,1.7, -1.91] ,[3.46,1.7, -2.13],[4.21,1.7, -2.27]];  // togli il - alle z
var curveMapping16 = BEZIER(S0)(controlpoints);

var curve16 = MAP(curveMapping16)(domain);

//DRAW(curve16)





//ctx.moveTo(421, 218);
//ctx.bezierCurveTo(451, 225, 433, 234, 451, 236);
//z è -y

var domain = INTERVALS(1)(32);
var controlpoints =   [[4.21,0, -2.17],[4.33,0, -2.2] ,[4.33,0, -2.34],[4.33,0, -2.36]];  // togli il - alle z
var curveMapping7 = BEZIER(S0)(controlpoints);

//var curve7 = MAP(curveMapping7)(domain);

//DRAW(curve7)

var domain = INTERVALS(1)(32);
var controlpoints =   [[4.21,1.7, -2.17],[4.33,1.7, -2.2] ,[4.33,1.7, -2.34],[4.33,1.7, -2.36]];  // togli il - alle z
var curveMapping8 = BEZIER(S0)(controlpoints);

var curve8 = MAP(curveMapping8)(domain);

//DRAW(curve8)





var domain = INTERVALS(1)(32);
var controlpoints =   [[4.21,0, -2.27],[4.29,0, -2.3] ,[4.29,0, -2.44]];  // togli il - alle z
var curveMapping17 = BEZIER(S0)(controlpoints);

var curve17 = MAP(curveMapping17)(domain);

//DRAW(curve17)



var domain = INTERVALS(1)(32);
var controlpoints =   [[4.21,1.7, -2.27],[4.29,1.7, -2.3] ,[4.29,1.7, -2.44]];  // togli il - alle z
var curveMapping18 = BEZIER(S0)(controlpoints);

var curve18 = MAP(curveMapping18)(domain);

//DRAW(curve18)









var domain2 = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);


var out = MAP(BEZIER(S2)([curveMapping,curveMapping2]))(domain2);
var out2 = MAP(BEZIER(S2)([curveMapping3,curveMapping4]))(domain2);
var out3= MAP(BEZIER(S2)([curveMapping5,curveMapping6]))(domain2);
var out4 = MAP(BEZIER(S2)([curveMapping7,curveMapping8]))(domain2);

var outs = MAP(BEZIER(S2)([curveMapping11,curveMapping12]))(domain2);
var outs2 = MAP(BEZIER(S2)([curveMapping13,curveMapping14]))(domain2);
var outs3= MAP(BEZIER(S2)([curveMapping15,curveMapping16]))(domain2);
var outs4 = MAP(BEZIER(S2)([curveMapping17,curveMapping18]))(domain2);

outt=STRUCT([out,out2,out3,out4,outs,outs2,outs3,outs4])


var outp = MAP(BEZIER(S2)([curveMapping,curveMapping11]))(domain2);
var outp2 = MAP(BEZIER(S2)([curveMapping3,curveMapping13]))(domain2);
var outp3= MAP(BEZIER(S2)([curveMapping5,curveMapping15]))(domain2);
var outp4 = MAP(BEZIER(S2)([curveMapping7,curveMapping17]))(domain2);

var outp6 = MAP(BEZIER(S2)([curveMapping2,curveMapping12]))(domain2);
var outp7 = MAP(BEZIER(S2)([curveMapping4,curveMapping14]))(domain2);
var outp8= MAP(BEZIER(S2)([curveMapping6,curveMapping16]))(domain2);
var outp9 = MAP(BEZIER(S2)([curveMapping8,curveMapping18]))(domain2);

outt2=STRUCT([outp,outp2,outp3,outp4,outp6,outp7,outp8,outp9])



outttot=STRUCT([outt,outt2])

outttot=COLOR([0,0,0.15])(outttot)

//DRAW(outttot)

























//braccioli

//(33, 147);
//ctx.bezierCurveTo(79, 149, 78, 229, 122, 198);

var domain = INTERVALS(1)(32);
var controlpoints =   [[0.33,-0.23, -1.47],[0.79,-0.23, -1.49] ,[0.78,-0.23, -2.29],[1.22,-0.23, -1.98]];  // togli il - alle z
var curveMapping20 = BEZIER(S0)(controlpoints);

var curve20 = MAP(curveMapping20)(domain);

//DRAW(curve20)


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.33,-0.46, -1.47],[0.79,-0.46, -1.49] ,[0.78,-0.46, -2.29],[1.22,-0.46, -1.98]];  // togli il - alle z
var curveMapping20b = BEZIER(S0)(controlpoints);

var curve20b = MAP(curveMapping20b)(domain);

//DRAW(curve20b)



var domain = INTERVALS(1)(32);
var controlpoints =   [[0.33,-0.23, -1.37],[0.79,-0.23, -1.39] ,[0.78,-0.23, -2.19],[1.22,-0.23, -1.88]];  // togli il - alle z
var curveMapping30 = BEZIER(S0)(controlpoints);

var curve30 = MAP(curveMapping30)(domain);

//DRAW(curve30)


var domain = INTERVALS(1)(32);
var controlpoints =   [[0.33,-0.46, -1.37],[0.79,-0.46, -1.39] ,[0.78,-0.46, -2.19],[1.22,-0.46, -1.88]];  // togli il - alle z
var curveMapping30b = BEZIER(S0)(controlpoints);

var curve30b = MAP(curveMapping30b)(domain);

//DRAW(curve30b)










//(118, 198);
//ctx.bezierCurveTo(185, 153, 207, 166, 178, 273);


var domain = INTERVALS(1)(32);
var controlpoints =   [[1.22,-0.23, -1.98],[1.85,-0.23, -1.53] ,[2.07,-0.23, -1.66],[1.78,-0.23, -2.73]];  // togli il - alle z  
var curveMapping22 = BEZIER(S0)(controlpoints);

var curve22 = MAP(curveMapping22)(domain);

//DRAW(curve22)

var domain = INTERVALS(1)(32);
var controlpoints =   [[1.22,-0.46, -1.98],[1.85,-0.46, -1.53] ,[2.07,-0.46, -1.66],[1.78,-0.46, -2.73]];  // togli il - alle z  
var curveMapping22b = BEZIER(S0)(controlpoints);

var curve22b = MAP(curveMapping22b)(domain);

//DRAW(curve22b)




var domain = INTERVALS(1)(32);
var controlpoints =   [[1.22,-0.23, -1.88],[1.85,-0.23, -1.43] ,[2.17,-0.23, -1.66],[1.88,-0.23, -2.73]];  // togli il - alle z  
var curveMapping32 = BEZIER(S0)(controlpoints);

var curve32 = MAP(curveMapping32)(domain);

//DRAW(curve32)



var domain = INTERVALS(1)(32);
var controlpoints =   [[1.22,-0.46, -1.88],[1.85,-0.46, -1.43] ,[2.17,-0.46, -1.66],[1.88,-0.46, -2.73]];  // togli il - alle z  
var curveMapping32b = BEZIER(S0)(controlpoints);

var curve32b = MAP(curveMapping32b)(domain);

//DRAW(curve32b)






//(178, 265);
//ctx.bezierCurveTo(173, 312, 177, 334, 79, 324);



var domain = INTERVALS(1)(32);
var controlpoints =   [[1.78,-0.23, -2.73],[1.68,-0.23, -3.17] ,[1.65,-0.23, -3.2],[0.79,-0.23, -3.17]];  // togli il - alle z       ultima z 3.24   penul   3.34  
var curveMapping24 = BEZIER(S0)(controlpoints);

var curve24 = MAP(curveMapping24)(domain);

//DRAW(curve24)


var domain = INTERVALS(1)(32);
var controlpoints =   [[1.78,-0.46, -2.73],[1.68,-0.46, -3.17] ,[1.65,-0.46, -3.2],[0.79,-0.46, -3.17]];  // togli il - alle z       ultima z 3.24   penul   3.34  
var curveMapping24b = BEZIER(S0)(controlpoints);

var curve24b = MAP(curveMapping24b)(domain);

//DRAW(curve24b)


var domain = INTERVALS(1)(32);
var controlpoints =   [[1.88,-0.23, -2.73],[1.78,-0.23, -3.17] ,[1.65,-0.23, -3.3],[0.79,-0.23, -3.22]];  // togli il - alle z       ultima z 3.24   penul   3.34  
var curveMapping34 = BEZIER(S0)(controlpoints);

var curve34 = MAP(curveMapping34)(domain);

//DRAW(curve34)


var domain = INTERVALS(1)(32);
var controlpoints =   [[1.88,-0.46, -2.73],[1.78,-0.46, -3.17] ,[1.65,-0.46, -3.3],[0.79,-0.46, -3.22]];  // togli il - alle z       ultima z 3.24   penul   3.34  
var curveMapping34b = BEZIER(S0)(controlpoints);

var curve34b = MAP(curveMapping34b)(domain);

//DRAW(curve34b)



///////////////////////////////////////////


var outp16 = MAP(BEZIER(S2)([curveMapping20,curveMapping20b]))(domain2);
var outp17 = MAP(BEZIER(S2)([curveMapping22,curveMapping22b]))(domain2);
var outp18= MAP(BEZIER(S2)([curveMapping24,curveMapping24b]))(domain2);

outt3=STRUCT([outp16,outp17,outp18])
//DRAW(outt3)


var outp116 = MAP(BEZIER(S2)([curveMapping30,curveMapping30b]))(domain2);
var outp117 = MAP(BEZIER(S2)([curveMapping32,curveMapping32b]))(domain2);
var outp118= MAP(BEZIER(S2)([curveMapping34,curveMapping34b]))(domain2);

outt4=STRUCT([outp116,outp117,outp118])
//DRAW(outt4)


var outp216 = MAP(BEZIER(S2)([curveMapping30,curveMapping20]))(domain2);
var outp217 = MAP(BEZIER(S2)([curveMapping32,curveMapping22]))(domain2);
var outp218= MAP(BEZIER(S2)([curveMapping34,curveMapping24]))(domain2);

outt5=STRUCT([outp216,outp217,outp218])
//DRAW(outt5)


var outp316 = MAP(BEZIER(S2)([curveMapping30b,curveMapping20b]))(domain2);
var outp317 = MAP(BEZIER(S2)([curveMapping32b,curveMapping22b]))(domain2);
var outp318= MAP(BEZIER(S2)([curveMapping34b,curveMapping24b]))(domain2);
outt6=STRUCT([outp316,outp317,outp318])
//DRAW(outt6)



outt_tot1=STRUCT([outt3,outt4,outt5,outt6])

halfBracc=S([2])([-1])(outt_tot1)
halfBracc=T([2])([1.7+0.46+0.23])(outt_tot1)




//DRAW(outt_tot1)
//DRAW(halfBracc)

var2=(COLOR([235/256,181/256,95/256])(STRUCT([outt_tot1,halfBracc])))


//235 181 95























// cordolo
//(390, 252);
//ctx.bezierCurveTo(396, 204, 315, 193, 285, 213);

var domain = INTERVALS(1)(32);
var controlpoints =   [[3.9,0, -2.52],[3.96,0, -2.04] ,[3.15,0, -1.93],[2.85,0, -2.13]];  // togli il - alle z
var curveMapping124 = BEZIER(S0)(controlpoints);

var curve124 = MAP(curveMapping124)(domain);

//DRAW(curve124)

var domain = INTERVALS(1)(32);
var controlpoints =   [[3.9,-0.23, -2.52],[3.96,-0.23, -2.04] ,[3.15,-0.23, -1.93],[2.85,-0.23, -2.13]];  // togli il - alle z
var curveMapping124b = BEZIER(S0)(controlpoints);

var curve124b = MAP(curveMapping124b)(domain);

//DRAW(curve124b)



var domain = INTERVALS(1)(32);
var controlpoints =   [[3.83,0, -2.52],[3.86,0, -2.04] ,[3.15,0, -2.03],[2.85,0, -2.23]];  // togli il - alle z
var curveMapping34 = BEZIER(S0)(controlpoints);

var curve34 = MAP(curveMapping34)(domain);

//DRAW(curve34)


var domain = INTERVALS(1)(32);
var controlpoints =   [[3.83,-0.23, -2.52],[3.86,-0.23, -2.04] ,[3.15,-0.23, -2.03],[2.85,-0.23, -2.23]];  // togli il - alle z
var curveMapping34b = BEZIER(S0)(controlpoints);

var curve34b = MAP(curveMapping34b)(domain);

//DRAW(curve34b)




//(256, 315);
//ctx.bezierCurveTo(326, 313, 380, 345, 393, 253);

var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,0, -3.20],[3.26,0, -3.13] ,[3.80,0, -3.45],[3.9,0, -2.52]];  // togli il - alle z
var curveMapping26 = BEZIER(S0)(controlpoints);

var curve26 = MAP(curveMapping26)(domain);

//DRAW(curve26)


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,-0.23, -3.20],[3.26,-0.23, -3.13] ,[3.80,-0.23, -3.45],[3.9,-0.23, -2.52]];  // togli il - alle z
var curveMapping26b = BEZIER(S0)(controlpoints);

var curve26b = MAP(curveMapping26b)(domain);

//DRAW(curve26b)


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,0, -3.13],[3.26,0, -3.03] ,[3.70,0, -3.45],[3.83,0, -2.52]];  // togli il - alle z
var curveMapping36 = BEZIER(S0)(controlpoints);

var curve36 = MAP(curveMapping36)(domain);

//DRAW(curve36)

var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,-0.23, -3.13],[3.26,-0.23, -3.03] ,[3.70,-0.23, -3.45],[3.83,-0.23, -2.52]];  // togli il - alle z
var curveMapping36b = BEZIER(S0)(controlpoints);

var curve36b = MAP(curveMapping36b)(domain);

//DRAW(curve36b)






//2.56 -3.15

//(258, 313);
//ctx.bezierCurveTo(219, 310, 184, 315, 88, 317)


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,0, -3.20],[2.18,0, -3.22] ,[1.84,0, -3.20],[0.79,0, -3.22]];  // togli il - alle z
var curveMapping28 = BEZIER(S0)(controlpoints);

var curve28 = MAP(curveMapping28)(domain);

//DRAW(curve28)


var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,-0.23, -3.20],[2.18,-0.23, -3.22] ,[1.84,-0.23, -3.20],[0.79,-0.23, -3.22]];  // togli il - alle z
var curveMapping28b = BEZIER(S0)(controlpoints);

var curve28b = MAP(curveMapping28b)(domain);

//DRAW(curve28b)



var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,0, -3.13],[2.18,0, -3.12] ,[1.84,0, -3.12],[0.79,0, -3.14]];  // togli il - alle z
var curveMapping38 = BEZIER(S0)(controlpoints);

var curve38 = MAP(curveMapping38)(domain);

//DRAW(curve38)

var domain = INTERVALS(1)(32);
var controlpoints =   [[2.56,-0.23, -3.13],[2.18,-0.23, -3.12] ,[1.84,-0.23, -3.12],[0.79,-0.23, -3.14]];  // togli il - alle z
var curveMapping38b = BEZIER(S0)(controlpoints);

var curve38b = MAP(curveMapping38b)(domain);

//DRAW(curve38b)




var outp416 = MAP(BEZIER(S2)([curveMapping124,curveMapping124b]))(domain2);
var outp417 = MAP(BEZIER(S2)([curveMapping26,curveMapping26b]))(domain2);
var outp418= MAP(BEZIER(S2)([curveMapping28,curveMapping28b]))(domain2);

outt7=STRUCT([outp416,outp417,outp418])

//DRAW(outt7)



var outp516 = MAP(BEZIER(S2)([curveMapping34,curveMapping34b]))(domain2);
var outp517 = MAP(BEZIER(S2)([curveMapping36,curveMapping36b]))(domain2);
var outp518= MAP(BEZIER(S2)([curveMapping38,curveMapping38b]))(domain2);

outt8=STRUCT([outp516,outp517,outp518])

//DRAW(outt8)


var outp616 = MAP(BEZIER(S2)([curveMapping124,curveMapping34]))(domain2);
var outp617 = MAP(BEZIER(S2)([curveMapping26,curveMapping36]))(domain2);
var outp618= MAP(BEZIER(S2)([curveMapping28,curveMapping38]))(domain2);

outt9=STRUCT([outp616,outp617,outp618])

//DRAW(outt9)



var outp716 = MAP(BEZIER(S2)([curveMapping124b,curveMapping34b]))(domain2);
var outp717 = MAP(BEZIER(S2)([curveMapping26b,curveMapping36b]))(domain2);
var outp718= MAP(BEZIER(S2)([curveMapping28b,curveMapping38b]))(domain2);

outt10=STRUCT([outp716,outp717,outp718])

//DRAW(outt10)

outt_tot2=STRUCT([outt7,outt8,outt9,outt10])

//DRAW(outt_tot2)

halfCordolo=S([2])([-1])(outt_tot2)
halfCordolo=T([2])([1.7+0.23])(outt_tot2)
//DRAW(halfCordolo)



var3=(COLOR([235/256,181/256,95/256])(STRUCT([outt_tot2,halfCordolo])))






















//(161, 183);
//ctx.bezierCurveTo(180, 176, 171, 319, 130, 317)



var domain = INTERVALS(1)(32);
var controlpoints =   [[1.61,-0.23, -1.83],[1.76,-0.23, -1.76] ,[1.71,-0.23, -3.19],[1.38,-0.23, -3.17]];  // togli il - alle z
var curveMapping50 = BEZIER(S0)(controlpoints);

var curve50 = MAP(curveMapping50)(domain);

//DRAW(curve50)



var domain = INTERVALS(1)(32);
var controlpoints =   [[1.71,-0.23, -1.83],[1.9,-0.23, -1.76] ,[1.86,-0.23, -3.19],[1.5,-0.23, -3.17]];  // togli il - alle z
var curveMapping50b = BEZIER(S0)(controlpoints);

var curve50b = MAP(curveMapping50b)(domain);

//DRAW(curve50b)


var outp8716 = MAP(BEZIER(S2)([curveMapping50b,curveMapping50]))(domain2);
outp8716=S([1,3])([1.8,1.08])(outp8716)
outp8716=T([1,3])([-1.3,0.25])(outp8716)
//DRAW(outp8716)


halfSlice=S([2])([-1])(outp8716)
halfSlice=T([2])([1.7])(halfSlice)
//DRAW(halfSlice)


var4=(COLOR([235/256,181/256,95/256])(STRUCT([halfSlice,outp8716])))





cubo=CUBOID([0.08,1.7+0.46+0.3,0.3])
cubo=T([2,3])([-0.23-0.15,-2])(cubo)
cubo=R([1,3])([-0.6])(cubo)
cubo=T([1,3])([-0.4,-0.25])(cubo)

cubo=(COLOR([235/256,181/256,95/256])(cubo))




DRAW(STRUCT([cubo,var4,var3,var2,outttot]))