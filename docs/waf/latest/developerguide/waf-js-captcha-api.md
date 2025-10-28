**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using the CAPTCHA JavaScript API

This section provides instructions for using the CAPTCHA integration API.

The CAPTCHA JavaScript API allows you to configure the CAPTCHA puzzle and place it where you want
in your client application. This API leverages the features of the intelligent
threat JavaScript APIs to acquire and use AWS WAF tokens after an end user
successfully completes a CAPTCHA puzzle.

Implement the JavaScript integration first in a test environment, then in
production. For additional coding guidance, see the sections that follow.

###### To use the CAPTCHA integration API

1. **Install the API**
   1. Sign in to the AWS Management Console and open the AWS WAF console at
      [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
   2. In the navigation pane, choose **Application integration**. On the
      **Application integration** page, you can see tabbed
      options.
   3. Select **CAPTCHA integration**.
   4. Copy the listed JavaScript integration script tag for use in your integration.
   5. In your application page code, in the `<head>` section, insert the script tag
      that you copied. This inclusion makes the CAPTCHA puzzle available for
      configuration and use.

   ```
   <head>
       <script type="text/javascript" src="`integrationURL`/jsapi.js" defer></script>
   </head>
   ```

   This `<script>` listing is configured with the `defer`
   attribute, but you can change the setting to `async` if you want
   a different behavior for your page.

   The CAPTCHA script also automatically loads the intelligent threat integration script
   if it isn't already present. The intelligent threat integration script
   causes your client application to automatically retrieve a token in the
   background on page load, and provides other token management functionality
   that you need for your use of the CAPTCHA API.

2. **(Optional) Add domain configuration for the client's
   tokens** – By default, when AWS WAF creates a token, it
   uses the host domain of the resource that’s associated with the protection pack (web ACL). To
   provide additional domains for the JavaScript APIs, follow the guidance at
   [Providing domains for use in the
   tokens](waf-js-challenge-api-set-token-domain.md "waf-js-challenge-api-set-token-domain.md").
3. **Get the encrypted API key for the client** – The CAPTCHA API requires an encrypted API key that contains a list of valid
   client domains. AWS WAF uses this key to
   verify that the client domain you're using with the integration is approved to use AWS WAF CAPTCHA.
   To generate your API key, follow the guidance at [Managing API keys for the JS CAPTCHA API](waf-js-captcha-api-key.md "waf-js-captcha-api-key.md").
4. **Code your CAPTCHA widget implementation** – Implement the `renderCaptcha()` API call in your page, at the
   location where you want to use it. For information about configuring and using this
   function, see the following sections,
   [CAPTCHA JavaScript API
   specification](waf-js-captcha-api-specification.md "waf-js-captcha-api-specification.md") and
   [How to render
   the CAPTCHA puzzle](waf-js-captcha-api-render.md "waf-js-captcha-api-render.md").

The CAPTCHA implementation integrates with the intelligent threat integration APIs
for token management and to run
fetch calls that use the AWS WAF tokens. For guidance about using these APIs, see [Using the intelligent threat JavaScript API](waf-js-challenge-api.md "waf-js-challenge-api.md"). 5. **Add token verification in your protection pack (web ACL)** –
Add at least one rule to your protection pack (web ACL) that checks for a valid CAPTCHA
token in the web requests that your client sends. You can use the
CAPTCHA rule action to check, as described in [CAPTCHA and Challenge in
AWS WAF](waf-captcha-and-challenge.md "waf-captcha-and-challenge.md").

The protection pack (web ACL) additions verify that requests going to your protected endpoints include the
token that you've acquired in your client integration. Requests that include
a valid, unexpired CAPTCHA token pass the CAPTCHA rule action
inspection and do not present your end user with another CAPTCHA puzzle.
After you've implemented the JavaScript API, you can review the CloudWatch metrics for CAPTCHA puzzle attempts and solutions. For metrics and dimension details, see [Account metrics and dimensions](waf-metrics.md#waf-metrics-account "waf-metrics.md#waf-metrics-account").

###### Topics

- [CAPTCHA JavaScript API
  specification](waf-js-captcha-api-specification.md "waf-js-captcha-api-specification.md")
- [How to render
  the CAPTCHA puzzle](waf-js-captcha-api-render.md "waf-js-captcha-api-render.md")
- [Handling a CAPTCHA
  response from AWS WAF](waf-js-captcha-api-conditional.md "waf-js-captcha-api-conditional.md")
- [Managing API keys for the JS CAPTCHA API](waf-js-captcha-api-key.md "waf-js-captcha-api-key.md")
