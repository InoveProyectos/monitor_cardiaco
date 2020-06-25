$(document).ready(function(){

    send()
    setInterval(send, 10000)

});

function send()
{
    name = 'equipo1'
    heart_rate = document.getElementById('pulsos').value;

    var url = window.location.href

    $.post(url, {name: name},
        function(data) {
            $('#div_image').html('<img src="data:image/png;base64,' + data + '" />');      
                
        }
    );
}