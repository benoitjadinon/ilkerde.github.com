

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

  <body id="redirect_test" class="article">
    <a href="redirect_test"></a>

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
          <p>from unittest import main as runTests
from specs import HttpTest</p>
<p>import re</p>
<p>class ExistingUrlWithoutHtmlSuffix(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('test')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_with_html_suffix</span><span class="p">(</span><span class="n">self</span><span class="p">)</span><span class="o">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">getresponse</span><span class="p">(</span><span class="err">&#39;</span><span class="n">test</span><span class="err">&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="p">.</span><span class="n">getheader</span><span class="p">(</span><span class="err">&#39;</span><span class="n">location</span><span class="err">&#39;</span><span class="p">),</span> 
        <span class="n">self</span><span class="p">.</span><span class="n">url</span><span class="p">(</span><span class="err">&#39;</span><span class="n">test</span><span class="p">.</span><span class="n">html</span><span class="err">&#39;</span><span class="p">))</span>
</pre></div>


<p>class NonExistentUrl(HttpTest):
    def test_respond_status_404(self):
        response = self.getresponse('non-existent')
        self.assertEqual(response.status, 404)</p>
<div class="codehilite"><pre><span class="nx">def</span> <span class="nx">test_respond_content_title_directory_of_alternatives</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self.</span><span class="nx">getresponse</span><span class="p">(</span><span class="s1">&#39;non-existent&#39;</span><span class="p">)</span>
    <span class="n">body</span> <span class="o">=</span> <span class="nx">str</span><span class="p">(</span><span class="nx">response.read</span><span class="p">())</span>
    <span class="k">match</span> <span class="o">=</span> <span class="nx">re.search</span><span class="p">(</span><span class="nb">r</span><span class="s1">&#39;.*&lt;title&gt;404.*&#39;</span><span class="p">,</span> <span class="nb">body</span><span class="p">)</span>
    <span class="bp">self.</span><span class="nx">assertIsNotNone</span><span class="p">(</span><span class="k">match</span><span class="p">)</span>
</pre></div>


<p>class WordpressPageIndexedUrl(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('page/3')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_to_index_of_path</span><span class="p">(</span><span class="n">self</span><span class="p">)</span><span class="o">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">getresponse</span><span class="p">(</span><span class="err">&#39;</span><span class="n">page</span><span class="o">/</span><span class="mi">3</span><span class="err">&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="p">.</span><span class="n">getheader</span><span class="p">(</span><span class="err">&#39;</span><span class="n">location</span><span class="err">&#39;</span><span class="p">),</span>
        <span class="n">self</span><span class="p">.</span><span class="n">url</span><span class="p">(</span><span class="err">&#39;</span><span class="n">index</span><span class="p">.</span><span class="n">html</span><span class="err">&#39;</span><span class="p">))</span>
</pre></div>


<p>class WordpressTagbasedUrl(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('on/technology')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_to_index_of_path</span><span class="p">(</span><span class="n">self</span><span class="p">)</span><span class="o">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">getresponse</span><span class="p">(</span><span class="err">&#39;</span><span class="n">on</span><span class="o">/</span><span class="n">technology</span><span class="err">&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="p">.</span><span class="n">getheader</span><span class="p">(</span><span class="err">&#39;</span><span class="n">location</span><span class="err">&#39;</span><span class="p">),</span>
        <span class="n">self</span><span class="p">.</span><span class="n">url</span><span class="p">(</span><span class="err">&#39;</span><span class="n">index</span><span class="p">.</span><span class="n">html</span><span class="err">&#39;</span><span class="p">))</span>
</pre></div>


<p>class WordpressArchiveBasedUrl(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('2007')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_to_index_of_path</span><span class="p">(</span><span class="n">self</span><span class="p">)</span><span class="o">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">getresponse</span><span class="p">(</span><span class="err">&#39;</span><span class="mi">2007</span><span class="err">&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="p">.</span><span class="n">getheader</span><span class="p">(</span><span class="err">&#39;</span><span class="n">location</span><span class="err">&#39;</span><span class="p">),</span>
        <span class="n">self</span><span class="p">.</span><span class="n">url</span><span class="p">(</span><span class="err">&#39;</span><span class="n">index</span><span class="p">.</span><span class="n">html</span><span class="err">&#39;</span><span class="p">))</span>
</pre></div>


<p>class NoWwwSubdomainPrefixedHost(HttpTest):
    host = 'dev.ilker.de'</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_status_301</span><span class="p">(</span><span class="n">self</span><span class="p">)</span><span class="o">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">getresponse</span><span class="p">(</span><span class="err">&#39;</span><span class="n">test</span><span class="err">&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">status</span><span class="p">,</span> <span class="mi">301</span><span class="p">)</span>

<span class="n">def</span> <span class="n">test_redirect_location_to_www_domain</span><span class="p">(</span><span class="n">self</span><span class="p">)</span><span class="o">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">getresponse</span><span class="p">(</span><span class="err">&#39;</span><span class="n">test</span><span class="err">&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="p">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="p">.</span><span class="n">getheader</span><span class="p">(</span><span class="err">&#39;</span><span class="n">location</span><span class="err">&#39;</span><span class="p">),</span>
        <span class="err">&#39;</span><span class="n">http</span><span class="o">:</span><span class="c1">//www.dev.ilker.de/meta/tests/test&#39;)</span>
</pre></div>


<p>if <strong>name</strong> == '<strong>main</strong>':
    runTests()</p>        </div>
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
