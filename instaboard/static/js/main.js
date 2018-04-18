$('#account-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});


function create_post() {
    console.log("create post is working!")
    $.ajax({
        url : "account", 
        type : "POST",
        data : { 
          username : $('#username').val(),
          password: $('#password').val() 
        }, 
        
        success : function(json) {
            console.log(json); 
            console.log("success");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};