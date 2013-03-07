function identity(n){
	var matrix=[];
	for(i=0;i<n;i++){
		matrix[i]=[];
		for(j=0;j<n;j++){
			if(j!==i)
				matrix[i][j]=0;
			else
				matrix[i][j]=1;
		}
	}
	return matrix;
}