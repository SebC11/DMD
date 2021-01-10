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
    $('#login-form').submit(function(e){
        console.log("test");
    });
    // $(document).on("submit", "#login-form", function(e){
    //     e.preventDefault();
    //     console.log("Login Attempted");
    //     var form = $(this).serialize();
    //     $.ajax({
    //         url: '/check-login',
    //         type: 'POST',
    //         data: form,
    //         success: function(response){
    //             if(response == "error"){
    //                 alert("Could not log in")
    //             }else {
    //                 console.log("Logged in as", response);
    //             }
    //
    //         }
    //     });
    // });
});