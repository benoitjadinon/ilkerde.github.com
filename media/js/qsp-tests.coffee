require ['cs!qsp', 'extras/jquery', 'extras/specit'], (qsparser) ->
  module 'qsp'

  qs = undefined

  enc = (str) ->
    encodeURIComponent str

  _sample_mail = enc 'joe@example.com'
  _sample_text = enc 'This is a test'
  _sample_url = "http://example.com/test/page.html?name=Joe&mail=#{ _sample_mail }&subject=#{ _sample_text }"
  _sample_url_malformed = "http://example.com/p.html?wrong=wrong%20%encoding"

  describe "query string extraction", -> 
    before -> qs = qsparser _sample_url 

    it "should detect query string in a sample url", ->
      equal qs.toString(), "name=Joe&mail=#{ _sample_mail }&subject=#{ _sample_text }"

  describe "query string recognition", ->
    before -> qs = qsparser _sample_url 

    it "should contain a name property with 'Joe' as value", ->
      equal qs.name, 'Joe'

    it "should have all 3 passed properties with values", ->
      ok (qs.name? and qs.mail? and qs.subject?)

    it "should unespace escaped values of properties", ->
      equal qs.mail, 'joe@example.com'

  describe "error handling", ->
    before -> qs = qsparser _sample_url_malformed

    it "should ignore an unescaping error and provide the raw value", ->
      equal qs.wrong, 'wrong%20%encoding'