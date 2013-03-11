mailr = (url, $, qsp, yuri) ->
  qs = qsp url
  return if not qs.ref or not qs.title

  uri = yuri.parse qs.ref
  return if uri.hostname.length > 0 and uri.hostname != 'ilker.de'

  qs.mail = 'comment@ilker.de'
  qs.subject ?= "Comment: #{ qs.title }"

  substitute = (key, value) ->
    $(".mailr-#{key}").text value

  mailto = (mail, subject) ->
    enc = encodeURIComponent
    "mailto:#{mail}?subject=#{enc subject}"

  substitute key, value for key, value of qs
  $('a.mailr').attr('href', mailto qs.mail, qs.subject)
  $('div.mailr').append "<a href='#{ mailto qs.mail, qs.subject }'>Write A Comment</a> <span>via Email</span>"
  $('span.mailr').empty().append "<a href='#{ qs.ref }'>\"#{ qs.title }\"</a>"

define [
  'cs!qsp', 'libs/yuri'
], (qsp, yuri) ->
  (url, $) -> mailr url, $, qsp, yuri