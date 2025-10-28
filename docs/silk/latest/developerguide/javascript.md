# Learn about using JavaScript with Amazon Silk

Amazon Silk uses the [V8 JavaScript
engine](https://developers.google.com/v8/intro "https://developers.google.com/v8/intro") to compile and execute JavaScript.

Using the Amazon Silk **Settings** menu, users can enable or disable
JavaScript. The setting is enabled by default.

![JavaScript setting toggle switch in Amazon Silk browser settings menu.](images/silk-shared-javascript.png)
When JavaScript is disabled, Silk ignores the content of `<script>` tags.
You can use the `<noscript>` tag to let users know that JavaScript content is
disabled.

```
<html>
  <body>
    <h1>Test Script</h1>
    <script>document.write("JavaScript is enabled in your browser.")</script>
    <noscript>It looks like JavaScript is disabled in your browser, or your browser doesn't support JavaScript.</noscript>
  </body>
</html>

```

Here's the output of the above markup rendered by Amazon Silk with JavaScript
disabled:

![Error message indicating JavaScript is disabled or unsupported in the browser.](images/javascript_disabled_page.png)

## JavaScript Loading

Though not specific to Amazon Silk, the following recommendations for loading JavaScript
can improve the performance of your website.

- Wherever practical, combine multiple external script files into a single file to
  improve page load time.
- Avoid including duplicate scripts on a page.
- Include external CSS files before external scripts. Otherwise script loading may
  block style sheet loading. And include script files as far down the page as possible.
  HTML parsing is blocked by the downloading and execution of scripts.
- Don't put inline scripts between included CSS files and other resources. Like an
  external script, an inline script can prevent a CSS file from downloading in parallel to
  other resources. In general, it's best to avoid inline scripts altogether and instead
  include external JavaScript files.
- Use minified JavaScript. Minified JavaScript files are smaller and therefore
  download faster. Available tools for compressing JavaScript include [UglifyJS](https://github.com/mishoo/UglifyJS "https://github.com/mishoo/UglifyJS"), [Closure Compiler](https://developers.google.com/closure/compiler/ "https://developers.google.com/closure/compiler/"), and
  [YUI Compressor](http://yui.github.io/yuicompressor/ "http://yui.github.io/yuicompressor/").
- Consider using the [async](http://www.w3schools.com/tags/att_script_async.asp "http://www.w3schools.com/tags/att_script_async.asp") and [defer](http://www.w3schools.com/TAGs/att_script_defer.asp "http://www.w3schools.com/TAGs/att_script_defer.asp") attributes in your script elements. With `async` set, a
  script is downloaded asynchronously and then executed, blocking HTML parsing. With
  `defer` set, a script is downloaded asynchronously and then executed after
  HTML parsing has completed.
  To learn more about improving load times for scripts, see the following
  resources:

- [Properly including stylesheets and scripts](https://developers.google.com/speed/articles/include-scripts-properly "https://developers.google.com/speed/articles/include-scripts-properly")
- [14 Rules for Faster-Loading Web
  Sites](http://stevesouders.com/hpws/rules.php "http://stevesouders.com/hpws/rules.php")
- [Deep dive
  into the murky waters of script loading](http://www.html5rocks.com/en/tutorials/speed/script-loading/ "http://www.html5rocks.com/en/tutorials/speed/script-loading/")
