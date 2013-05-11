#profilo sx

#scocca superiore tettuccio
#controls1=(MAP(BEZIER(S1)([[0.205,-0.410],  [0.269,-0.376], [0.325,-0.370],  [0.413,-0.384]]))(INTERVALS(1)(32)))

controls1=(MAP(BEZIER(S1)([[0.205,-0.410],  [0.229,-0.395], [0.254,-0.384],  [0.288,-0.372]]))(INTERVALS(1)(32)))

controls1_1=(MAP(BEZIER(S1)([[0.288,-0.372],  [0.320,-0.371], [0.348,-0.373],  [0.382,-0.378]]))(INTERVALS(1)(32)))

controls1_2=(MAP(BEZIER(S1)([[0.382,-0.378],  [0.403,-0.384], [0.425,-0.391],  [0.446,-0.399]]))(INTERVALS(1)(32)))

controls1_3=(MAP(BEZIER(S1)([[0.446,-0.399],[0.465,-0.405],[0.477,-0.409]]))(INTERVALS(1)(32)))

#scocca superiore cofano
#[0.205, -0.410],  [0.163, -0.418] , [0.125, -0.422],  [0.104, -0.430]


controls2=(MAP(BEZIER(S1)([[0.205, -0.410],  [0.163, -0.418] , [0.125, -0.422],  [0.104, -0.430]]))(INTERVALS(1)(32)))


controls3=(MAP(BEZIER(S1)([[0.104, -0.430],  [0.090,-0.440],  [0.084,-0.461],  [0.084,-0.490]]))(INTERVALS(1)(32)))

#[0.90,-0.440],  [0.84,-0.461],  [0.84,-0.490]

controls4=(MAP(BEZIER(S1)([[0.084, -0.490],  [0.112,-0.494],  [0.136,-0.495]]))(INTERVALS(1)(32)))


controls5=(MAP(BEZIER(S1)([[0.136, -0.495],  [0.140,-0.469],  [0.154,-0.445],[0.178,-0.440],[0.199,-0.445],[0.211,-0.459],[0.219,-0.477],[0.217,-0.495]]))(INTERVALS(1)(32)))


controls6=(MAP(BEZIER(S1)([[0.217,-0.495],[0.397,-0.495]]))(INTERVALS(1)(32)))


controls7=(MAP(BEZIER(S1)([[0.400,-0.495],[0.400,-0.477],[0.410,-0.457],[0.422,-0.447],[0.442,-0.443],[0.456,-0.449],[0.469,-0.459],[0.475,-0.470],[0.478,-0.495]]))(INTERVALS(1)(32)))


controls8=(MAP(BEZIER(S1)([[0.480,-0.495],[0.507,-0.492],[0.516,-0.490],[0.522,-0.481]]))(INTERVALS(1)(32)))

controls9=(MAP(BEZIER(S1)([[0.522,-0.481],[0.524,-0.460],[0.523,-0.453],[0.519,-0.453]]))(INTERVALS(1)(32)))

controls10=(MAP(BEZIER(S1)([[0.519,-0.453],[0.512,-0.436],[0.503,-0.426],[0.495,-0.418],[0.477,-0.409]]))(INTERVALS(1)(32)))

#vetro posteriore
#controls11=(MAP(BEZIER(S1)([[0.477,-0.409],[0.454,-0.395],[0.436,-0.388],[0.413,-0.384]]))(INTERVALS(1)(32)))



profiloSx=T(2)(0.496+0.03)(STRUCT([controls1,controls2,controls3,controls4,controls5,controls6,controls7,controls8,controls9,controls10,controls1_1,controls1_2,controls1_3]))

profiloDx= T(3)(0.192)(profiloSx)

proLateral=T(3)(-0.192/2)(STRUCT([profiloSx,profiloDx]))

#VIEW(proLateral)












#profilo superiore

