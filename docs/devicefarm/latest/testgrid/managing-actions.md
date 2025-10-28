# Actions in Device Farm desktop browser testing

When you interact with the W3C WebDriver protocol, Device Farm logs the calls made as actions.

An `action` represents the WebDriver endpoint requested by your test's
`RemoteWebDriver`. Actions consist of:

- The HTTP `requestType` (method) used for the call.
- The HTTP `statusCode` returned by the WebDriver API.
- The time that the call was made.
- The number, in milliseconds, it took to make the call.
