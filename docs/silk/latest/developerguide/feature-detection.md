# Learn about feature detection

When you build a website, you want to deliver the best possible experience to all of your
customers, no matter what browser and platform they're using. You can do this with feature
detection. Feature detection is a content-delivery strategy predicated on feature availability,
not browser functionality. Instead of checking to see if a customer is using "browser X version
1.1" and then assuming that this version of browser X supports some feature, you test for the
feature directly and serve content accordingly.

###### Note

You can also use user agent detection to target content, but this approach can be
problematic. User agent detection requires you to keep track of the browsers your customers
use and the features that those browsers support. Those variables will change over time, so
user agent detection isn't future proof. User agent detection can be useful if feature
detection is expensive or if a particular feature is only partially implemented by a browser.
But in most cases, feature detection is the right choice. For more information about user agent detection, see [Learn about user agent strings](user-agent.md "user-agent.md").

## Additional Resources

- [HTML5 Rocks: Feature,
  Browser, and Form Factor Detection: It's Good for the Environment](http://www.html5rocks.com/en/tutorials/detection/ "http://www.html5rocks.com/en/tutorials/detection/")
- [A List Apart: Taking Advantage of HTML5 and CSS3 with Modernizr](http://alistapart.com/article/taking-advantage-of-html5-and-css3-with-modernizr "http://alistapart.com/article/taking-advantage-of-html5-and-css3-with-modernizr")
- [Dive Into HTML5: Detecting HTML5
  Features](http://diveintohtml5.info/detect.html "http://diveintohtml5.info/detect.html")
