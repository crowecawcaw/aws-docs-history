# Troubleshooting Device Farm desktop browser testing

In this section, you'll find some common problems you can run into and how to address
them.

###### Topics

- [Can't connect to a
  RemoteWebDriver](#troubleshooting-cannot-connect-webdriver "#troubleshooting-cannot-connect-webdriver")
- [Timeouts when setting up
  RemoteWebDriver](#troubleshooting-timeout-framework "#troubleshooting-timeout-framework")
- [Rate limit errors during session
  creation](#troubleshooting-limits "#troubleshooting-limits")
- [I get errors during session
  creation](#troubleshooting-expected-browser "#troubleshooting-expected-browser")
- [Browser can't connect to my
  app](#troubleshooting-cannot-connect-browser "#troubleshooting-cannot-connect-browser")
- [Selenium 3 WebDriver testing
  framework is not working properly with Microsoft Edge (Chromium)](#troubleshooting-edge-dependencies "#troubleshooting-edge-dependencies")
- [My tests using XPath are slow](#troubleshooting-xpath-slow "#troubleshooting-xpath-slow")

## Can't connect to a

`RemoteWebDriver`

You might see this error when you have an expired URL from
`CreateTestGridUrl`. The URL is valid only for a short time, as specified
in the API call. Even if a session is created before the expiry, it cannot be accessed
after the expiration of the `RemoteWebDriver` URL.

## Timeouts when setting up

`RemoteWebDriver`

If your testing framework enforces strict timeouts for test completion, you might see
tests time out when setting up a new session. When you start a session, there is a 60 to
120 delay between the request to create the session and its availability for use. In
situations where you cannot increase timeouts, we recommend that you request a session
and open a page before your test framework sets up your tests, and then re-use that
session for your test suite. Make sure to close your session when your tests are
complete.

## Rate limit errors during session

creation

You have too many open sessions, are opening too many sessions per second, or are
making too many WebDriver requests per second. This is common in large, highly parallel
test suites where many browsers are being controlled at once.

For more information, see [Quotas in Device Farm desktop browser testing](techref-limits.md "techref-limits.md").

### Session creation rate management

If you are opening more than 5 sessions at a time, we recommend adding a random
delay before your session creation. A uniformly random delay of 0.5 to 5 seconds
will stagger your session creation and avoid rate limiting during this time.

### Actions per second rate management

If you are frequently experiencing a Rate Limit Exceeded error from Selenium actions other than Create Session calls, then please contact us via a support ticket for assistance. The current default limit is 1200 actions per second.

## I get errors during session

creation

If you get errors during session creation or are getting a browser that you don't
expect, check that your requested capabilities are valid. Make sure:

- the `browserName` capability contains a supported browser
  name
- the `browserName` capability value is lower case
- the `browserVersion` capability is set to
  `latest`, `latest-1`, or `latest-2`
- the `platform` capability is set to a supported
  platform
- the URL of the WebDriver hub has not expired

For more information, see

- [Supported browsers](techref-support.md#techref-support-browsers "techref-support.md#techref-support-browsers")
- [Supported platforms](techref-support.md#techref-support-platforms "techref-support.md#techref-support-platforms")

## Browser can't connect to my

app

You might see this in the following cases:

- Verify the DNS hostname that is being used to connect to your application. If
  you are using Amazon VPC, verify that private DNS is enabled and configured
  properly.
- If you are using a Amazon VPC configuration, verify that the correct subnets and
  security groups have been applied and that the specified VPC is in the
  `us-west-2` region. Additionally, if your application requires
  access to the internet, for example to access a CDN, those resources must be
  accessible from within the VPC or through a NAT gateway. For more information on
  NAT gateways, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
  _Amazon VPC user guide_.
- You must not block traffic from Amazon EC2 or other AWS services.

## Selenium 3 WebDriver testing

framework is not working properly with Microsoft Edge (Chromium)

Selenium 3 requires the _Selenium Tools for Microsoft Edge_ package to be
able to support the Edge browser. For more information, see [Using Selenium 3](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python#using-selenium-3 "https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python#using-selenium-3").

Note that Selenium 4 contains built-in support for Edge.

## My tests using XPath are slow

Due to the design of Selenium and the desktop browser testing feature, tests using
XPath are slow if they are not optimized properly.

If you use `find_elements_by_xpath`, consider the following
optimizations:

- Use an ID selector instead of XPath.
- In Python, avoid looping over the results multiple times or casting the
  results to a `list`, using `map`, or other late-binding
  iterators without caching the results. Use
  `str(`your-element.getAttribute(…)`)`
  when requesting strings.
- If you are using the list multiple times, cache the results if
  possible.

Selenium makes a full round-trip web request for each action you take on the returned
elements on an XPath query. For example, if you request every link in a page
(`//a`) and want to validate that every link points to a real resource,
each call to `getAttribute` from your test results in a full round-trip
request to the desktop browser testing feature running your test and the WebDriver
automating your browser, even if the content has not changed.