#parafango
controls12=(MAP(BEZIER(S1)([[0.132,0,0.782],[0.142,0,0.782],[0.158,0,0.783],[0.176,0,0.783]]))(INTERVALS(1)(64)))

#faro
controls13=COLOR(RED)((MAP(BEZIER(S1)([[0.132,0,0.782],[0.109,0,0.769],[0.094,0,0.750],[0.082,0,0.732]]))(INTERVALS(1)(64))))
controls14=(MAP(BEZIER(S1)([[0.082,0,0.732],[0.081,0,0.685]]))(INTERVALS(1)(64)))

#metà posteriore
controls15=(MAP(BEZIER(S1)([[0.514,0,0.745],[0.521,0,0.728],[0.526,0,0.707],[0.527,0,0.688]]))(INTERVALS(1)(64)))

#continuo verso parafango parte posteriore
controls16=(MAP(BEZIER(S1)([[0.514,0,0.745],[0.505,0,0.765],[0.480,0,0.778],[0.446,0,0.782]]))(INTERVALS(1)(64)))

#scocca laterale
controls17=(MAP(BEZIER(S1)([[0.446,0,0.782],[0.394,0,0.780]]))(INTERVALS(1)(64)))

controls18=(MAP(BEZIER(S1)([[0.394,0,0.780],[0.349,0,0.780],[0.313,0,0.783]]))(INTERVALS(1)(64)))

controls19=(MAP(BEZIER(S1)([[0.313,0,0.783],[0.274,0,0.783],[0.226,0,0.780]]))(INTERVALS(1)(64)))

controls20=(MAP(BEZIER(S1)([[0.226,0,0.780],[0.202,0,0.783],[0.189,0,0.783],[0.176,0,0.783]]))(INTERVALS(1)(64)))

#VIEW(STRUCT([controls1,controls2,controls3,controls4,controls5,controls6,controls7,controls8,controls9,controls10,controls11]))

profiloSup=(STRUCT([controls13,controls14,controls12,controls15,controls16,controls17,controls18,controls19,controls20]))

#ok
proSup=T(2)(0.03)(STRUCT([   T(3)(0.688)(S([1,2,3])([1,1,-1])(profiloSup)),T(3)(-0.688)(profiloSup)]))

proSup2=T(2)(0.07)(proSup)

#VIEW(proSup)



#VIEW(STRUCT([proSup,proLateral,proSup2]))













#profilo anteriore

#tettuccio

controls21=(MAP(BEZIER(S1)([[0,-0.142,0.166],[0,-0.142,0.148],[0,-0.143,0.133],[0,-0.144,0.120]]))(INTERVALS(1)(64)))

#vetro laterale
controls22=(MAP(BEZIER(S1)([[0,-0.144,0.120],[0,-0.146,0.102],[0,-0.163,0.096],[0,-0.181,0.090]]))(INTERVALS(1)(64)))

controls23=(MAP(BEZIER(S1)([[0,-0.181,0.090],[0,-0.189,0.078],[0,-0.195,0.072],[0,-0.204,0.072]]))(INTERVALS(1)(64)))

controls24=(MAP(BEZIER(S1)([[0,-0.204,0.072],[0,-0.208,0.070],[0,-0.217,0.070],[0,-0.229,0.071]]))(INTERVALS(1)(64)))

controls25=(MAP(BEZIER(S1)([[0,-0.229,0.071],[0,-0.242,0.073],[0,-0.257,0.075],[0,-0.265,0.073]]))(INTERVALS(1)(64)))

controls26=(MAP(BEZIER(S1)([[0,-0.265,0.073],[0,-0.266,0.085],[0,-0.265,0.103]]))(INTERVALS(1)(64)))

controls27=(MAP(BEZIER(S1)([[0,-0.265,0.103],[0,-0.266,0.121],[0,-0.256,0.130],[0,-0.256,0.166]]))(INTERVALS(1)(64)))

