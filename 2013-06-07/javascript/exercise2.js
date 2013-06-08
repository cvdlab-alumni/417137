//es 1

var dominio = DOMAIN([[-15, 15], [-15, 15]])([20,20]);

var terrain = function(punto){
	var x = punto[0];
	var y = punto[1];
	var z =  1;
	
	if (y==15 || y==-15)
		return [x,y,0]

	if (x==15 || x==-15)
		return [x,y,0]

	return [x, y, Math.random()*z*2];
}

brown  = [90/255,50/255,20/255]; 

brown2  = [50/255,10/255,10/255]; 

var DTM = MAP(terrain)(dominio);

pianura=(COLOR(brown)(CUBOID([30,13]))) //terreno pianeggiante

DRAW(T([0,1])([-15,+15])(pianura))

DRAW(COLOR(brown)(DTM));


//es 2

vertici=DTM.geometry.vertices;

MinMax=function (vertici) {
MinZ=[0,0,1];
MaxZ=[0,0,0];
for (var i = 0; i <vertici.length; i++) {
		if (vertici[i].position.z>MaxZ[2]){
			MaxZ[0]=vertici[i].position.x
			MaxZ[1]=vertici[i].position.y
			MaxZ[2]=vertici[i].position.z
		}
		if (vertici[i].position.z<MinZ[2])
			MinZ=[vertici[i].position.x,vertici[i].position.y,vertici[i].position.z]
	};
	return [MinZ,MaxZ];
}

m=MinMax(vertici);

//lago
blue = [0,0,1]; 
lago=COLOR(blue)(CUBOID([16,20]))
DRAW(T([0,1,2])([-10,-8,m[0][2]+0.3])(lago));




