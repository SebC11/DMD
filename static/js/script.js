$(document).ready(function(){
    console.log("Document Loaded");
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log("Form Submitted");
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response)
            }
        });
    });
});