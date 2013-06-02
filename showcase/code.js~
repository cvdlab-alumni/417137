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
  glass_color = [185/256,211/256,238/256]; 
  



//scocca joystick


function circlt (sel) {
return function (r) {
return function (d_z) {
return function (p) {
return [ r * COS(sel(p))-1.5, r * SIN(sel(p))+5, d_z ];
};
};
};
};


//es cerchi per bezier
// più verde meno rosso e bezierali
var c1 = circlt(S1)(2)(2);
var cc1 = MAP(c1)(INTERVALS(2*PI)(32));
//cc1=T([1,2])([-1.5,5])(cc1)
//DRAW(cc1);

function circl (sel) {
return function (r) {
return function (d_z) {
return function (p) {
return [ r * COS(sel(p)), r * SIN(sel(p)), d_z ];
};
};
};
};


//es cerchi per bezier
var c = circl(S1)(3.8)(6);
var cc = MAP(c)(INTERVALS(2*PI)(32));
//DRAW(cc);



var domain = PROD1x1([INTERVALS(2*PI)(32),INTERVALS(1)(16)]);

var ou = MAP(BEZIER(S2)([c1,c]))(domain);
//DRAW(ou);


//------------------------------------------------



//parte circolare superiore inferiore
var mode = DISK(3.8)(32);

mode=EXTRUDE([2.6])(mode);
mode=T([3])([6])(mode)
//DRAW(mode)





// cerchio con i tasti
var ctas = circl(S1)(3.8)(8);
var cctas = MAP(c)(INTERVALS(2*PI)(32));
var ous = MAP(BEZIER(S2)([c1,ctas]))(domain);









/*


//disco chiusura in fondo
var model = DISK(1)(32);
model=T([1,2,3])([-1.5,5.3,1])(model)
DRAW(model)

























/*


function circlt3 (sel) {
return function (r) {
return function (d_z) {
return function (p) {
return [ r * COS(sel(p))-1.5, r * SIN(sel(p))+5.3, d_z ];
};
};
};
};


//es cerchi per bezier
// più verde meno rosso e bezierali
var c3 = circlt3(S1)(0.2)(0.5);
var cc3 = MAP(c3)(INTERVALS(2*PI)(32));
//cc1=T([1,2])([-1.5,5])(cc1)
DRAW(cc3);


var domain = PROD1x1([INTERVALS(2*PI)(32),INTERVALS(1)(16)]);

var out = MAP(BEZIER(S2)([c3,c2]))(domain);
DRAW(out);

*/






//-------------------------------------------semisfera in fondo smussata
var domain9=DOMAIN([[0,PI],[0,PI]])([24,36])
var mapping=function(v){
var a=v[0];
var b=v[1];
var u=2*SIN(a)*COS(b);
var v=2*0.3*SIN(a)*SIN(b);
var w=2*COS(a);
	return [u,v,w];
}
var modell=MAP(mapping)(domain9)


modell=R([2,3])([3*PI/2])(modell)
//model=T([1,2,3])([-1.5,5.3,1])(model)
//DRAW(model)




modell=T([1,2,3])([-1.5,5,2])(modell)
//DRAW(modell)
//-1.5,5,2   2



var imp=STRUCT([ou,mode,modell,ous])
imp=COLOR(black)(imp)

//tasti posteriori r1,r2,l1,l2






///qui parte parte posteriore che contiene r1 r2 e l1 e l2










//con z negative






//curve laterali
var dom1D = INTERVALS(1)(32);
var dom2D = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);

