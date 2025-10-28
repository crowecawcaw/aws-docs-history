**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF mobile SDK specification

This section lists the SDK objects, operations, and configuration settings for the latest available version of the
AWS WAF mobile SDK. For detailed information about how the token provider and operations
work for the various combinations of configuration settings, see [How the AWS WAF mobile SDK works](waf-mobile-sdk-how-it-works.md "waf-mobile-sdk-how-it-works.md").

**`WAFToken`**

Holds an AWS WAF token.

**`getValue()`**

Retrieves the `String` representation of the
`WAFToken`.

**`WAFTokenProvider`**

Manages tokens in your mobile app. Implement this using a
`WAFConfiguration` object.

**`getToken()`**

If background refresh is enabled, this returns the cached
token. If background refresh is disabled, this makes a
synchronous, blocking call to AWS WAF to retrieve
a new token.

**`loadTokenIntoProvider(WAFToken)`**

Loads the specified token into the `WAFTokenProvider`,
replacing any token that the provider was managing. The token provider takes ownership
of the new token and handles refreshing it going forward. This operation also updates the token in the
cookie store, if `setTokenCookie` is enabled in the `WAFConfiguration`.

**`onTokenReady(WAFTokenResultCallback)`**

Instructs the token provider to refresh the token and invoke the provided callback
when an active token is ready. The token provider will
invoke your callback in a background thread when the token
is cached and ready. Call this when your app first loads and
also when it comes back to an active state. For more
information about returning to an active state, see [Retrieving a token following app
inactivity](waf-mobile-sdk-how-it-works.md#waf-mobile-sdk-how-back-from-inactive "waf-mobile-sdk-how-it-works.md#waf-mobile-sdk-how-back-from-inactive").

For Android or iOS apps, you can set `WAFTokenResultCallback` to the
operation that you want the token provider to invoke when a
requested token is ready. Your implementation of
`WAFTokenResultCallback` must take the
parameters `WAFToken`, `SdkError`. For
iOS apps, you can alternately create an inline function.

**`storeTokenInCookieStorage(WAFToken)`**

Instructs the `WAFTokenProvider` to store the specified AWS WAF token
into the SDK’s cookie manager. By default, the token is only added to the cookie store when it's
first acquired and when it's refreshed. If the application clears the shared cookie store for any reason,
the SDK doesn't automatically add the AWS WAF token back until the next refresh.

**`WAFConfiguration`**

Holds the configuration for the implementation of the `WAFTokenProvider`.
When you implement this, you provide your protection pack (web ACL)’s integration URL, the
domain name to use in the token, and any non-default settings that you
want the token provider to use.

The following list specifies the configuration settings that you can
manage in the `WAFConfiguration` object.

**`applicationIntegrationUrl`**

The application integration URL. Get this from the AWS WAF console or through the
`getWebACL` API call.

Required: Yes

Type: App-specific URL. For iOS, see [iOS
URL](https://developer.apple.com/documentation/foundation/url "https://developer.apple.com/documentation/foundation/url"). For Android, see [java.net URL](https://docs.oracle.com/javase/7/docs/api/java/net/URL.html "https://docs.oracle.com/javase/7/docs/api/java/net/URL.html").

**`backgroundRefreshEnabled`**

Indicates whether you want the token provider to refresh the token in the background. If you
set this, the token provider refreshes your tokens in the
background according to the configuration settings that
govern automatic token refresh activities.

Required: No

Type: `Boolean`

Default value: `TRUE`

**`domainName`**

The domain to use in the token, which is used in token acquisition and cookie
storage. For example, `example.com` or
`aws.amazon.com`. This is usually the host
domain of your resource that’s associated with the protection pack (web ACL),
where you’ll be sending web requests. For the ACFP
managed rule group, `AWSManagedRulesACFPRuleSet`,
this will usually be a single domain that matches the domain
in the account creation path that you provided in the rule group
configuration. For the ATP
managed rule group, `AWSManagedRulesATPRuleSet`,
this will usually be a single domain that matches the domain
in the login path that you provided in the rule group
configuration.

Public suffixes aren't allowed. For example, you can't use `gov.au` or `co.uk` as the token domain.

The domain must be one that AWS WAF will accept, based on
the protected host domain and the protection pack (web ACL)'s token domain
list. For more information, see [AWS WAF protection pack (web ACL) token domain list configuration](waf-tokens-domains.md#waf-tokens-domain-lists "waf-tokens-domains.md#waf-tokens-domain-lists").

Required: Yes

Type: `String`

**`maxErrorTokenRefreshDelayMsec`**

The maximum time in milliseconds to wait before repeating
a token refresh after a failed attempt.
For each auto-retry for a failed attempt, it will add an
exponential backoff up until the given input delay time.
This value is used after token retrieval has failed and been retried
`maxRetryCount` times.

Required: No

Type: `Integer`

Default value: `5000` (5 seconds)

Minimum value allowed: `1` (1
millisecond)

Maximum value allowed: `30000` (30
seconds)

**`maxRetryCount`**

The maximum number of retries to perform with exponential
backoff when a token is requested.

Required: No

Type: `Integer`

Default value: `Infinity`

Minimum value allowed: `0`

Maximum value allowed: `100`

**`setTokenCookie`**

Indicates whether you want the SDK’s cookie manager
to add a token cookie into requests and in other areas.

With a `TRUE` value:

- The cookie manager adds a token cookie to all requests
  whose path is under the path specified in `tokenCookiePath`.
- The `WAFTokenProvider`
  operation `loadTokenIntoProvider()` updates
  the token in the cookie store, in addition to loading it into the token provider.

Required: No

Type: `Boolean`

Default value: `TRUE`

**`tokenCookiePath`**

Used when `setTokenCookie` is `TRUE`. Indicates the top-level
path where you want the SDK’s cookie manager to add a token
cookie. The manager adds a token cookie to all requests that
you send to this path and to all child paths.

For example, if you set this to `/web/login`,
then the manager includes the token cookie for everything
sent to `/web/login` and any of its child paths,
like `/web/login/help`. It doesn't include the
token for requests sent to other paths, like `/`,
`/web`, or `/web/order`.

Required: No

Type: `String`

Default value: `/`

**`tokenRefreshDelaySec`**

Used for background refresh. The maximum amount of time in
seconds between background token refreshes.

Required: No

Type: `Integer`

Default value: `88`

Minimum value allowed: `88`

Maximum value allowed: `300` (5
minutes)

## AWS WAF mobile SDK errors

This section lists the possible errors for the current AWS WAF mobile SDK version.

**`SdkError`**

The error type returned when failing to retrieve a token. The Android and iOS SDK have the same error types.

The AWS WAF mobile SDK has the following error types:

**`invalidChallenge`**

This error is returned when the token server returns invalid challenge data, or the response blob is mutated by an attacker.

**`errorInvokingGetChallengeEndpoint`**

This error is returned when the token server sends a non-success response code back to the client or when a network error occurs.

**`invalidVerifyChallengeResponse`**

This error is returned when there is an error retrieving the `aws-waf-token` from the AWS WAF server's verification response, or the server response was tampered with.

**`errorInvokingVerifyEndpoint`**

This error is returned when the client receives a bad response from the AWS WAF server or network error when verifying the solved challenge.

**`internalError`**

This error is returned on all other errors that might occur within the SDK itself.

**`socketTimeoutException`**

This error is often returned when encountering network errors during token retrieval.

This error might be caused by the following:

- Low network bandwidth: Confirm your network connectivity settings
- Mutated Application Integration URL: Confirm that the integration URL is not modified from what appears on the AWS WAF console
