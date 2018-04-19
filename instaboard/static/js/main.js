// Add instagram account modal

$('#account-form').on('submit', function(event){
    event.preventDefault();
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

$('#following-user-follower-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    following_user_follower_form();
});

function following_user_follower_form() {
    console.log("Following_user_follower_form is working!")
    $.ajax({
        url : "follow", 
        type : "POST",
        data : { 
          user_id : $('#user_id').val(),
          username: $('#username').val(),
        }, 
        success : function(json) {
          console.log(json);
        },
        error : function(xhr,errmsg,err) {
          show_error($('#results'));
        }
    });
};