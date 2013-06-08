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
