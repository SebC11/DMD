$(document).ready(function(){
    console.log("Document Loaded");
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log(e);
        console.log("Form Submitted");
        let form = $('#register-form').serialize();
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
        let form = $(this).serialize();
        console.log(form);
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
                window.location.href = window.location.href;
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
                    console.log(response);
                    window.location.reload(true);
                } else {
                    alert(response);
                }
            }
        });
    });
   $('a.button').click(function() {
       console.log("liked");
       let stars = $(this).children()
       let numberOfStars = parseInt(stars[1].innerText.toString()) + 1;
       console.log($(this));
       let id = $(this).id.substring(6);
       console.log(id.toString());
       let content = encodeURI(document.getElementById("content" + id.toString()).innerText);
       let username = encodeURI(document.getElementById("username" + id.toString()).innerText);
       let form = "content=" + content + "&username=" + username + "&stars=" + numberOfStars.toString();
       $.ajax({
           url: '/update-stars',
           type: 'POST',
           data: form,
           success: function (response) {
               if(response == "success"){
                   document.getElementById("stars").innerText = numberOfStars.toString();
                   console.log("We did it");

               } else {
                   console.log("Failure");
               }
           }
       });

   });

});