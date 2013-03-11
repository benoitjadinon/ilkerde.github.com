require ['cs!slidr', 'extras/jquery', 'extras/jquery-autotype', 'extras/specit'], (slideact) ->
  module 'slidr'

  logo_original = $('#logo').css('background-image')

  describe "slidr: invisibility of script text and decorations by default", ->
    before -> slideact $

    it "should hide the transscript section", ->
      ok $('.slide-text').is(':hidden')

    it "should not have class 'slide-text-show' on transscript", ->
      ok !$('.slide-text').hasClass('slide-text-show')

  describe "slidr: switching to large mode with button click", ->
    before -> 
      slideact $
      $('a.slide-mode').click()

    it "should replace logo image with none", ->
      equal $('#logo').css('background-image'), 'none'

    it "should hide the disclaimer", ->
      ok $('#disclaimer').is(':hidden')

    it "should add class 'slidebig' on content", ->
      ok $('#content').hasClass('slidebig')

    it "should replace class 'slide-page' with 'slidebig-page' on page", ->
      ok $('#page').hasClass('slidebig-page')
      ok !$('#page').hasClass('slide-page')

  describe "slidr: switching back to normal mode with button click", ->
    before -> 
      slideact $
      $('a.slide-mode').click()
      $('a.slide-mode').click()

    it "should show the disclaimer", ->
      ok $('#disclaimer').is(':visible')

    it "should remove class 'slide-text-show' on transscript", ->
      ok !$('.slide-text').hasClass('slide-text-show')

    it "should restore logo image with original", ->
      equal $('#logo').css('background-image'), logo_original

    it "should remove class 'slidebig' on content", ->
      ok !$('#content').hasClass('slidebig')

    it "should replace class 'slidebig-page' with 'slide-page' on page", ->
      ok $('#page').hasClass('slide-page')
      ok !$('#page').hasClass('slidebig-page')

  describe "slidr: showing text with script with button click", ->
    before -> 
      slideact $
      $('a.slide-script').click()

    it "should show the transscript", ->
      ok $('.slide-text').is(':visible')

    it "should hide the disclaimer", ->
      ok $('#disclaimer').is(':hidden')

    it "should hide the slide contents", ->
      ok $('.slide div').is(':hidden')

    it "should add class 'slide-text-show' on transscript", ->
      ok $('.slide-text').hasClass('slide-text-show')

  describe "slidr: showing slide contents with button click", ->
    before -> 
      slideact $
      $('a.slide-script').click()
      $('a.slide-cover').click()

    it "should hide the transscript", ->
      ok $('.slide-text').is(':hidden')

    it "should show the slide contents", ->
      ok $('.slide div').is(':visible')

    it "should show the disclaimer", ->
      ok $('#disclaimer').is(':visible')

    it "should remove class 'slide-text-show' on transscript", ->
      ok !$('.slide-text').hasClass('slide-text-show')

    it "should restore logo image with original", ->
      equal $('#logo').css('background-image'), logo_original
