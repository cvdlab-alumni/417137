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





cyl=CYL_SURFACE([0.1,3.13])([64,8])  //////////////////////////5.5--------------------->3.5
//cyl=R([1,3])([PI/2])(cyl)
cyl=T([1,3])([0.9,0])(cyl)
//DRAW(cyl)




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




cyl2=CYL_SURFACE([0.1,1.5])([64,8])  //////////////////////////5.5--------------------->3.5
cyl2=R([1,3])([PI/2])(cyl2)
cyl2=T([1,3])([-1.5,-0.9])(cyl2)
//DRAW(cyl2)





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
tubo2=T([1])([-1.5])(tubo2)

//DRAW(tubo2)



cyl3=CYL_SURFACE([0.1,3.4])([64,8])  //////////////////////////5.5--------------------->3.5
//cyl=R([1,3])([PI/2])(cyl)
cyl3=T([1,3])([-2.4,0])(cyl3)
//DRAW(cyl3)




domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[-1,0,0],[0,0,1],[0,0,2],[3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[-0.8,0,0],[0,0,0.8],[0,0,1.8],[2.6,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo3=STRUCT([out,out2])
tubo3=T([1,3])([-1.5,3.4])(tubo3)
//DRAW(tubo3)





cyl4=CYL_SURFACE([0.1,7.6])([64,8])  //////////////////////////5.5--------------------->3.5
cyl4=R([1,3])([PI/2])(cyl4)
cyl4=T([1,3])([-1.5,4.3])(cyl4)
//DRAW(cyl4)



domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[1,0,0],[0,0,1],[0,0,2],[-3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[0.8,0,0],[0,0,0.8],[0,0,1.8],[-2.6,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,-0.4,0],[0,0.4,0]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0.4,0],[0,-0.4,0]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo4=STRUCT([out,out2])
tubo4=T([1,3])([6.1,3.4])(tubo4)

//DRAW(tubo4)





cyl5=CYL_SURFACE([0.1,3.4])([64,8])  //////////////////////////5.5--------------------->3.5
//cyl=R([1,3])([PI/2])(cyl)
cyl5=T([1,3])([7,0])(cyl5)
//DRAW(cyl5)




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
tubo5=STRUCT([out,out2])
tubo5=T([1])([7.9])(tubo5)

//DRAW(tubo5)




cyl6=CYL_SURFACE([0.1,1.5])([64,8])  //////////////////////////5.5--------------------->3.5
cyl6=R([1,3])([PI/2])(cyl6)
cyl6=T([1,3])([7.9,-0.9])(cyl6)
//DRAW(cyl6)



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
tubo6=STRUCT([out,out2])
tubo6=T([1])([9.4])(tubo6)
//DRAW(tubo6)






cyl7=CYL_SURFACE([0.1,2.5])([64,8])  //////////////////////////5.5--------------------->3.5
//cyl=R([1,3])([PI/2])(cyl)
cyl7=T([1,3])([10.3,0])(cyl7)
//DRAW(cyl7)




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
tubo7=STRUCT([out,out2])
tubo7=T([1,2,3])([10.3,0.9,2.5])(tubo7)

//DRAW(tubo7)




cyl8=CYL_SURFACE([0.1,1])([64,8])  //////////////////////////5.5--------------------->3.5
cyl8=R([2,3])([PI/2])(cyl8)
cyl8=T([1,2,3])([10.3,1.8,3.4])(cyl8)
//DRAW(cyl8)




half=STRUCT([cyl,tubo2,cyl2,tubo3,cyl3,tubo4,cyl4,tubo5,cyl5,tubo6,cyl6,tubo7,cyl7,tubo,cyl8])


half=T([2])([-1.8])(half)

half2=S([2])([-1])(half)

tot=(STRUCT([half,half2]))

tot=T([2])([1.8])(tot)


cassetto=(CUBOID([3.2,3.6,1]))
cassetto=T([1])([-2.375])(cassetto)
cassetto=COLOR([0.1,0.1,0.1])(cassetto)
//DRAW(cassetto)
maniglia=(CUBOID([0.8,0.2,0.15]))
maniglia=T([1,2,3])([-1.19,-0.2,0.5])(maniglia)
//DRAW(maniglia)

cassetto2=(CUBOID([3.2,3.6,1]))
cassetto2=T([1,3])([-2.375,1.02])(cassetto2)
cassetto2=COLOR([0.1,0.1,0.1])(cassetto2)
maniglia2=(CUBOID([0.8,0.2,0.15]))
maniglia2=T([1,2,3])([-1.19,-0.2,1.5])(maniglia2)
//DRAW(maniglia2)
//DRAW(cassetto2)

cassetto3=(CUBOID([3.2,3.6,1]))
cassetto3=T([1,3])([-2.375,2.04])(cassetto3)
cassetto3=COLOR([0.1,0.1,0.1])(cassetto3)
maniglia3=(CUBOID([0.8,0.2,0.15]))
maniglia3=T([1,2,3])([-1.19,-0.2,2.5])(maniglia3)
//DRAW(maniglia3)
//DRAW(cassetto3)



cassetto2a=(CUBOID([3.2,3.6,0.9]))
cassetto2a=T([1,3])([7,1.1])(cassetto2a)
cassetto2a=COLOR([0.1,0.1,0.1])(cassetto2a)
maniglia4=(CUBOID([0.8,0.2,0.15]))
maniglia4=T([1,2,3])([8.3,-0.2,2.4])(maniglia4)
//DRAW(maniglia4)
//DRAW(cassetto2a)

cassetto2a2=(CUBOID([3.2,3.6,0.9]))
cassetto2a2=T([1,3])([7,2.02])(cassetto2a2)
cassetto2a2=COLOR([0.1,0.1,0.1])(cassetto2a2)
maniglia5=(CUBOID([0.8,0.2,0.15]))
maniglia5=T([1,2,3])([8.3,-0.2,1.5])(maniglia5)
//DRAW(maniglia5)
//DRAW(cassetto2a2)


tavola=(CUBOID([8.3,3.6,0.1]))
tavola=T([1,3])([-1.9,4.3])(tavola)
tavola=COLOR([0.1,0.1,0.1])(tavola)
//DRAW(tavola)



disks = DISK(0.1)([64,4]);
//disks2=R([1,3])([-PI/2])(disks)
disks2=T([1,3])([0.9,3.13])(disks)

disks3=T([2])([3.6])(disks2)


DRAW(STRUCT([tot,cassetto,maniglia,cassetto2,maniglia2,cassetto3,maniglia3,cassetto2a,maniglia4,cassetto2a2,maniglia5,tavola,disks2,disks3]))
