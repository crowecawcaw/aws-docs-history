**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How the AWS WAF mobile SDK works

This section explains how the AWS WAF mobile SDK classes, properties, and operations work together.

The mobile SDKs provide you with a configurable token provider that you can use
for token retrieval and use. The token provider verifies that the requests that you
allow are from legitimate customers. When you send requests to the AWS
resources that you protect with AWS WAF, you include the token in a cookie, to
validate the request. You can handle the token cookie manually or have the token
provider do it for you.

This section covers the interactions between the classes, properties, and methods
that are included in the mobile SDK. For the SDK specification, see [AWS WAF mobile SDK specification](waf-mobile-sdk-specification.md "waf-mobile-sdk-specification.md").

## Token retrieval and caching

When you create the token provider instance in your mobile app, you configure how
you want it to manage tokens and token retrieval. Your main choice is how to
maintain valid, unexpired tokens for use in your app’s web requests:

- **Background refresh enabled** – This is the default.
  The token provider automatically refreshes the token in the background
  and caches it. With background refresh enabled, when you call
  `getToken()`, the operation retrieves the cached token.

The token provider performs the token refresh at configurable intervals, so that an
unexpired token is always available in the cache while the application
is active. Background refresh is paused while your application is in an
inactive state. For information about this, see [Retrieving a token following app
inactivity](#waf-mobile-sdk-how-back-from-inactive "#waf-mobile-sdk-how-back-from-inactive").

- **Background refresh disabled** – You can disable
  background token refresh, and then retrieve tokens only on demand.
  Tokens retrieved on demand aren't cached, and you can retrieve more than
  one if you want. Each token is independent of any others that you
  retrieve, and each has its own timestamp that's used to calculate
  expiration.

You have the following choices for token retrieval when background refresh
is disabled:

    + **`getToken()`** – When you call
     `getToken()` with background refresh disabled, the
     call synchronously retrieves a new token from AWS WAF.
     This is a potentially blocking call that might affect app
     responsiveness if you invoke it on the main thread.
    + **`onTokenReady(WAFTokenResultCallback)`**
     – This call asynchronously retrieves a new token and then
     invokes the provided result callback in a background thread when a
     token is ready.

### How the token provider retries failed token retrievals

The token provider automatically retries token retrieval when retrieval fails. Retries are
initially performed using exponential backoff with a starting retry wait time of
100 ms. For information about exponential retries, see [Error retries and exponential backoff in AWS](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md").

When the number of retries reaches the configured `maxRetryCount`, the token
provider either stops trying or switches to trying every
`maxErrorTokenRefreshDelayMsec` milliseconds, depending on the
type of token retrieval:

- **`onTokenReady()`** –
  The token provider switches to waiting
  `maxErrorTokenRefreshDelayMsec` milliseconds between
  attempts, and continues trying to retrieve the token.
- **Background refresh** – The token
  provider switches to waiting `maxErrorTokenRefreshDelayMsec`
  milliseconds between attempts, and continues trying to retrieve the
  token.
- **On-demand `getToken()` calls, when
  background refresh is disabled** – The token
  provider stops trying to retrieve a token and returns the previous token
  value, or a null value if there is no previous token.

## Token retrieval retry scenarios

When the token provider tries to retrieve a token, it might result in auto-retries depending on where token retrieval fails in the token acquisition flow. This section lists the possible places where you might see an auto-retry.

- **Obtaining or verifying the AWS WAF Challenge through /inputs or /verify:**
  - When a request to obtain and verify a AWS WAF challenge is made and fails, it can result in an auto-retry.
  - You might observe auto-retries happening here along with a `socketTimeoutException` error. This can have multiple causes including:
    - Low network bandwidth: Confirm your network connectivity settings
    - Mutated Application Integration URL: Confirm that the integration URL is not modified from what appears on the AWS WAF console

  - The auto-retry count is configurable with the `maxRetryCount()` function

- **Refreshing the token:**
  - When a request to refresh the token is made through the token handler, it might result in an auto-retry.
  - The auto-retry count here is configurable with the `maxRetryCount()` function.

A configuration with no auto-retries is possible by setting `maxRetryCount(0)`.

## Token immunity time and background refresh

The token immunity time that you configure in the Web ACL is independent of the token refresh interval you set in the AWS WAF mobile SDK.
When you enable background refresh, the SDK refreshes the token at the interval you specify using
`tokenRefreshDelaySec()`. This can result in multiple valid tokens existing simultaneously,
depending on your configured immunity time.

To prevent multiple valid tokens, you can disable background refresh and use the
`getToken()` function to manage the token lifecycle in your mobile app.

## Retrieving a token following app

inactivity

Background refresh is only performed while your app is considered active for your app
type:

- **iOS** – Background
  refresh is performed when the app is in the foreground.
- **Android** – Background
  refresh is performed when the app isn't closed, whether it's in
  the foreground or background.

If your app remains in any state that doesn’t support background refresh for longer than
your configured `tokenRefreshDelaySec` seconds, the token provider
pauses background refresh. For example, for an iOS app, if
`tokenRefreshDelaySec` is 300 and the app closes or goes into the
background for more than 300 seconds, the token provider stops refreshing the
token. When the app returns to an active state, the token provider automatically
restarts background refresh.

When your app comes back to an active state, call `onTokenReady()` so you can
be notified when the token provider has retrieved and cached a new token. Don't
just call `getToken()`, because the cache might not yet contain a
current, valid token.

## Application Integration URL

The AWS WAF mobile SDK application integration URL points to a Web ACL that you've enabled for application integration. This URL routes requests to the correct backend server and associates them with your customer. It doesn't serve as a hard security control, so exposing an integration URL doesn't pose a security risk.

You can technically modify the provided integration URL and still obtain a token. However, we don't recommend this because you might lose visibility into challenge solve rates or encounter token retrieval failures with `socketTimeoutException` errors.

## Dependencies

Each downloadable AWS WAF mobile SDK includes a README file that lists out the dependencies for its specific version of the SDK. Refer to the README for the dependencies for your version of the mobile SDK.

## Obfuscation/ProGuard (Android SDK Only)

If you use an obfuscation or minification product like ProGuard, you might need to exclude certain namespaces to ensure the mobile SDK works correctly. Check the README for your version of the mobile SDK to find the list of namespaces and exclusion rules.
