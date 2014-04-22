

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

  <body id="articles_feed_test" class="article">
    <a href="articles_feed_test"></a>

    <div id="header">
      <div class="page">
        <div id="logo"><span class='no'>ilker.de: Creative Computing
</span></div>
      </div>
    </div>

    <div id="title">
      <div class="page">
        <hr />
        <div id="bar">
          <h2></h2>
        </div>
      </div>
    </div>

    <div id="body" class="article">
      <div class="page">
        <div id="content">
          <p>import requests</p>
<p>from unittest import TestCase
from unittest import main as runTests</p>
<p>from lxml import etree
from lxml.html import soupparser</p>
<p>class UrlMaker():
    host = 'www.dev.ilker.de'</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">page</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">page</span><span class="p">)</span><span class="o">:</span>
    <span class="k">return</span> <span class="err">&#39;</span><span class="n">http</span><span class="o">:</span><span class="c1">//{0}/{1}&#39;.format(self.host, page)</span>
</pre></div>


<p>class ArticlesFeedTest(TestCase, UrlMaker):
    def test_articles_page_has_same_list_as_rss_feed(self):
        r_page = requests.get(self.page('articles.html'))
        r_code = soupparser.fromstring(r_page.content)
        r_count = len(r_code.xpath('//ul[@class="all"]/li'))</p>
<div class="codehilite"><pre>    <span class="n">f_page</span> <span class="o">=</span> <span class="n">requests</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">page</span><span class="p">(</span><span class="err">&#39;</span><span class="n">feed</span><span class="p">.</span><span class="n">xml</span><span class="err">&#39;</span><span class="p">))</span>
    <span class="n">f_code</span> <span class="o">=</span> <span class="n">etree</span><span class="p">.</span><span class="n">XML</span><span class="p">(</span><span class="n">f_page</span><span class="p">.</span><span class="n">content</span><span class="p">)</span>
    <span class="n">f_count</span> <span class="o">=</span> <span class="n">len</span><span class="p">(</span><span class="n">f_code</span><span class="p">.</span><span class="n">xpath</span><span class="p">(</span><span class="err">&#39;</span><span class="c1">//a:entry&#39;, namespaces={&#39;a&#39;:&#39;http://www.w3.org/2005/Atom&#39;}))</span>

    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="n">r_count</span><span class="p">,</span> <span class="n">f_count</span><span class="p">)</span>
</pre></div>        </div>
        <div id="remarks">
                            </div>
      </div>
    </div>

    <div id="footer">
      <div class=page">
        <div class="about">
  <hr />
  <div class="more">
    <h5>Verfasst</h5>
    <ul><li><span>01.01.2012</span></li></ul>
        <h5>Website</h5>
    <ul>
      <li><a href="articles.html">
Verzeichnis</a></li>
      <li><a href="feed.xml">
Abonnement</a></li>
      <li><a href="imprint.html">
Impressum</a></li>
    </ul>
  </div>
</div>
                <div id="menu">
          <div class="page">
            <hr />
            <ul>
              <li><a href="/index.html">
Inhalt</a></li>
              <li><a href="/bio.html">
Person</a></li>
            </ul>
          </div>
        </div>
              </div>
    </div>

        <div id="disclaimer">
      <div class="page">
        <hr />
        <p>(c) Copyright 1998 - 2014 Ilker Cetinkaya.</p>
      </div>
    </div>
    
    <script type="text/javascript">
      require(['main'], function(app){
                              });
    </script>
  </body>
</html>
