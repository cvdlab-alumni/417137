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


//tubo curvo
domain= PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)]);

var c1 = CUBIC_HERMITE(S1)([[1,0,0],[0,1,0],[0,2,0],[-3,0,0]]);
//DRAW(MAP(c1)(INTERVALS(1)(14)));

var c2 = CUBIC_HERMITE(S1)([[0.75,0,0],[0,0.75,0],[0,1.75,0],[-2.5,0,0]]);
//DRAW(MAP(c2)(INTERVALS(1)(14)));

var sur3 = CUBIC_HERMITE(S2)([c1,c2,[0,0,0.5],[0,0,-0.5]]);
var out = MAP(sur3)(domain); //mezzo tubo
//DRAW(out);

var sur31 = CUBIC_HERMITE(S2)([c1,c2,[0,0,-0.5],[0,0,0.5]]);
var out2 = MAP(sur31)(domain); //mezzo tubo
tubo=STRUCT([out,out2])
//DRAW(tubo)





//cilindro dritto
cyl=CYL_SURFACE([0.125,5.5])([64,8])  //////////////////////////5.5--------------------->3.5
cyl=R([2,3])([PI/2])(cyl)
cyl=T([1])([0.875])(cyl)
//DRAW(cyl);

//tubo curvo2
tub2=R([1,2])([3*PI/2])(tubo)
tub2=T([2])([-5.5])(tub2)
//DRAW(tub2)
tuboRicurvo=STRUCT([tubo,cyl,tub2])

tuboRicurvo=T([1])([1.75])(tuboRicurvo)///////////////////////
//DRAW(tuboRicurvo);

tuboide=STRUCT([tubo,cyl])
tuboide=T([1])([2.5])(tuboide)
tub2=R([1,2])([3*PI/2])(tubo)
//tub2=T([1,2])([2.5,-3.5])(tub2)
tub2=R([1,3])([3*PI/2])(tub2)
tub2=T([1,2,3])([3.375,-5.5,-0.875])(tub2)////////////----------------->-5.5--------------------->-3.5


tub2cur=STRUCT([tuboide,tub2])
tub2cur=R([2,3])([3*PI/2])(tub2cur)

tub2cur=T([1,2,3])([0.75,0.75,0.75])(tub2cur)    //traslo di più


//DRAW(tub2cur)



cyl=CYL_SURFACE([0.125,3.25])([64,8])   //tubo più lungo
cyl=R([1,3])([PI/2])(cyl)
cyl=T([2,3])([0.75,-0.125])(cyl)
//DRAW(cyl)

///ribalto
rib=STRUCT([tub2cur,cyl])

rib=S([1])([-1])(rib)
//DRAW(rib);

mezz=STRUCT([cyl,rib])

//mezz=T([2])([1.75])(mezz)/////////////////////////////////////////////////


//DRAW(mezz)


//rib
rib2=STRUCT([mezz,tub2cur])
rib2=T([2])([1.75])(rib2)

//DRAW(rib2)





//tubo curvo alto vicino bracciolo

cyl=tubo
cyl=R([1,3])([3*PI/2])(cyl)
cyl=R([1,2])([2*PI/2])(cyl)
cyl=T([1,2,3])([-4.125,1.75,6.25])(cyl)/////////////////////////7---->5

cyl2=T([1])([8.25])(cyl)

cyls=STRUCT([cyl,cyl2])
//DRAW(cyls);  //commento tubo dritto in alto prima del bracciolo


//mezz=STRUCT([cyls,rib2])  //////////////////////
//mezz=S([2])([-1])(mezz)
//DRAW(mezz);





//cilindro più corto dietro
cyl4=CYL_SURFACE([0.125,0.3])([64,8])
cyl4=T([1,2,3])([-4.125,0.875,6.2])(cyl4)/////////////////////////7---->5


//cilindro più lungo anteriore
cyl5=CYL_SURFACE([0.125,0.8])([64,8])
cyl5=T([1,2,3])([4.125,0.875,5.5])(cyl5)/////////////////////////7---->5







v2=T([3])([-1.5])(cyl)
v2=R([1,2])([2*PI/2])(v2)
v2=R([1,3])([PI])(v2)


v3=T([1])([8.25])(v2)
//cyl=R([1,2])([2*PI/2])()


v3=T([2,3])([2,10.25])(v3)
v2=T([2,3])([2,11])(v2)


vs=STRUCT([v2,v3])
vs=T([2])([-0.25])(vs)


model1=STRUCT([rib2,cyls,cyl5,cyl4,vs]);


tube=CYL_SURFACE([0.125,2.15])([64,8])   //1.4



tubo2=R([2,3])([PI/2])(tube)
tubo2=T([1,2,3])([-4.125,0,5.375])(tubo2)


tubo3=R([2,3])([PI/2])(tube)

tubo3=T([1,2,3])([4.125,0,4.625])(tubo3)




model=STRUCT([model1,tubo2,tubo3])
model=T([2])([2.15])(model)  //1.4

mirrorModel=S([2])([-1])(model)


xtub=CYL_SURFACE([0.125,8.5])([64,8])   
xtub=R([1,3])([PI/2])(xtub)
xtub=T([1,2,3])([-4.25,4.415,6.2])(xtub) 

