$(document).ready(function(){
    $('.btn-send').click(function(e)
    {
        e.preventDefault();

        name = 'Hector'
        heart_rate = 58

        var url = window.location.href

        $.post(url, {name: name, heart_rate: heart_rate},
            function(data) {
                $('#div_image').html('<img src="data:image/png;base64,' + data + '" />');      
                    
            }
        );
 
    });
});