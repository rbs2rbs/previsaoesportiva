$(function() {   
    $('#liga').change(function(){
        $('.t_liga').hide();
        $('#' + $(this).val()).show();
    });
});