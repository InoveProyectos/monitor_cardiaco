
var url = window.location.href + '/tabla'

$.get(url, function(list) {
	
			
	personas = JSON.parse(list);		
	size = Object.keys(personas['name']).length;
	
	for(var i= 0; i < size; i++)
	{
		name = personas['name'][i];
		last_record_time = personas['last_record_time'][i];
		last_record_value = personas['last_record_value'][i];
		last_record_activity = personas['last_record_activity'][i];
		record_count = personas['record_count'][i];

		// Con estos datos se debe completar la tabla en HTML

	}
	

}); 

      
