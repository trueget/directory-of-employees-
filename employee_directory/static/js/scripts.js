$(function() {
    $('#search-form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            success: function(response) {
                $('#content').html(response);
            },
            error: function(xhr) {
                console.log(xhr.responseText);
            }
        });
    });
});