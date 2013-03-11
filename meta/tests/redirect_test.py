

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
  <body id="redirect_test">
    <a href="redirect_test"></a>
    <div id="page" class="article-page">
      <div id="header">
        <div id="pin"><a href="http://ilker.de"><span class='no'>Home
</span></a></div>
        <div id="bar">
          <h2></h2>
        </div>
      </div>

      <div id="content" class="article">
        <p>from unittest import main as runTests
from specs import HttpTest</p>
<p>import re</p>
<p>class ExistingUrlWithoutHtmlSuffix(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('test')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_with_html_suffix</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;test&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="o">.</span><span class="n">getheader</span><span class="p">(</span><span class="s">&#39;location&#39;</span><span class="p">),</span> 
        <span class="n">self</span><span class="o">.</span><span class="n">url</span><span class="p">(</span><span class="s">&#39;test.html&#39;</span><span class="p">))</span>
</pre></div>


<p>class NonExistentUrl(HttpTest):
    def test_respond_status_404(self):
        response = self.getresponse('non-existent')
        self.assertEqual(response.status, 404)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_respond_content_title_directory_of_alternatives</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;non-existent&#39;</span><span class="p">)</span>
    <span class="n">body</span> <span class="o">=</span> <span class="n">str</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="nb">read</span><span class="p">())</span>
    <span class="n">match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">r</span><span class="s">&#39;.*&lt;title&gt;404.*&#39;</span><span class="p">,</span> <span class="n">body</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertIsNotNone</span><span class="p">(</span><span class="n">match</span><span class="p">)</span>
</pre></div>


<p>class WordpressPageIndexedUrl(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('page/3')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_to_index_of_path</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;page/3&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="o">.</span><span class="n">getheader</span><span class="p">(</span><span class="s">&#39;location&#39;</span><span class="p">),</span>
        <span class="n">self</span><span class="o">.</span><span class="n">url</span><span class="p">(</span><span class="s">&#39;index.html&#39;</span><span class="p">))</span>
</pre></div>


<p>class WordpressTagbasedUrl(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('on/technology')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_to_index_of_path</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;on/technology&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="o">.</span><span class="n">getheader</span><span class="p">(</span><span class="s">&#39;location&#39;</span><span class="p">),</span>
        <span class="n">self</span><span class="o">.</span><span class="n">url</span><span class="p">(</span><span class="s">&#39;index.html&#39;</span><span class="p">))</span>
</pre></div>


<p>class WordpressArchiveBasedUrl(HttpTest):
    def test_redirect_status_301(self):
        response = self.getresponse('2007')
        self.assertEqual(response.status, 301)</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_location_to_index_of_path</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;2007&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="o">.</span><span class="n">getheader</span><span class="p">(</span><span class="s">&#39;location&#39;</span><span class="p">),</span>
        <span class="n">self</span><span class="o">.</span><span class="n">url</span><span class="p">(</span><span class="s">&#39;index.html&#39;</span><span class="p">))</span>
</pre></div>


<p>class NoWwwSubdomainPrefixedHost(HttpTest):
    host = 'dev.ilker.de'</p>
<div class="codehilite"><pre><span class="n">def</span> <span class="n">test_redirect_status_301</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;test&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">status</span><span class="p">,</span> <span class="mi">301</span><span class="p">)</span>

<span class="n">def</span> <span class="n">test_redirect_location_to_www_domain</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="o">.</span><span class="n">getresponse</span><span class="p">(</span><span class="s">&#39;test&#39;</span><span class="p">)</span>
    <span class="n">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span>
        <span class="n">response</span><span class="o">.</span><span class="n">getheader</span><span class="p">(</span><span class="s">&#39;location&#39;</span><span class="p">),</span>
        <span class="s">&#39;http://www.dev.ilker.de/meta/tests/test&#39;</span><span class="p">)</span>
</pre></div>


<p>if <strong>name</strong> == '<strong>main</strong>':
    runTests()</p>      </div>

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
