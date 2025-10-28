# How to detect a feature

There are several ways to detect features. You can write your own feature detection
scripts, or you can use a helper library. Both methods are demonstrated below.

###### Test for Feature Support

The following code detects support for the HTML5 canvas element by testing one of the
element's attributes (`getContext`). The attribute test is important because
browsers can create elements that they don't actually support. If we can interact with an
attribute, that gives us more information.

```
<!DOCTYPE html>
<html>
  <body>
    <div>Test support for the HTML5 canvas element.</div>
    <script>
    function supportsCanvas() {
        return !!document.createElement('canvas').getContext;
    }
    if (supportsCanvas()) {
        alert('Your browser supports the canvas element.');
    } else {
        alert('Your browser does not support the canvas element.');
    }
    </script>
    </body>
</html>

```

If our test for the `getContext` method returns true, we assume that canvas is
supported. The test uses double negation `!!` to force a boolean value (true or
false). For more on this canvas test and on the Modernizr test below, see [Canvas](http://diveintohtml5.info/detect.html#canvas "http://diveintohtml5.info/detect.html#canvas") in Mark Pilgrim's [Detecting HTML5 Features](http://diveintohtml5.info/detect.html "http://diveintohtml5.info/detect.html").

###### Test for a Feature with Modernizr

You can also detect features by using [Modernizr](https://modernizr.com/docs/#using-modernizr-with-javascript "https://modernizr.com/docs/#using-modernizr-with-javascript"), a JavaScript library that identifies support for HTML5 and CSS3
features. It minimizes the amount of code you have to write. You can build a custom
Modernizr library to test for specific features.

In an application, we need to serve content for the supported feature. And if the feature
isn't supported, we need to have a fallback. Polyfills can help with this. Polyfills are
JavaScript shims that approximate native browser functionality. Modernizr maintains a listing
of [HTML5 Cross Browser Polyfills](https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-Browser-Polyfills "https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-Browser-Polyfills").
