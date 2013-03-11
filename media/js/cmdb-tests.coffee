define ['cs!cmdb', 'extras/jquery', 'extras/jquery-autotype', 'extras/specit'], (commandbox) ->
  module 'cmdb'

  typein = (k) ->
    tb = $('input[name="command"]')
    tb.autotype(k)

  dokeydown = (k) ->
    e = $.Event 'keydown'
    e.which = {
      'ESC':27
    }[k] or k.charCodeAt 0

    $(document).trigger(e)

  visibleitems = (items) ->
    lis = $('#list li')
    ids = ($(li).attr('id') for li in lis when $(li).is(':visible'))
    !(ids < items or ids > items)
    
  describe "cmdb: regular expression matching", -> 
    before -> commandbox $

    it "should extend jquery expressions with regex expression", ->
      ok $.expr[':'].regex?

    it "should match contents of an element with a regex", ->
      equal $('#list').find('li:regex("some")').length, 1

    it "should not match a nonexistent text of a regex", ->
      equal $('#list').find('li:regex("none")').length, 0

    it "should match an expression case insensitive", ->
      equal $('#list').find('li:regex("OTH")').length, 2

  describe "cmdb: box structure and appearance", ->
    before -> commandbox $
      
    it "should create a form with id 'commandbox'", -> 
      ok $('#commandbox').length
    
    it "should create a textbox named 'command' within form", ->
      ok $('#commandbox input[name="command"]').length

    it "should create a label for the textbox", ->
      ok $('#commandbox label[for="command"]').length

    it "should have the initial text 'Search:' enclosed in a span within the label", ->
      equal $('label[for="command"] span').text(), 'Search:'

    it "should not be visible", ->
      ok $('#commandbox').is(':hidden')

  describe "cmdb: keyboard control", ->
    before -> commandbox $

    it "should display the form when the 'S' key is pressed", ->
      dokeydown 'S'
      ok $('#commandbox').is(':visible')

    it "should focus the textbox when the 'S' key is pressed", ->
      dokeydown 'S'
      ok $('input[name="command"]').is(':focus')

    it "should not show form twice when 'S' key is pressed twice", ->
      dokeydown 'S'
      $('#commandbox').hide()
      dokeydown 'S'
      ok $('#commandbox').is(':hidden')

    it "should hide form when 'ESC' key is pressed after it has been shown", ->
      dokeydown 'S'
      dokeydown 'ESC'
      ok $('#commandbox').is(':hidden')

    it "should not hide form when 'ESC' key is pressed but box wasn't invoked by 'S' key", ->
      $('#commandbox').show()
      dokeydown 'ESC'
      ok $('#commandbox').is(':visible')

    it "should activate form when 'S' is pressed after a previous hiding using 'ESC'", ->
      dokeydown 'S'
      dokeydown 'ESC'
      dokeydown 'S'
      ok $('#commandbox').is(':visible')

    it "should not hide form when 'ESC' key is pressed after a previous hiding and visible box not being invoked by 'S' key", ->
      dokeydown 'S'
      dokeydown 'ESC'
      $('#commandbox').show()
      dokeydown 'ESC'
      ok $('#commandbox').is(':visible')

  describe "cmdb: search command: input box filter behaviour", ->
    before -> commandbox $

    it "should only display 'some' and 'STUFF' when searching for 's' in input box", -> 
      dokeydown 'S'
      typein 's'
      ok visibleitems(['some', 'stuff'])