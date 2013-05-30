

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

        <link rel="stylesheet" type="text/css" href="http://app.ilker.de/devy?q=http://www.ilker.de/media/css/style.css?i3">
                <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Gudea|Droid%20Sans%20Mono" >
    
        <script src="/media/js/app.js"></script>
    <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="http://code.jquery.com/jquery-migrate-1.1.1.min.js"></script>
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
  <body id="articles_feed_test">
    <a href="articles_feed_test"></a>
    <div id="page" class="article-page">
      <div id="header">
        <div id="pin"><a href="http://ilker.de"><span class='no'>Home
</span></a></div>
        <div id="bar">
          <h2></h2>
        </div>
      </div>

      <div id="content" class="article">
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
