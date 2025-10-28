# Learn about user agent strings

In the user agent request header field, Amazon Silk sends one of three user agent strings,
depending on the view requested on the device by the customer. If a specific view is not
requested, the view defaults to Tablet for Fire tablets, and Mobile for Fire phones. If a site
has compatibility issues when rendered in the default view, a different view may be selected by
the device. The templates for the Amazon Silk user agents are shown below.

**Tablet**

```
Mozilla/5.0 (Linux; Android `android-version`; `product-model` Build/`product-build`) AppleWebKit/`webkit-version` (KHTML, like Gecko)
    Silk/`browser-version` like Chrome/`chrome-version` Safari/`webkit-version`
```

**Desktop**

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/`webkit-version` (KHTML, like Gecko)
    Silk/`browser-version` like Chrome/`chrome-version` Safari/`webkit-version`
```

**Mobile**

```
Mozilla/5.0 (Linux; Android `android-version`; `product-model` Build/`product-build`) AppleWebKit/`webkit-version` (KHTML, like Gecko)
    Silk/`browser-version` like Chrome/`chrome-version` Mobile Safari/`webkit-version`
```

###### Note

Red and italics indicates variable fields, which are described below.

###### Template fields

- `android-version` – The [Android platform
  version](http://developer.android.com/about/dashboards/index.html "http://developer.android.com/about/dashboards/index.html") (for example, `4.4.3`).
- `product-model` – The value of [Build.MODEL](http://developer.android.com/reference/android/os/Build.html#MODEL "http://developer.android.com/reference/android/os/Build.html#MODEL") (for example, `KFTT`).

For a complete list of the product models, see [Learn about screen resolution](screen-size.md "screen-size.md").

- `product-build` – The value of [Build.ID](http://developer.android.com/reference/android/os/Build.html#ID "http://developer.android.com/reference/android/os/Build.html#ID")
  (for example, `IML74K`).
- `webkit-version` – Indicates the version of WebKit used
  (for example, `535.19`). The version can change whenever the Fire device receives
  a software update.
- `browser-version` – Indicates the version of the Amazon Silk
  browser (for example, `44.1.54`). The version can change whenever the Fire device
  receives a software update.
- `chrome-version` – The version of Google Chrome with
  which the Amazon Silk browser is compatible.

## User agent string examples

### Examples of the Amazon Silk User Agent String

**Tablet**

```
Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko)
    Silk/44.1.54 like Chrome/44.0.2403.63 Safari/537.36
```

**Desktop**

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
    Silk/44.1.54 like Chrome/44.0.2403.63 Safari/537.36
```

**Mobile**

```
Mozilla/5.0 (Linux; U; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko)
    Silk/44.1.54 like Chrome/44.0.2403.63 Mobile Safari/537.36
```

### UA for Kindle Fire 1st Generation

###### Note

The UA for the Kindle Fire 1st Generation follows a slightly different
syntax.

In the examples below, red and italic text indicates variable fields. The
Amazon Silk-Accelerated value can be either `true` or `false`, depending
upon customer selection.

**Desktop/Tablet**

```
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/`1.0.13.81_10003810`) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=`true`
```

**Mobile**

```
Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; Silk/`1.0.13.81_10003810`) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Silk-Accelerated=`true`
```
