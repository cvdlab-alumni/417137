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



domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[1,0,0],[0,0,-1],[0,0,-2],[-3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[0.8,0,0],[0,0,-0.8],[0,0,-1.8],[-2.6,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo=STRUCT([out,out2])

//DRAW(tubo)



cyl=CYL_SURFACE([0.1,4])([64,8])
cyl=R([1,3])([PI/2])(cyl)
cyl=T([1,3])([-4,-0.9])(cyl)
//DRAW(cyl)



domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[-1,0,0],[0,0,-1],[0,0,-2],[3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[-0.8,0,0],[0,0,-0.8],[0,0,-1.8],[2.6,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo2=STRUCT([out,out2])

tubo2=T([1,3])([-4,-0])(tubo2)
//DRAW(tubo2)





cyl2=CYL_SURFACE([0.1,5.5])([64,8]) 
//cyl=R([1,3])([PI/2])(cyl)
cyl2=T([1,3])([0.9,-0])(cyl2)
//DRAW(cyl2)




domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[0,-1,0],[0,0,1],[0,0,2],[0,3,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[0,-0.8,0],[0,0,0.8],[0,0,1.8],[0,2.6,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[-0.4,0,0],[0.4,0,0]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0.4,0,0],[-0.4,0,0]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo3=STRUCT([out,out2])

tubo3=T([1,2,3])([0.9,0.9,5.5])(tubo3)
//DRAW(tubo3)



cyl3=CYL_SURFACE([0.1,2])([64,8])  
cyl3=R([2,3])([PI/2])(cyl3)
cyl3=T([1,2,3])([0.9,2.9,6.4])(cyl3)
//DRAW(cyl3)




cyl4=CYL_SURFACE([0.1,5.5])([64,8])  
//cyl=R([1,3])([PI/2])(cyl)
cyl4=T([1,3])([-4.9,-0])(cyl4)
//DRAW(cyl4)





domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[0,-1,0],[0,0,1],[0,0,2],[0,3,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[0,-0.8,0],[0,0,0.8],[0,0,1.8],[0,2.6,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[-0.4,0,0],[0.4,0,0]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0.4,0,0],[-0.4,0,0]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo4=STRUCT([out,out2])

tubo4=T([1,2,3])([-4.9,0.9,5.5])(tubo4)
//DRAW(tubo4)



cyl5=CYL_SURFACE([0.1,2])([64,8]) 
cyl5=R([2,3])([PI/2])(cyl5)
cyl5=T([1,2,3])([-4.9,2.9,6.4])(cyl5)
//DRAW(cyl5)




half=STRUCT([cyl,cyl2,cyl3,cyl4,cyl5,tubo,tubo2,tubo3,tubo4])
half=T([1,2])([0.4,-2.9])(half)

half2=S([2])([-1])(half)










domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[1,0,0],[0,1,0],[0,2,0],[-3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[0.8,0,0],[0,0.8,0],[0,1.8,0],[-2.6,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,0,0.4],[0,0,-0.4]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0,-0.4],[0,0,0.4]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo20=STRUCT([out,out2])

tubo20=T([1,2,3])([1.4,1.8,5.2])(tubo20)
//DRAW(tubo20)




cyl20=CYL_SURFACE([0.1,6])([64,8])  
cyl20=R([1,3])([PI/2])(cyl20)
cyl20=T([1,2,3])([-4.6,2.7,5.2])(cyl20)
//DRAW(cyl20)







cyl21=CYL_SURFACE([0.1,1.8])([64,8])  
cyl21=R([2,3])([PI/2])(cyl21)
cyl21=T([1,2,3])([2.3,1.8,5.2])(cyl21)
//DRAW(cyl21)


cyl22=CYL_SURFACE([0.1,1.8])([64,8]) 
cyl22=R([2,3])([PI/2])(cyl22)
cyl22=T([1,2,3])([-5.5,1.8,5.2])(cyl22)
//DRAW(cyl22)







domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[-1,0,0],[0,1,0],[0,2,0],[3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[-0.8,0,0],[0,0.8,0],[0,1.8,0],[2.6,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,0,0.4],[0,0,-0.4]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0,-0.4],[0,0,0.4]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo21=STRUCT([out,out2])

tubo21=T([1,2,3])([-4.6,1.8,5.2])(tubo21)
//DRAW(tubo21)




half22=STRUCT([tubo20,tubo21,cyl20,cyl21,cyl22]);

half23=S([2])([-1])(half22);









var model1 = DISK(4.6)([64,4]);

var model2=T([3])([0.2])(model1)


var c = circl(S1)(4.6)(0);
//var cc = MAP(c)(INTERVALS(2*PI)(32));

var c2 = circl(S1)(4.6)(0.2);
//var cc2 = MAP(c2)(INTERVALS(2*PI)(32));

var domain = PROD1x1([INTERVALS(2*PI)(32),INTERVALS(1)(1)]);
var ou = MAP(BEZIER(S2)([c2,c]))(domain);

glass=STRUCT([model1,model2,ou])
glass=COLOR(glass_color)(glass)

glass=T([1,2,3])([-1.5,0.1,6.5])(glass)



model=STRUCT([half,half2,half22,half23,glass])
DRAW(model)