profiloAnt=T(2)(0.266+0.03)(STRUCT([controls22,controls21,controls23,controls24,controls25,controls26,controls27]))


#ok

proAnt=T(1)(0.085)(STRUCT([T(3)(-0.166)(profiloAnt),T(3)(0.166)(S([1,2,3])([1,1,-1])(profiloAnt))]))

#VIEW(proAnt)


#VIEW(STRUCT([proSup,proLateral,proSup2,proAnt]))














#profilo posteriore

controls28=(MAP(BEZIER(S1)([[0,-0.141,0.43],[0,-0.141,0.409],[0,-0.143,0.393],[0,-0.144,0.383]]))(INTERVALS(1)(64)))

controls29=(MAP(BEZIER(S1)([[0,-0.144,0.383],[0,-0.146,0.37],[0,-0.157,0.364],[0,-0.168,0.359]]))(INTERVALS(1)(64)))

controls30=(MAP(BEZIER(S1)([[0,-0.144,0.383],[0,-0.146,0.37],[0,-0.157,0.364],[0,-0.168,0.359]]))(INTERVALS(1)(64)))

controls31=(MAP(BEZIER(S1)([[0,-0.168,0.359],[0,-0.181,0.354],[0,-0.19,0.341],[0,-0.201,0.338]]))(INTERVALS(1)(64)))

controls32=(MAP(BEZIER(S1)([[0,-0.201,0.338],[0,-0.217,0.338],[0,-0.232,0.339],[0,-0.248,0.342]]))(INTERVALS(1)(64)))


controls33=(MAP(BEZIER(S1)([[0,-0.248,0.342],[0,-0.258,0.344],[0,-0.262,0.349],[0,-0.264,0.362]]))(INTERVALS(1)(64)))

controls34=(MAP(BEZIER(S1)([[0,-0.264,0.362],[0,-0.265,0.381],[0,-0.251,0.387],[0,-0.250,0.4]]))(INTERVALS(1)(64)))

controls35=(MAP(BEZIER(S1)([[0,-0.250,0.4],[0,-0.25,0.43]]))(INTERVALS(1)(64)))

#ok
profiloPost=(T(2)(0.265)(STRUCT([controls28,controls29,controls30,controls31,controls32,controls33,controls34,controls35])))
proPost=T([1,2])([0.52,0.012])(STRUCT([T(3)(-0.43)(profiloPost),T(3)(0.43)(S([1,2,3])([1,1,-1])(profiloPost))]))

#VIEW(proPost)

profileTotal=T(1)(-0.3)(STRUCT([proSup,proLateral,proSup2,proAnt,proPost]))

profileTotal=S([1,2,3])([20,20,20])(profileTotal)

#VIEW(STRUCT([profileTotal,ruote]))


#VIEW(profileTotal)

#--------------------------------------------------





def annulus_sector (alpha, r, R) :
	#interval1 = INTERVALS(alpha)(36)
	#interval2 = INTERVALS(R-r)(36) #da r a R, problema
	#domain = PROD([interval1,interval2])
	domain = Plasm.translate(POWER([INTERVALS(alpha)(36),INTERVALS(R-r)(36)]),Vecf([0.0,0.0,r]))
	def mapping (v) :
		a = v[0]
		r = v[1]
		return [r*COS(a), r*SIN(a)]
	model = MAP(mapping)(domain)
	return model

#copertone nero   
torusSurface = COLOR([0,0,0,1])(TORUS([3.5, 6])([36,24]))
#VIEW(torusSurface)

#cerchione
torusSurface2 = COLOR([1,1,1,1])(TORUS([2.5, 5])([46,40]))
#VIEW(torusSurface2)

torusSurface2=T(3)(-1)(MULTEXTRUDE(annulus_sector(2*PI,3,5))(2))


#VIEW(STRUCT([torusSurface,torusSurface2]))



