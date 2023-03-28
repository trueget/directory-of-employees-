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

function submitForm() {
    const formData = new FormData(document.querySelector('#sort-form'));
    fetch('{% url "employees:all_workers" %}', {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
        body: formData,
    })
    .then(response => response.text())
    .then(data => {
        document.querySelector('#model-list').innerHTML = data;
    });
}