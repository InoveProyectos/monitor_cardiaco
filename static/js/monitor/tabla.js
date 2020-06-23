
var url = window.location.href

// Agregado para evitar que un onclick arruine las url
if(url.slice(-1) == '#')
{
	url = url.substring(0, url.length - 1);
}

function view(name) {
	
	var historico_url = url + '/tabla/historico?name=' + name
	
	window.location = historico_url
}

var tabla_url = url + '/tabla'

$.get(tabla_url, function(list) {
	
			
	personas = JSON.parse(list);		
	size = Object.keys(personas['name']).length;
	
	var table_data = '';

	for(var i= 0; i < size; i++)
	{
		name = personas['name'][i];
		last_record_time = personas['time'][i];
		last_record_value = personas['value'][i];
		record_count = personas['count'][i];

		table_data += '<tr>';
		table_data += '<td>'+name+'</td>';
		table_data += '<td>'+last_record_time+'</td>';
		table_data += '<td>'+last_record_value+'</td>';
		table_data += '<td>'+record_count+'</td>';
		table_data += '<td><a href="#" class="btn-view" onclick="view(\'' + name + '\')">Ver</a></td>';
		table_data += '</tr>';

	}
	$("#list_table").append(table_data);
	

}); 

      
