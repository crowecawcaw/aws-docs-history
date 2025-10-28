# Learn about the Do Not Track header field

Amazon Silk supports the Do Not Track (DNT) header request field, an HTTP header field that
specifies a user preference about data collection. Many
websites collect
information about user browsing behavior, and with the DNT field users can opt out of such data
collection.

###### To locate the DNT option

1. From the Silk browser, tap the menu icon, and then tap **Settings**.
2. Tap **Privacy**, and then tap **'Do Not Track'**.
3. You can turn DNT on or off.
   Amazon Silk users configure their DNT preferences on the device, and these preferences are then
   communicated in the HTTP request header in the DNT field. A DNT header with a value of
   `1` indicates that the user prefers **not** to allow
   the target site to track the user's browsing behavior. A DNT header with a value of
   `0` indicates that the user has the default setting, which allows the target site
   to track the user's browsing behavior.

Here's [a W3C
example](http://www.w3.org/TR/tracking-dnt/#dnt-header-field "http://www.w3.org/TR/tracking-dnt/#dnt-header-field") of an HTTP header with the DNT field set to 1:

```

GET /something/here HTTP/1.1
Host: example.com
DNT: 1
```

The Do Not Track standard also allows for a window property to detect Do Not Track status
inside JavaScript or other dynamic site content. Amazon Silk supports this property and will set it if
the user has expressed a Do Not Track preference. The property is
`navigator.doNotTrack`, and it will be set to “yes” if the user has selected Do Not
Track, and “no” (the default) if the user has decided to permit tracking.

Note that the W3C specification for DNT behavior defines request and response headers for
communicating tracking preferences, but it does not require sites to respect an expressed user
preference.

## Additional Resources

To learn more about the Do Not Track standard, see the following resources:

- [Tracking Preference
  Expression](http://www.w3.org/TR/tracking-dnt/ "http://www.w3.org/TR/tracking-dnt/")
- [Mozilla Developer Network: The Do Not Track Field Guide](https://developer.mozilla.org/en-US/docs/Web/Security/Do_not_track_field_guide "https://developer.mozilla.org/en-US/docs/Web/Security/Do_not_track_field_guide")
- [Mozilla Developer Network: Navigator.doNotTrack](https://developer.mozilla.org/en-US/docs/Web/API/navigator.doNotTrack "https://developer.mozilla.org/en-US/docs/Web/API/navigator.doNotTrack")
- [Do Not Track: Universal Web Tracking Opt
  Out](http://donottrack.us/ "http://donottrack.us/")