#bullone
#VIEW(T([3])([-0.6])(MULTEXTRUDE(RING([0.5, 1])([16,16]))(1.2)))

#raggi 3.5
#VIEW(STRUCT([R([1,3])(PI/2),T([3])([1]),CYLINDER([0.4,3.5])(36)]))



#raggi
#VIEW(STRUCT([R([1,3])(PI/2),T([1])([1]),CYLINDER([0.4,3.5])(36),    R([2,3])(PI/2),  T([3])([1])  ,CYLINDER([0.4,3.5])(36)     ]))

raggio=STRUCT([R([1,3])(PI/2),T([1])([1]),TRUNCONE([0.2,1.0,4])(32)])
#VIEW(T([3])([1])(raggio))

raggio2=STRUCT([R([1,2])(2*PI/5),raggio])
#VIEW(T([3])([1])(raggio2))

raggio3=STRUCT([R([1,2])(2*PI/5),raggio2])
#VIEW(T([3])([1])(raggio3))

raggio4=STRUCT([R([1,2])(2*PI/5),raggio3])
#VIEW(T([3])([1])(raggio4))

raggio5=STRUCT([R([1,2])(2*PI/5),raggio4])
#VIEW(T([3])([1])(raggio5))

ruotaCompleta=STRUCT([T([3])([1])(raggio5),T([3])([1])(raggio4),T([3])([1])(raggio3),T([3])([1])(raggio2),T([3])([1])(raggio)])

ruota=STRUCT([T([3])([-2])(ruotaCompleta),T([3])([-0.6])(MULTEXTRUDE(RING([0.5, 1])([16,16]))(1.2)),torusSurface,torusSurface2])

ruota=S(3)(1.5)(ruota)


ruota=S([1,2,3])([0.1,0.1,0.1])(ruota)




ruotaPosDx=T(1)(3-0.2)(ruota)
ruotaPosDx=T(3)(-2)(ruotaPosDx)
ruotaPosDx=T(2)(0.7)(ruotaPosDx)


ruotaAntDx=T(1)(-3+0.52)(ruota)
ruotaAntDx=T(3)(-2)(ruotaAntDx)
ruotaAntDx=T(2)(0.7)(ruotaAntDx)

ruotaPosSx=T(1)(3-0.2)(ruota)
ruotaPosSx=T(3)(2)(ruotaPosSx)
ruotaPosSx=T(2)(0.7)(ruotaPosSx)

ruotaAntSx=T(1)(-3+0.52)(ruota)
ruotaAntSx=T(3)(2)(ruotaAntSx)
ruotaAntSx=T(2)(0.7)(ruotaAntSx)

ruote=STRUCT([ruotaPosDx,ruotaAntDx,ruotaAntSx,ruotaPosSx])

#VIEW(ruote)

#VIEW(STRUCT([profileTotal,ruote]))
#VIEW della seconda ruota




#FINE PNEUMATICO----------------------------------------------------------------------------------------------------








#----------------------------------------------------------------------------------


#volante




def circl (sel,r,altezza):
	def circle0 (p):
		return [ r * COS(sel(p)), r * SIN(sel(p)), altezza ]; 
	return circle0

#mettici un toro o un anello
c=circl(S1,3,1)
co=BEZIER(S1)([c])
ma=MAP(co)(Plasm.power(INTERVALS(2*PI)(32),INTERVALS(1)(1)))






c1=circl(S1,2.5,1)
co1=BEZIER(S1)([c1])
ma2=MAP(co1)(Plasm.power(INTERVALS(2*PI)(32),INTERVALS(1)(1)))

#curva superiore
controls100=(MAP(BEZIER(S1)([[0.232,-0.542],[0.434,-0.412],[0.590,-0.416]]))(INTERVALS(1)(64)))
controls100p=((BEZIER(S1)([[0.232,-0.542],[0.434,-0.412],[0.590,-0.416]])))

