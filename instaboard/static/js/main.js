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
          if (json.status) {
            console.log('success')
          } else {
            show_error($('#results'));
          }
        },
        error : function(xhr,errmsg,err) {
          show_error($('#results'));
        }
    });
};

function show_error(element) {
  element.html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error</div>");
}