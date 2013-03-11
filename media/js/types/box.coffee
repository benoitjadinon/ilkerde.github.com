root = exports ? this

class Box
  constructor: ($, @itemselector) ->
    $("""
      <form id="commandbox">
        <label for="command"><span>Search:</span></label>
        <input type="text" name="command" value="" />
      </form>
    """)
      .appendTo('#meta')
      .hide()

    @form = $('#commandbox')
    @text = @form.find('input')

  filter: (e) =>
    query = @form.find('input').val()

    matches = $(@itemselector)
      .hide()
      .parent().parent()
      .find("li:regex('#{query}')")
      .show()

  hide: (e, keys) => 
    keys.unmap 'ESC'
    keys.map 'S', @show

    @form.hide()

  show: (e, keys) =>
    keys.unmap 'S'
    keys.map 'ESC', @hide

    @form.show()
    @text
      .focus()
      .keyup @filter

define -> Box
