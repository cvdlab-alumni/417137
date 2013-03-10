function select(data, key, values){
filterRes=[];
for(i=0;i<values.length;i++){
filterRes.push( data.filter(function(item){
 return (item[key]===values[i]);
})[0]);
}
return filterRes;
}
