$(document).ready(function() {
  // Update slider label on value change
  $('input[type=range]').change(updateControlLabel);

  // Update labels when form is reset
  $('#rating-controls button[type=reset]').click(resetRatingForm);

  // Submit rating values
  $('#rating-controls button[type=submit]').click(submitIdealValues);

  // Set default values before saving new submission
  $('form[name=new-submission-form]').submit(setDefaults);

  function updateControlLabel(event) {
    $('label[for=' + event.target.id + ']')
      .find('span')
      .text(event.target.value)
  }

  function resetRatingForm(event) {
    event.preventDefault();
    $('#rating-controls input[type=range]').val(5);
    $('#rating-controls label').find('span').text(5);
  }

  function submitIdealValues(event) {
    event.preventDefault()

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
  }

  function setDefaults(event) {
    // Stop form submission
    event.preventDefault();

    // Set a default value for all empty fields
    $('form[name=new-submission-form] input').each(function() {
      if ( !$(this).val() ) {
        $(this).val(25)
      }
    });

    // Now submit the form
    event.target.submit()
  }
});
