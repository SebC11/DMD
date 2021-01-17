$(document).ready(function(){
    console.log("Document Loaded");
    console.log($("#loginForm"));
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log(e);
        console.log("Form Submitted");
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(){
                window.location.href='/login'
            }
        });
    });
    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();
        console.log("Login Attempted");
        var form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(response){
                if(response == "error"){
                    alert("Could not log in")
                }else {
                    console.log("Logged in as", response);
                    window.location.href='/';
                }
            }
        });
    });
    $(document).on('click', '#logout', function(e){
        console.log("triggered logout");
        e.preventDefault();

        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(response){
                if(response == "success"){
                    window.location.href = '/login';
                }else {
                    alert("Something went wrong");
                }
            }
        });
    });

    $(document).on("submit", '#post-activity', function (e){
        e.preventDefault();
        form = $(this).serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });
    $(document).on("submit", '#settings-form', function (e) {
        e.preventDefault();
        form = $(this).serialize();
        $.ajax({
            url: '/post-settings',
            type: 'POST',
            data: form,
            success: function(response){
                if(response == "success"){
                    window.location.href = window.location.href;
                } else {
                    alert(response);
                }
            }
        });
    });
});