$(document).ready(function(){

    send()
    setInterval(send, 10000)

});

function send()
{
    name = 'equipo1'

    var url = window.location.href

    $.post(url, {name: name},
        function(data) {
            $('#div_image').html('<img src="data:image/png;base64,' + data + '" />');      
                
        }
    );
}