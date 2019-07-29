// https://dribbble.com/shots/2308755-Search-Transform-Principle-Freebie
$('button').on('click', function(e) {
    e.preventDefault();
    $('form').addClass('opened');
    $('input[type="search"]').focus();
  });
  
  $('input[type="search"]').on('focusout', function(e) {
    $('form').removeClass('opened');
  });
  