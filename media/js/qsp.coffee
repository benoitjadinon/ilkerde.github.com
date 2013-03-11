qsp = (url) ->
  decode = (s) ->
    try
      return decodeURIComponent s
    catch e
      return s

  qs = {
    toString: ->
      url.substring(url.indexOf('?') + 1)
  }

  components = qs.toString().split '&'
  pairs = (c.split '=' for c in components)
  qs[pair[0]] = decode(pair[1]) for pair in pairs

  qs

define -> qsp