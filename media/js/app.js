function parseURI(e){var t=String(e).replace(/^\s+|\s+$/g,"").match(/^([^:\/?#]+:)?(\/\/(?:[^:@]*(?::[^:@]*)?@)?(([^:\/?#]*)(?::(\d*))?))?([^?#]*)(\?[^#]*)?(#[\s\S]*)?/);return t?{href:t[0]||"",protocol:t[1]||"",authority:t[2]||"",host:t[3]||"",hostname:t[4]||"",port:t[5]||"",pathname:t[6]||"",search:t[7]||"",hash:t[8]||""}:null}function absolutizeURI(e,t){function n(e){var t=[];return e.replace(/^(\.\.?(\/|$))+/,"").replace(/\/(\.(\/|$))+/g,"/").replace(/\/\.\.$/,"/../").replace(/\/?[^\/]*/g,function(e){e==="/.."?t.pop():t.push(e)}),t.join("").replace(/^\//,e.charAt(0)==="/"?"/":"")}return t=parseURI(t||""),e=parseURI(e||""),!t||!e?null:(t.protocol||e.protocol)+(t.protocol||t.authority?t.authority:e.authority)+n(t.protocol||t.authority||t.pathname.charAt(0)==="/"?t.pathname:t.pathname?(e.authority&&!e.pathname?"/":"")+e.pathname.slice(0,e.pathname.lastIndexOf("/")+1)+t.pathname:e.pathname)+(t.protocol||t.authority||t.pathname?t.search:t.search||e.search)+t.hash}var requirejs,require,define;(function(e){function c(e,t){return f.call(e,t)}function h(e,t){var n,r,i,s,o,a,f,l,c,h,p=t&&t.split("/"),d=u.map,v=d&&d["*"]||{};if(e&&e.charAt(0)===".")if(t){p=p.slice(0,p.length-1),e=p.concat(e.split("/"));for(l=0;l<e.length;l+=1){h=e[l];if(h===".")e.splice(l,1),l-=1;else if(h===".."){if(l===1&&(e[2]===".."||e[0]===".."))break;l>0&&(e.splice(l-1,2),l-=2)}}e=e.join("/")}else e.indexOf("./")===0&&(e=e.substring(2));if((p||v)&&d){n=e.split("/");for(l=n.length;l>0;l-=1){r=n.slice(0,l).join("/");if(p)for(c=p.length;c>0;c-=1){i=d[p.slice(0,c).join("/")];if(i){i=i[r];if(i){s=i,o=l;break}}}if(s)break;!a&&v&&v[r]&&(a=v[r],f=l)}!s&&a&&(s=a,o=f),s&&(n.splice(0,o,s),e=n.join("/"))}return e}function p(t,r){return function(){return n.apply(e,l.call(arguments,0).concat([t,r]))}}function d(e){return function(t){return h(t,e)}}function v(e){return function(t){s[e]=t}}function m(n){if(c(o,n)){var r=o[n];delete o[n],a[n]=!0,t.apply(e,r)}if(!c(s,n)&&!c(a,n))throw new Error("No "+n);return s[n]}function g(e){var t,n=e?e.indexOf("!"):-1;return n>-1&&(t=e.substring(0,n),e=e.substring(n+1,e.length)),[t,e]}function y(e){return function(){return u&&u.config&&u.config[e]||{}}}var t,n,r,i,s={},o={},u={},a={},f=Object.prototype.hasOwnProperty,l=[].slice;r=function(e,t){var n,r=g(e),i=r[0];return e=r[1],i&&(i=h(i,t),n=m(i)),i?n&&n.normalize?e=n.normalize(e,d(t)):e=h(e,t):(e=h(e,t),r=g(e),i=r[0],e=r[1],i&&(n=m(i))),{f:i?i+"!"+e:e,n:e,pr:i,p:n}},i={require:function(e){return p(e)},exports:function(e){var t=s[e];return typeof t!="undefined"?t:s[e]={}},module:function(e){return{id:e,uri:"",exports:s[e],config:y(e)}}},t=function(t,n,u,f){var l,h,d,g,y,b=[],w;f=f||t;if(typeof u=="function"){n=!n.length&&u.length?["require","exports","module"]:n;for(y=0;y<n.length;y+=1){g=r(n[y],f),h=g.f;if(h==="require")b[y]=i.require(t);else if(h==="exports")b[y]=i.exports(t),w=!0;else if(h==="module")l=b[y]=i.module(t);else if(c(s,h)||c(o,h)||c(a,h))b[y]=m(h);else{if(!g.p)throw new Error(t+" missing "+h);g.p.load(g.n,p(f,!0),v(h),{}),b[y]=s[h]}}d=u.apply(s[t],b);if(t)if(l&&l.exports!==e&&l.exports!==s[t])s[t]=l.exports;else if(d!==e||!w)s[t]=d}else t&&(s[t]=u)},requirejs=require=n=function(s,o,a,f,l){return typeof s=="string"?i[s]?i[s](o):m(r(s,o).f):(s.splice||(u=s,o.splice?(s=o,o=a,a=null):s=e),o=o||function(){},typeof a=="function"&&(a=f,f=l),f?t(e,s,o,a):setTimeout(function(){t(e,s,o,a)},4),n)},n.config=function(e){return u=e,n},define=function(e,t,n){t.splice||(n=t,t=[]),!c(s,e)&&!c(o,e)&&(o[e]=[e,t,n])},define.amd={jQuery:!0}})(),define("extras/almond",function(){}),define("cs",{load:function(e){throw new Error("Dynamic load not allowed: "+e)}}),function(){var e,t,n=function(e,t){return function(){return e.apply(t,arguments)}};t=typeof exports!="undefined"&&exports!==null?exports:this,e=function(){function e(e,t){this.itemselector=t,this.show=n(this.show,this),this.hide=n(this.hide,this),this.filter=n(this.filter,this),e('<form id="commandbox">\n  <label for="command"><span>Search:</span></label>\n  <input type="text" name="command" value="" />\n</form>').appendTo("#meta").hide(),this.form=e("#commandbox"),this.text=this.form.find("input")}return e.prototype.filter=function(e){var t,n;return n=this.form.find("input").val(),t=$(this.itemselector).hide().parent().parent().find("li:regex('"+n+"')").show()},e.prototype.hide=function(e,t){return t.unmap("ESC"),t.map("S",this.show),this.form.hide()},e.prototype.show=function(e,t){return t.unmap("S"),t.map("ESC",this.hide),this.form.show(),this.text.focus().keyup(this.filter)},e}(),define("cs!types/box",[],function(){return e})}.call(this),function(){var e,t,n=function(e,t){return function(){return e.apply(t,arguments)}};t=typeof exports!="undefined"&&exports!==null?exports:this,e=function(){function e(e){var t;this.binding=e,this.handle=n(this.handle,this),this.map=n(this.map,this),this.unmap=n(this.unmap,this),(t=this.binding)==null&&(this.binding={}),this.specialkeys={ESC:27}}return e.prototype.getCode=function(e){return this.specialkeys[e]||e.charCodeAt(0)},e.prototype.unmap=function(e){var t;return t=this.getCode(e),delete this.binding[t]},e.prototype.map=function(e,t){var n;return n=this.getCode(e),this.binding[n]=t},e.prototype.handle=function(e){var t,n;n=e.which,t=this.binding[n];if(t!=null)return t(e,this),e.preventDefault(),e.stopPropagation()},e}(),define("cs!types/keymap",[],function(){return e})}.call(this),function(){var e;e=function(e,t,n){var r,i;return e.extend(e.expr[":"],{regex:function(e,t,n,r){var i,s;return s=e.textContent||e.innerText||"",i=new RegExp(n[3]||"","i"),s.search(i)>=0}}),r=new t(e,".listing .item"),i=new n,i.map("S",r.show),e(document).keydown(function(e){return i.handle(e)})},define("cs!cmdb",["cs!types/box","cs!types/keymap"],function(t,n){return function(r){return e(r,t,n)}})}.call(this),function(){var e;e=function(e){var t,n,r,i,s,o,u,a;r=function(e){try{return decodeURIComponent(e)}catch(t){return e}},o={toString:function(){return e.substring(e.indexOf("?")+1)}},n=o.toString().split("&"),s=function(){var e,r,i;i=[];for(e=0,r=n.length;e<r;e++)t=n[e],i.push(t.split("="));return i}();for(u=0,a=s.length;u<a;u++)i=s[u],o[i[0]]=r(i[1]);return o},define("cs!qsp",[],function(){return e})}.call(this);var URIBuilder={parse:parseURI,absolute:absolutizeURI};define("libs/yuri",[],function(){return URIBuilder}),function(){var e;e=function(e,t,n,r){var i,s,o,u,a,f,l;o=n(e);if(!o.ref||!o.title)return;a=r.parse(o.ref);if(a.hostname.length>0&&a.hostname!=="ilker.de")return;o.mail="comment@ilker.de",(l=o.subject)==null&&(o.subject="Comment: "+o.title),u=function(e,n){return t(".mailr-"+e).text(n)},s=function(e,t){var n;return n=encodeURIComponent,"mailto:"+e+"?subject="+n(t)};for(i in o)f=o[i],u(i,f);return t("a.mailr").attr("href",s(o.mail,o.subject)),t("div.mailr").append("<a href='"+s(o.mail,o.subject)+"'>Write A Comment</a> <span>via Email</span>"),t("span.mailr").empty().append("<a href='"+o.ref+"'>\""+o.title+'"</a>')},define("cs!mailr",["cs!qsp","libs/yuri"],function(t,n){return function(r,i){return e(r,i,t,n)}})}.call(this),function(){var e;e=function(e){var t;return e(".slide-text").hide(),t=e("#logo").css("background-image"),e("a.slide-mode").click(function(){var n;return n=e("#content").hasClass("slidebig"),n?(e("#disclaimer").show(),e("#logo").css("background-image",t),e("#content").removeClass("slidebig"),e("#page").addClass("slide-page").removeClass("slidebig-page")):(e("#disclaimer").hide(),e("#logo").css("background-image","none"),e("#content").addClass("slidebig"),e("#page").addClass("slidebig-page").removeClass("slide-page"))}),e("a.slide-script").click(function(){return e(".slide-text").addClass("slide-text-show").show(),e(".slide-content,       #disclaimer").hide()}),e("a.slide-cover").click(function(){return e(".slide-text").removeClass("slide-text-show").hide(),e(".slide-content,       #disclaimer").show()})},define("cs!slidr",[],function(){return function(t){return e(t)}})}.call(this),define("main",["cs!cmdb","cs!mailr","cs!slidr"],function(e,t,n){return{cmdb:e,mailr:t,slidr:n}});