xtub2=T([2])([-8.825])(xtub) 


modelF=STRUCT([model,xtub2,xtub,mirrorModel])

//DRAW(modelF)

////////////////////////////////////////////////////////////////////////////////////////////
tubSchienale=CYL_SURFACE([0.125,6])([64,8])
//tubSchienale=R([2,3])([PI/2])(tubSchienale)
//tubSchienale=T([2])([4.25])(tubSchienale)


//DRAW(tubSchienale)

tubCurvSchienale=R([2,3])([PI])(tubo)
tubCurvSchienale=R([1,3])([PI/2])(tubCurvSchienale)


//DRAW(tubCurvSchienale)


xtub=CYL_SURFACE([0.125,8.5])([64,8])   
xtub=R([1,3])([PI/2])(xtub)
xtub=T([1,2,3])([-4.25,4.415,5.625])(xtub) 

//tubo vertical
tubSchienale8=T([2])([-0.875])(tubSchienale)
//DRAW(tubSchienale8)


//tubo orizz
tubSchienale7=CYL_SURFACE([0.125,0.65])([64,8])
tubSchienale7=R([2,3])([PI/2])(tubSchienale7)
tubSchienale7=T([2,3])([0.65,-0.875])(tubSchienale7)
//DRAW(tubSchienale7)


//tubb curvo 2 schien
tubbbb=R([1,2])([PI])(tubo)
//DRAW(tubbbb)



xtub3=CYL_SURFACE([0.125,6.5])([64,8])     //lunghezza stecca sedia 
xtub3=R([1,3])([PI/2])(xtub3)
xtub3=T([1,2,3])([0,-0.875,0])(xtub3) 

//DRAW(xtub3)





tubSchienale5=CYL_SURFACE([0.125,4.5])([64,8])
tubSchienale5=R([2,3])([PI/2])(tubSchienale5)
tubSchienale5=T([1,2,3])([-0.875,4.4,0])(tubSchienale5) 
//DRAW(tubSchienale5)



sed=STRUCT([tubbbb,xtub3,tubSchienale5])
//DRAW(sed)
sed=T([2])([-0.375])(sed) 


schi=STRUCT([tubCurvSchienale,tubSchienale7,tubSchienale8])
schi=T([2,3])([-1.75,0.625])(schi)           //1.75    0.3
//DRAW(schi)

tot=STRUCT([schi,sed])
tot=T([1,2,3,])([-0.88,-2,3.7])(tot)                     //verde 0.3                                 blu ok + 4 

tot=R([1,3])([-0.3])(tot)




//DRAW(tot)


tot2=S([2])([-1])(tot)
tott=STRUCT([tot,tot2,modelF])
//DRAW(tott)








































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



//DRAW(T([3])([-0.6])(EXTRUDE([1.2])(annulus_sector(2*PI, 0.92, 1))));



cubo=CUBOID([8.2,0.05,1])
cubo=T([1,2,3])([-4.1,-3,5.75])(cubo)
//DRAW(cubo)



cubo2=CUBOID([8.2,0.75,0.05])
cubo2=T([1,2,3])([-4.1,-4.2,7.15])(cubo2)
//DRAW(cubo2)



cubo3=CUBOID([5.4,6.5,0.05])
cubo3=T([1,2,3])([-0.3,-3.25,3.7])(cubo3)
cubo3=R([1,3])([-0.3])(cubo3)

//DRAW(cubo3)


cubo4=CUBOID([0.05,9.22,2])
cubo4=T([1,2,3])([-0.95,-4.6,8.13])(cubo4)
cubo4=R([1,3])([-0.3])(cubo4)

//DRAW(cubo4)




cubo5=CUBOID([0.05,9.22,1.8])
cubo5=T([1,2,3])([-0.95,-4.6,4.1])(cubo5)
cubo5=R([1,3])([-0.3])(cubo5)

//DRAW(cubo5)


cubo6=S([2])([-1])(cubo)
cubo7=S([2])([-1])(cubo2)


cuboidi=STRUCT([cubo,cubo2,cubo3,cubo4,cubo5,cubo6,cubo7])
cuboidi=COLOR([0.1,0.1,0.1])(cuboidi)












disks = DISK(0.125)([64,4]);
disks2=R([1,3])([-PI/2])(disks)
disks2=T([1,2,3])([-4.25,4.41,6.2])(disks2)

disks3=S([1])([-1])(disks2)

disks4=S([2])([-1])(disks2)

disks5=S([2])([-1])(disks3)

disks6=T([1,2,3])([-4.375,4.51,10.2])(disks)
disks6=R([1,3])([-0.3])(disks6)
disks6=T([1,2,3])([3.3,0.115,1.15])(disks6)
disks7=S([2])([-1])(disks6)

disks8=R([1,3])([-0.3])(disks2)
disks8=T([1,2,3])([10.17,-1.16,0.53])(disks8)
disks9=S([2])([-1])(disks8)

DRAW(STRUCT([cuboidi,tott,disks2,disks3,disks4,disks5,disks6,disks7,disks8,disks9]))
