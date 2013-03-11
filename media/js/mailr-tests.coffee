define ['cs!mailr', 'extras/jquery', 'extras/jquery-autotype', 'extras/specit'], (mailreplace) ->
  enc = encodeURIComponent

  _mailto_address = 'comment@ilker.de'

  _sample_subject = enc 'any cool thing'
  _sample_mail = enc 'joe@example.com'
  _sample_note = enc 'this is important'
  _sample_title = enc 'The Article Title'
  _sample_ref = enc '/blog/the-article-title.html'
  _sample_external_ref = enc 'http://external.com/blog/the-article-title.html'

  _sample_url = "http://example.com?subject=#{ _sample_subject }&mail=#{ _sample_mail }&note=#{ _sample_note }&title=#{ _sample_title }&ref=#{ _sample_ref }"
  _sample_url_missing_ref = "http://example.com?title=#{ _sample_title }"
  _sample_url_missing_title = "http://example.com?ref=#{ _sample_ref }"
  _sample_url_without_subject = "http://example.com?title=#{ _sample_title }&ref=#{ _sample_ref }"
  _sample_url_with_external_ref = "http://example.com?subject=#{ _sample_subject }&mail=#{ _sample_mail }&note=#{ _sample_note }&title=#{ _sample_title }&ref=#{ _sample_external_ref }"

  describe "mailr-* annotated class text content substitution", -> 
    before -> mailreplace _sample_url, $

    it "should replace inner text of 'mailr-subject' with subject value from url", ->
      equal $('h5').text(), 'any cool thing'

  describe "substitution from url querystring parameters", ->
    before -> mailreplace _sample_url, $

    it "should replace subject with value", ->
      equal $('.mailr-subject').text(), 'any cool thing'

    it "should replace note with value", ->
      equal $('.mailr-note').text(), 'this is important'

    it "should ignore the 'mail' parameter and always use 'comment@ilker.de' as mailto address", ->
      ok $('a.mailr').attr('href').indexOf(_mailto_address) > -1  

    it "should replace href attribute of 'a.mailr' with mail and subject parameters", ->
      equal $('a.mailr').attr('href'), "mailto:#{ _mailto_address }?subject=#{ _sample_subject }"

  describe "mail link 'button' generation", ->
    before -> mailreplace _sample_url, $

    it "should create an 'a' tag within the 'div.mailr' element", ->
      equal $('div.mailr a').size(), 1

    it "should contain the full mailto: link in the href attribute", ->
      equal $('div.mailr a').attr('href'), "mailto:#{ _mailto_address }?subject=#{ _sample_subject }"

    it "should have 'Write A Comment' as text within a element", ->
      equal $('div.mailr a').text(), 'Write A Comment'

    it "should have 'span' tag following the 'a' tag", ->
      equal $('div.mailr a+span').size(), 1

    it "should contain 'via Email' text within span", ->
      equal $('div.mailr a+span').text(), 'via Email'

  describe "referring page link generation", ->
    before -> mailreplace _sample_url, $

    it "should replace all childs / text from 'span.mailr' with an 'a' tag", ->
      equal $('span.mailr a').size(), 1

    it "should contain the title property as text within the link with surrounding quotes", ->
      equal $('span.mailr a').text(), '"The Article Title"'

    it "should contain the referrer url in href", ->
      equal $('span.mailr a').attr('href'), '/blog/the-article-title.html'

  describe "ref parameter is required", ->
    before -> mailreplace _sample_url_missing_ref, $
  
    it "should not substitute div.mailr", ->
      ok $('div.mailr').is(':empty')

    it "should not substitute a.mailr", ->
      equal $('a.mailr').text(), 'This is a Link'

    it "should not substitute span.mailr", ->
      equal $('span.mailr').text(), 'Anything'

  describe "title parameter is required", ->
    before -> mailreplace _sample_url_missing_title, $
  
    it "should not substitute div.mailr", ->
      ok $('div.mailr').is(':empty')

    it "should not substitute a.mailr", ->
      equal $('a.mailr').text(), 'This is a Link'

    it "should not substitute span.mailr", ->
      equal $('span.mailr').text(), 'Anything'

  describe "subject defaulted from title if not given", ->
    before -> mailreplace _sample_url_without_subject, $

    it "should create the subject from title as 'Comment: [title]", ->
      ok $('a.mailr').attr('href').indexOf(enc 'Comment: The Article Title') > -1

  describe "ref must be an internal url (no phishlinking)", ->
    before -> mailreplace _sample_url_with_external_ref, $

    it "should not substitute anything", ->
      ok $('div.mailr').is(':empty')