#curva superiore specchiata
controls100_1=S(1)(-1)(controls100)
controls100_1=T(1)(0.590*2)(controls100_1)

#curva laterale
controls101=(MAP(BEZIER(S1)([[0.230,-0.682,0.1],[0.316,-0.564,0.1],[0.396,-0.672,0.1],[0.416,-0.75,0.1],[0.464,-0.82,0.1],[0.506,-0.896,0.1],[0.512,-0.97,0.1]]))(INTERVALS(1)(64)))
controls101p=((BEZIER(S1)([[0.230,-0.682,0.1],[0.316,-0.564,0.1],[0.396,-0.672,0.1],[0.416,-0.75,0.1],[0.464,-0.82,0.1],[0.506,-0.896,0.1],[0.512,-0.97,0.1]])))

#curva laterale specchiata
controls102=S(1)(-1)(controls101)
controls102=T(1)(0.590*2)(controls102)

#mezzo volante
C0 = BEZIER(S1)([[0,0,0],[10,0,0]])
C1 = BEZIER(S1)([[0,2,0],[8,3,0],[9,2,0]])
C2 = BEZIER(S1)([[0,4,1],[7,5,-1],[8,5,1],[12,4,0]])
C3 = BEZIER(S1)([[0,6,0],[9,6,3],[10,6,-1]])
out = MAP(BEZIER(S2)([controls100p,controls101p]))(  Plasm.power(INTERVALS(1)(30),INTERVALS(1)(30))  )

#mezzo volante specchiato
out2=S(1)(-1)(out)
out2=T(1)(0.590*2)(out2)



#triangolo centrale
#C2 = BEZIER(S1)([[0.512,-0.97,0.1],[0.59,-0.97,0.1]])
#C3 = BEZIER(S1)([[0.668,-0.97,0.1],[0.590,-0.416,0.1]])
#C4 = BEZIER(S1)([[0.512,-0.97,0.1],[0.590,-0.416,0.1]])
#C5= BEZIER(S1)([[0.59,-0.97,0.1],[0.668,-0.416,0.1]])

#out3=MAP(COONSPATCH([C2,C3,C4,C5]))(Plasm.power(INTERVALS(1)(10),INTERVALS(1)(10)))

C4 = BEZIER(S1)([[0.512,-0.97],[0.668,-0.97]])
C5 = BEZIER(S1)([[0.590,-0.416]])


out3=MAP(BEZIER(S2)([C4,C5]))(Plasm.power(INTERVALS(1)(50),INTERVALS(1)(50)))
#coons






volanteInt=(STRUCT([out,out2,out3]))

volanteInt=MULTEXTRUDE(volanteInt)(0.2)



volanteInt=S(3)(0.5)(volanteInt)


volanteInt=T(1)(-0.23-0.156-0.17-0.05)(volanteInt)
volanteInt=T(2)(0.8)(volanteInt)
volanteInt=S([1,2])([2.5,2.5])(volanteInt)
volanteInt=T(2)(-0.5)(volanteInt)
volanteInt=T(3)(-0.03)(volanteInt)
volanteInt=T(1)(0.03)(volanteInt)

volanteInt=COLOR(BLACK)(volanteInt)

esternoVol=COLOR(BLACK)(TORUS([0.8,1])([30,30]))



volante=(STRUCT([volanteInt,esternoVol]))


volante=R([1,3])(3*PI/2)(volante)
volante=T(3)(1)(volante)
volante=T(1)(-1.5)(volante)
volante=T(2)(2.5)(volante)
volante=S([1,2,3])([0.4,0.4,0.4])(volante)
volante=T(1)(-0.5)(volante)
volante=T(2)(0.5)(volante)
volante=T(3)(0.3)(volante)

VIEW(STRUCT([profileTotal,ruote,volante]))


#VIEW(out)



#VIEW(STRUCT([controls100,controls101,controls102,controls100_1]))



#VIEW(ma)




