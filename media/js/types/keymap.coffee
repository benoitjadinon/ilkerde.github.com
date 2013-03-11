root = exports ? this

class KeyMap
  constructor: (@binding) -> 
    @binding ?= {}
    @specialkeys = {
      'ESC':27
    }

  getCode: (k) ->
    @specialkeys[k] or k.charCodeAt 0

  unmap: (k) =>
    key = @getCode k
    delete @binding[key]
  
  map: (k,f) =>
    key = @getCode k
    @binding[key] = f

  handle: (e) =>
    key = e.which
    command = @binding[key]
    
    if command?
      command e, this
      e.preventDefault()
      e.stopPropagation()

define -> KeyMap