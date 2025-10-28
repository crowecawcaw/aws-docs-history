# User agent detection

You can use JavaScript to detect the Amazon Silk user agent across various Kindle Fire device
families. Unless you want to provide a unique experience for different Kindle Fire devices, we
recommend a general match that will work over time as product models and version numbers
change. The following examples illustrate best practices for matching the Amazon Silk user agent
across Kindle Fire device types.

###### Note

You can use user agent detection to target content, but this approach can be
problematic. User agent detection requires you to keep track of the browsers your customers
use and the features that those browsers support. Those variables will change over time, so
user agent detection isn't future proof. User agent detection can be useful if feature
detection is expensive or if a particular feature is only partially implemented by a
browser. But in most cases, feature detection is the right choice. For more information, see [Learn about feature detection](feature-detection.md "feature-detection.md").

###### Note

The tests below also match the user agent string for the PlayStation Vita browser. If
this is a concern, you can exclude that browser using the following condition:

```
!/Playstation/.test(navigator.userAgent)
```

**To detect Amazon Silk**

```

if (/\bSilk\b/.test(navigator.userAgent)) {
    alert("Silk detected!");
}
```

**To detect the Amazon Silk version**

```

var match = /\bSilk\/([0-9._-]+)\b/.exec(navigator.userAgent);
if (match) {
    alert("Detected Silk version "+match[1]);
}
```

**To detect mobile/desktop preference**

```

var match = /\bSilk\/(.*\bMobile Safari\b)?/.exec(navigator.userAgent);
if (match) {
    alert("Detected Silk in mode "+(match[1] ? "Mobile" : "Default (desktop)"));
}
```

**To detect multiple variables at once**

```

var match = /(?:; ([^;)]+) Build\/.*)?\bSilk\/([0-9._-]+)\b(.*\bMobile Safari\b)?/.exec(navigator.userAgent);
if (match) {
    alert("Detected Silk version "+match[2]+" on device "+(match[1] || "Kindle Fire")+" in mode "+(match[3] ? "Mobile" : "Default (desktop)"));
}
```
