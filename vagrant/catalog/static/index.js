/*
Sets up the login button and sends data to /login
*/
$(".navbar-btn.btn-success").on("click", function(e) {
  e.preventDefault();
  window.location.href = "/login";
});

/*
Sets up the add button and sends user to /additem
*/
$(".btn-primary.add-new-item").on("click", function(e) {
  e.preventDefault();
  window.location.href = "/additem";
});

/*
Sets up the logout button and sends user to /gdisconnect
*/
$(".btn-danger.logout").on("click", function(e) {
  e.preventDefault();
  window.location.href = "/gdisconnect";
});

/*
Sets up the delete button and sends data to /catalogItem/itemID/delete
*/
function setupDelete(itemID) {
  $(".btn-danger.delete").on("click", function(e) {
    e.preventDefault();
    $.ajax({
      type: 'DELETE',
      url: '/catalogItem/' + itemID + '/delete',
      success: function(result) {
        window.location.href = "/success";
      }
    });
  });
}

/*
Selects the correct item in the select selector
*/
function selectOption(category) {
  $(".form-group select.options").val(category);
}

/*
Sets up the edit button and sends data to /edititem
*/
function setupEdit(itemID) {
  $(".btn-primary.submit").on("click", function(e) {
    e.preventDefault();
    var title = $("#title").val();
    var description = $("#description").val();
    var category = $("#category").val();
    var formData = {"title": title,
                    "description": description,
                    "category": category};
    $.ajax({
      type: 'POST',
      url: '/editItem/' + itemID + '/',
      data: formData,
      dataType: "text",
      success: function(result) {
        // window.location.href = "/success";
      }
    });
  });
}
/*
Sets up the add button and sends data to /additem
*/
function setupAdd() {
  $(".btn-primary.add").on("click", function(e) {
    e.preventDefault();
    var title = $("#title").val();
    var description = $("#description").val();
    var category = $("#category").val();
    var formData = {"title": title,
                    "description": description,
                    "category": category};
    $.ajax({
      type: 'POST',
      url: '/additem',
      data: formData,
      dataType: "text",
      success: function(result) {
        window.location.href = "/";
      }
    });
  });
}
