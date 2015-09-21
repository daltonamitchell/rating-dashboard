$(document).ready(function() {
  // Update slider label on value change
  $('input[type=range]').change(function(e) {
    $('label[for=' + e.target.id + ']')
      .find('span')
      .text(e.target.value)
  });

  // Update labels when form is reset
  $('#rating-controls button[type=reset]').click(function(e) {
    e.preventDefault();
    $('#rating-controls input[type=range]').val(5);
    $('#rating-controls label').find('span').text(5);
  });

  // Submit rating values
  $('#rating-controls button[type=submit]').click(function(e) {
    e.preventDefault()

    // Holds ideal values to send back
    var values = {};

    // Build ideal values object
    $('#rating-controls input[type=range]').each(function() {
      var id = $(this).context.id
                      .replace('-range','')
                      .replace('-','_');
      var value = parseInt($(this).val());
      values[id] = value;
    });

    // Set value on hidden object & submit
    $('input#ideal-values').val( JSON.stringify(values) );
    $('#rating-controls').find('form').submit();
  });
});
