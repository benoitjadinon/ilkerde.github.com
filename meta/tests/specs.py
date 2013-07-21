<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <title></title>
    <meta name="description" content="">
    <meta name="author" content="Ilker Cetinkaya">
    <meta name="viewport" content="width=device-width">
    <meta name="robots" content="noindex,nofollow">
    <link rel="shortcut icon" href="/favicon.ico?i3">
    <link rel="alternate" type="application/atom+xml" href="/feed.xml" title="ilker.de/articles">

        <link rel="stylesheet" href="http://app.ilker.de/devy?q=http://www.ilker.de/media/css/style.css?i3">
    
    
        <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<script src="http://code.jquery.com/jquery-migrate-1.1.1.min.js"></script>
    <script src="/media/js/app.js"></script>
    
            <script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-32542012-1']);
  _gaq.push(['_setDomainName', 'ilker.de']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>          </head>
  <body id="specs">
    <a href="specs"></a>
    <div id="page" class="article-page">
      <div id="header">
        <div id="pin"><a href="http://www.ilker.de"><span class='no'>Home
</span></a></div>
        <div id="bar">
          <h2></h2>
        </div>
      </div>

      <div id="content" class="article">
        <p>from unittest import TestCase
from httplib import HTTPConnection</p>
<p>test_host = 'www.dev.ilker.de'</p>
<p>class UrlMaker():
    host = test_host</p>
<div class="codehilite"><pre><span class="err">@</span><span class="n">classmethod</span>
<span class="n">def</span> <span class="n">path</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">page</span><span class="p">)</span><span class="o">:</span>
    <span class="k">return</span> <span class="s">&quot;/meta/tests/&quot;</span> <span class="o">+</span> <span class="n">page</span>

<span class="n">def</span> <span class="n">url</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">page</span><span class="p">)</span><span class="o">:</span>
    <span class="k">return</span> <span class="s">&quot;http://{0}/meta/tests/{1}&quot;</span><span class="p">.</span><span class="n">format</span><span class="p">(</span><span class="n">cls</span><span class="p">.</span><span class="n">host</span><span class="p">,</span> <span class="n">page</span><span class="p">)</span>
</pre></div>


<p>class HttpTest(TestCase, UrlMaker):
    @classmethod
    def setUpClass(cls):
        cls.http = HTTPConnection(cls.host, 80)</p>
<div class="codehilite"><pre><span class="err">@</span><span class="n">classmethod</span>
<span class="n">def</span> <span class="n">tearDownClass</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span><span class="o">:</span>
    <span class="n">cls</span><span class="p">.</span><span class="n">http</span><span class="p">.</span><span class="n">close</span><span class="p">()</span>

<span class="n">def</span> <span class="n">getresponse</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">page</span><span class="p">)</span><span class="o">:</span>
    <span class="n">self</span><span class="p">.</span><span class="n">http</span><span class="p">.</span><span class="n">request</span><span class="p">(</span><span class="err">&#39;</span><span class="n">GET</span><span class="err">&#39;</span><span class="p">,</span> <span class="n">self</span><span class="p">.</span><span class="n">path</span><span class="p">(</span><span class="n">page</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">http</span><span class="p">.</span><span class="n">getresponse</span><span class="p">()</span>
</pre></div>      </div>

      <div id="footer">
                <div class="about">
          <hr />
          <div id="published"><span class='no'>written on 
</span>01 January 2012</div>
          <div id="reference"><span class='no'>by Ilker Cetinkaya.
</span></div>
        </div>
        
                <div class="location">
          <hr />
          <div id="breadcrumb">
                        <a href="/meta/index.html">Meta</a>
                            / <a href="/meta/tests/test.html">Tests</a>
                                    </div>
        </div>
        
                <div class="index">
          <hr />
          <div id="logo"><span class='no'>Index of ilker.de
</span></div>
          <ul id="menu">
            <li><a href="/articles.html">
Artikel</a></li>
            <li><a href="/talks.html">
Vorträge</a></li>
            <li><a href="/bio.html">
Person</a></li>
          </ul>
        </div>
              </div>
      
      <div id="meta">
                        <div id="related">
          <hr />
          <h5>
Aktionen</h5>
                    <ul>
                        <li><a href="/feed.xml">
Abonnieren</a></li>
                                  </ul>
                  </div>
                        <div id="website">
          <hr />
          <h5>Website
</h5>
          <ul>
            <li><a href="/about.html">
Kolophon</a></li>
            <li><a href="/imprint.html">
Impressum</a></li>
          </ul>
        </div>
                      </div>

      <div id="disclaimer">
                <hr />
        <p>(c) Copyright <span class='no'>.
</span>1998 - 2013<span class='no'>.
</span> Ilker Cetinkaya.</p>
              </div>
    </div>
    <script type="text/javascript">
      require(['main'], function(app){
                              });
    </script>
  </body>
</html>
