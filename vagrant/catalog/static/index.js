$(".navbar-btn.btn-success").on("click", function(e) {
  e.preventDefault();
  window.location.href = "/login";
});
$(".btn-primary.add-new-item").on("click", function(e) {
  e.preventDefault();
  window.location.href = "/additem";
});
$(".btn-danger.logout").on("click", function(e) {
  e.preventDefault();
  window.location.href = "/gdisconnect";
});

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

function selectOption(category) {
  $(".form-group select.options").val(category);
}

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
