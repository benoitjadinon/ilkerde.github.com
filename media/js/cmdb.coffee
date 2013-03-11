cmdb = ($, Box, KeyMap) ->
  $.extend $.expr[':'], {
    regex: (e,i,m,a) ->
      text = e.textContent or e.innerText or ''
      expression = new RegExp(m[3] or '', 'i')

      text.search(expression) >= 0
  }

  box = new Box($, '.listing .item')
  keys = new KeyMap

  keys.map 'S', box.show

  $(document).keydown (e) -> keys.handle e

define [
  'cs!types/box', 
  'cs!types/keymap'
], (Box, KeyMap) ->
  ($) -> cmdb $, Box, KeyMap