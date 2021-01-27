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
   $('.like-button').on("click", function() {
       let elements = document.getElementsByName($(this).attr("name"));
       let stars = $(this).children()[1].innerText;
       let button = $(this);
       let numberOfStars = parseInt(stars) + 1;

       let content = encodeURI(elements[2].innerText);
       let username = encodeURI(elements[1].innerText);
       let form = "content=" + content + "&username=" + username + "&stars=" + numberOfStars.toString();
       console.log(form);
       $.ajax({
           url: '/update-stars',
           type: 'POST',
           data: form,
           success: function (response) {
               if(response == "success"){
                   button.children()[1].innerHTML = numberOfStars.toString();
                   console.log("We did it");

               } else {
                   console.log("Failure");
               }
           }
       });
   });
    $(document).on('submit', '.comment-form', function(e){
        e.preventDefault();
        let form = $(this).serialize();


        $.ajax({
            url: '/submit-comment'
        })
    });
});