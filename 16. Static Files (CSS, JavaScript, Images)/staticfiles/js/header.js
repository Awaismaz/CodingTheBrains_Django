$(document).ready(function() {

    $('#logout-btn').on('click', function(e) {
      e.preventDefault();
      $.ajax({
        url: '/accounts/logout/',
        type: 'POST',
        headers: {
          'X-CSRFToken': csrfToken
        },
        success: function (response) {
          if (response.success){
            $('#logged-in').hide();
          }
        }

      });
    });
  });