var Su0 = BEZIER(S1)([[5.9,0,0],[6.9,0,-19.6]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);


var Su1 = BEZIER(S1)([[0,0,-1.2],[-2.3,0,-0.8],[1.9,0,-22.3],[4.5,0,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[5.9,0,0],[3.9,0,-0.4],[1.8,0,-0.3],[0,0,-1.2]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[6.9,0,-19.6],[6.2,0,-21.4],[5.3,0,-22.8],[4.5,0,-24.4]];

var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out);

//------------------------------------------------------------------------------------------------

var dom1D = INTERVALS(1)(32);
var dom2D = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);

var Su0 = BEZIER(S1)([[5.9,16,0],[6.9,16,-19.6]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);


var Su1 = BEZIER(S1)([[0,16,-1.2],[-2.3,16,-0.8],[1.9,16,-22.3],[4.5,16,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[5.9,16,0],[3.9,16,-0.4],[1.8,16,-0.3],[0,16,-1.2]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[6.9,16,-19.6],[6.2,16,-21.4],[5.3,16,-22.8],[4.5,16,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out1 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out1);


//-----------------------------------------------------------------
//parte posteriore

var Su0 = BEZIER(S1)([[5.9,0,0],[6.9,0,-19.6]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[5.9,16,0],[6.9,16,-19.6]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[5.9,0,0],[5.9,16,0]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[6.9,0,-19.6],[6.9,16,-19.6]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out2 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out2);


//parte anteriore


var dom1D = INTERVALS(1)(32);
var dom2D = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);




var Su0 = BEZIER(S1)([[0,0,-1.2],[-4,8,-1.4],[0,16,-1.2]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[4.5,0,-24.4],[0.5,8,-24.4],[4.5,16,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);


var control2 = [[0,0,-1.2],[-2.3,0,-0.8],[1.9,0,-22.3],[4.5,0,-24.4]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[0,16,-1.2],[-2.3,16,-0.8],[1.9,16,-22.3],[4.5,16,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out3 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out3);


//parte superiore

var Su0 = BEZIER(S1)([[0,0,-1.2],[-4,8,-1.4],[0,16,-1.2]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[5.9,0,0],[5.9,16,0]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[0,0,-1.2],[1.8,0,-0.3],[3.9,0,-0.4],[5.9,0,0]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[0,16,-1.2],[1.8,16,-0.3],[3.9,16,-0.4],[5.9,16,0]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out4 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out4);


//parte inferiore
var Su0 = BEZIER(S1)([[4.5,0,-24.4],[0.5,8,-24.4],[4.5,16,-24.4]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[6.9,0,-19.6],[6.9,16,-19.6]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[4.5,0,-24.4],[5.3,0,-22.8],[6.2,0,-21.4],[6.9,0,-19.6]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[4.5,16,-24.4],[5.3,16,-22.8],[6.2,16,-21.4],[6.9,16,-19.6]]
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out5 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out5);




//tasto r2

var r=STRUCT([out,out1,out2,out3,out4,out5])





























//-----------------------------------
//tasto r1 vuoto


var dom1D = INTERVALS(1)(32);
var dom2D = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);



//faccia anteriore
var Su0 = BEZIER(S1)([[0,0,-1.2],[-4,8,-1.4],[0,16,-1.2]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[4.5,0,-24.4],[0.5,8,-24.4],[4.5,16,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);


var control2 = [[0,0,-1.2],[-2.3,0,-0.8],[1.9,0,-22.3],[4.5,0,-24.4]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[0,16,-1.2],[-2.3,16,-0.8],[1.9,16,-22.3],[4.5,16,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out3 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out3);




//faccia posteriore
var Su0 = BEZIER(S1)([[4,0,-1.2],[0,8,-1.4],[4,16,-1.2]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[8.5,0,-24.4],[4.5,8,-24.4],[8.5,16,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);


var control2 = [[4,0,-1.2],[1.7,0,-0.8],[5.9,0,-22.3],[8.5,0,-24.4]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[4,16,-1.2],[2.3,16,-0.8],[5.9,16,-22.3],[8.5,16,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out31 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out31);


//faccia superiore

var Su0 = BEZIER(S1)([[0,0,-1.2],[-4,8,-1.4],[0,16,-1.2]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[4,0,-1.2],[0,8,-1.4],[4,16,-1.2]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[0,0,-1.2], [4,0,-1.2]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[0,16,-1.2], [4,16,-1.2]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out311 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out311);


//pareti laterali

var Su0 = BEZIER(S1)([[0,0,-1.2], [4,0,-1.2]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[4.5,0,-24.4],[8.5,0,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[0,0,-1.2],[-2.3,0,-0.8],[1.9,0,-22.3],[4.5,0,-24.4]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[4,0,-1.2],[2.3,0,-0.8],[5.9,0,-22.3],[8.5,0,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out3111 = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out3111);

















var Su0 = BEZIER(S1)([[0,16,-1.2],[-2.3,16,-0.8],[1.9,16,-22.3],[4.5,16,-24.4]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[4,16,-1.2],[2.3,16,-0.8],[5.9,16,-22.3],[8.5,16,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[0,16,-1.2],[4,16,-1.2]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[4.5,16,-24.4],[8.5,16,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out3111d = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out3111d);








//parte sotto
var Su0 = BEZIER(S1)([[4.5,16,-24.4],[8.5,16,-24.4]]);
var curve0 = MAP(Su0)(dom1D);
//DRAW(curve0);

var Su1 = BEZIER(S1)([[4.5,0,-24.4],[8.5,0,-24.4]]);
var curve1 = MAP(Su1)(dom1D);
//DRAW(curve1);

var control2 = [[4.5,16,-24.4],[0.5,8,-24.4],[4.5,0,-24.4]];
var Sv0 = BEZIER(S2)(control2);
var curve2 = MAP(BEZIER(S0)(control2))(dom1D);
//DRAW(curve2);

var control3 = [[8.5,16,-24.4],[4.5,8,-24.4],[8.5,0,-24.4]];
var Sv1 = BEZIER(S2)(control3);
var curve3 = MAP( BEZIER(S0)(control3))(dom1D);
//DRAW(curve3);

var out3111ds = MAP(COONS_PATCH([Su0,Su1,Sv0,Sv1]))(dom2D);
//DRAW(out3111ds);

var r1=STRUCT([out3,out31,out311,out3111,out3111d,out3111ds])

var r1=S([3])([0.5])(r1)
var r1=T([1,2,3])([0,0,10])(r1)


var r1=S([1,2,3])([0.8,0.8,0.6])(r1)
var r1=T([1,2,3])([-3,1.5,-10])(r1)

//DRAW(r1)



//inserisco tasti
//-----------------------------------------------------------------------
var r2=S([1,2,3])([0.8,0.8,0.4])(r)

var r2=T([1,2,3])([-1,1.5,-12])(r2)
//DRAW(r2)

r=COLOR(black)(r)
tastPost=STRUCT([r,r1,r2])
tastPost=S([1,2,3])([0.2,0.2,0.2])(tastPost)
tastPost=R([1,2])([PI/2])(tastPost)
tastPost=T([1,2,3])([1.6,-4,8.5])(tastPost)
tastPost=S([3])([0.9])(tastPost)
tastPost=T([1,2,3])([0,0,0.88])(tastPost)








//parte centrale scocca
//3.8r 2.6z


cube=CUBOID([8.8,4.5,2.5])
cube=T([1,2,3])([2.9,-2.5,6])(cube)
cube=COLOR(black)(cube)




//tasti cerchio,triangolo ...

//tasti cerchio,triangolo,quadrato,x
var tastCirc = DISK(1)(32);
tastCirc=EXTRUDE([0.3])(tastCirc);

//DRAW(tastCirc);
//da fare i segni sopra: x, cerchio ecc...








//-------------------------CERCHIO----red
var r = 0.75;
var divs = 32;
var circlered = CIRCLE(r)(divs);
circlered=T([3])([0.3])(circlered)
circlered=COLOR(red)(circlered)
//DRAW(circlered);

var cerchio=STRUCT([tastCirc,circlered])
cerchio=T([1])([2])(cerchio);


//------------------triangolo-----verde


var points = [[0,0.8,0.3], [-0.6,-0.5,0.3], [0.6,-0.5,0.3],[0,0.8,0.3]];
var polyline = POLYLINE(points);
polyline=COLOR(green)(polyline)

var triangolo=STRUCT([tastCirc,polyline])
triangolo=T([2])([2])(triangolo);



//x blù

var points2 = [[0.6,-0.6,0.3], [-0.6,0.6,0.3]];
var points3 = [[-0.6,-0.6,0.3], [0.6,0.6,0.3]];

var polyline2 = POLYLINE(points2);
polyline2=COLOR(blue)(polyline2);

var polyline3 = POLYLINE(points3);
polyline3=COLOR(blue)(polyline3);


var xx=STRUCT([tastCirc,polyline3,polyline2])
xx=T([2])([-2])(xx);



//quadrato  rosa


var points4 = [[0.6,-0.6,0.3],[-0.6,-0.6,0.3], [-0.6,0.6,0.3],, [0.6,0.6,0.3],[0.6,-0.6,0.3]];


var polyline4 = POLYLINE(points4);
polyline4=COLOR(redd)(polyline4);


var quadrato=STRUCT([tastCirc,polyline4])
quadrato=T([1])([-2])(quadrato);


var tasC=STRUCT([xx,triangolo,cerchio,quadrato])

tasC=T([1,2,3])([0,0,8.6])(tasC);
tasC=R([1,2])([PI])(tasC);



//tasti centrali

//analog e select
var analog=CUBOID([2,1,0.3])
var select=T([1,2])([-3,3])(analog)

//start
var points=[[0,0],[0,1],[2,0.5],[0,0]];       // freccetta
//po=POLYLINE(po);
var cells=[[0,1,2,3]];
var start = SIMPLICIAL_COMPLEX(points)(cells);
start=EXTRUDE([0.3])(start);
start=T([1,2])([3,3])(start)




tastCentr=STRUCT([analog,select,start])
tastCentr=S([1,2,3])([0.7,0.7,0.7])(tastCentr)
tastCentr=R([1,2])([PI])(tastCentr)
tastCentr=T([1,2,3])([7.5,1.4,8.5])(tastCentr)




//fine tasti centrali
//--------------------------------------------------------------------------


//analogico
//----------------------------------------------------------------------------
// levette analogico
function annulus_sector (alpha, r, R) {
  var domain = DOMAIN([[0,alpha],[r,R]])([36,1]);
  var mapping = function (v) {
    var a = v[0];
    var r = v[1];
    
    return [r*COS(a), r*SIN(a)];
  }
  var model = MAP(mapping)(domain);
  return model;
}


//cilindro cavo

//DRAW((EXTRUDE([1.7])(annulus_sector(2*PI, 0.8, 1))));//1.7-->2
CYLC=((EXTRUDE([1.7])(annulus_sector(2*PI, 0.8, 1))));//1.7-->2
CYLC=COLOR(black)(CYLC)

var modelj = DISK(1)([32,10]);

modelj=EXTRUDE([1.3])(modelj) //-------------------------------
modelj=T([3])([-0.1])(modelj)  //-------------------------------

modelj=COLOR(black)(modelj)
//DRAW(model);


//cilindretto

//DRAW(CYL_SURFACE([0.45,2.3])([36]))//togli 0.3
cyl=(CYL_SURFACE([0.45,2.3])([36]))//togli 0.3

//sferetta interna
var domain9=DOMAIN([[0,PI],[0,2*PI]])([24,36])
var mapping3=function(v){
var a=v[0];
var b=v[1];
var u=0.98*SIN(a)*COS(b);
var v=0.98*SIN(a)*SIN(b);
var w=0.98*COS(a);
	return [u,v,w];
}
var sph=MAP(mapping3)(domain9)
sph=T([3])([0.95])(sph)//-0.3
//DRAW(sph);


//funghetto analogico

function circl (sel) {
return function (r) {
return function (d_z) {
return function (p) {
return [ r * COS(sel(p)), r * SIN(sel(p)), d_z ];
};
};
};
};
//es cerchi per bezier
var c1 = circl(S0)(4.5)(2);
var cc1 = MAP(c1)(INTERVALS(2*PI)(32));
//DRAW(cc1);

var c2 = circl(S0)(3.5)(3.8);
var cc2 = MAP(c2)(INTERVALS(2*PI)(32));
//DRAW(cc2);

var c3 = circl(S0)(2)(3.6);
var cc3 = MAP(c3)(INTERVALS(2*PI)(32));
//DRAW(cc3);

var domain5 = PROD1x1([INTERVALS(2*PI)(32),INTERVALS(1)(16)]);
var c4 = BEZIER(S0)([[0,0,3.65]]);

var base= MAP(BEZIER(S2)([c1,BEZIER(S0)([[0,0,2]])]))(domain5);
var out = MAP(BEZIER(S2)([c1,c2,c3,c4]))(domain5);
var analogic=STRUCT([out,base])
analogic=T([3])([9])(analogic)
analogic=S([1,2,3])([0.2,0.2,0.2])(analogic)



an=STRUCT([analogic,modelj,cyl,sph,CYLC])
an=T([1,2,3])([3.5,1.8,3.8])(an)
an=S([1,2,3])([1.2,1.2,1.6])(an)

//DRAW(an);


//parte sx specchiata

var partsx=STRUCT([imp,tastPost,an])
partsx=T([1])([-13.5])(partsx)
partsx=S([1])([-1])(partsx)


// freccette
//arrow

var po=[[0,0],[1.2,0],[1.2,1.2],[0.6,1.7],[0,1.2],[0,0]];       // freccetta
//po=POLYLINE(po);
var cells=[[0,1,2,3,4,5]];
var freccetta = SIMPLICIAL_COMPLEX(po)(cells);
freccetta=EXTRUDE([0.3])(freccetta);

var c2r=R([1,2])([PI/2])(freccetta)
var c2r=T([1,2])([2.6,1.6])(c2r)
arrows=STRUCT([freccetta,c2r])

var arrows2=S([1,2])([-1,-1])(arrows)
//DRAW(arrows)

var arrows2=T([1,2])([1.2,4.4])(arrows2)
//DRAW(arrows2)
arrowsTot=STRUCT([arrows,arrows2])
//DRAW(arrowsTot)


arrowsTot=T([1,2,3])([13,-2.3,8.5])(arrowsTot)


//fine frecce direzionali
//------------------------------------------------------------------





var model=STRUCT([imp,tastPost,cube,tasC,tastCentr,an,partsx,arrowsTot])

