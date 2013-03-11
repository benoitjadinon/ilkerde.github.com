slidr = ($) ->
  $('.slide-text').hide()

  logo_image = $('#logo').css('background-image')
  
  $('a.slide-mode').click ->
    is_large = $('#content').hasClass('slidebig')

    if !is_large
      $('#disclaimer').hide()
      $('#logo').css('background-image', 'none')
      $('#content').addClass('slidebig')
      $('#page')
        .addClass('slidebig-page')
        .removeClass('slide-page')
    else
      $('#disclaimer').show()
      $('#logo').css('background-image',logo_image)
      $('#content').removeClass('slidebig')
      $('#page')
        .addClass('slide-page')
        .removeClass('slidebig-page')

  $('a.slide-script').click ->
    $('.slide-text')
      .addClass('slide-text-show')
      .show()
    $('.slide-content,
       #disclaimer').hide()

  $('a.slide-cover').click ->
    $('.slide-text')
      .removeClass('slide-text-show')
      .hide()
    $('.slide-content,
       #disclaimer').show()

define ->
  ($) -> slidr $