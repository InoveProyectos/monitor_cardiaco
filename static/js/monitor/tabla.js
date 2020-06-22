
var url = window.location.href + '/tabla'

$.get(url, function(list) {
	
			
	personas = JSON.parse(list);		
	size = Object.keys(personas['name']).length;
	
	for(var i= 0; i < size; i++)
	{
		name = personas['name'][i];
		last_record_time = personas['time'][i];
		last_record_value = personas['value'][i];
		record_count = personas['count'][i];

		// Con estos datos se debe completar la tabla en HTML

	}
	

}); 

      
