**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using the intelligent threat JavaScript API

This section provides instructions for using the intelligent threat JavaScript API in your client application.

The intelligent threat APIs provide operations for running silent challenges against the user's browser,
and for handling the AWS WAF tokens that provide proof of successful challenge and CAPTCHA responses.

Implement the JavaScript integration first in a test environment, then in
production. For additional coding guidance, see the sections that follow.

###### To use the intelligent threat APIs

1. **Install the APIs**

If you use the CAPTCHA API, you can skip this step.
When you install the CAPTCHA API, the script automatically
installs the intelligent threat APIs.

    1. Sign in to the AWS Management Console and open the AWS WAF console at
    [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
    2. In the navigation pane, choose **Application integration**. On the
     **Application integration** page, you can see tabbed
     options.
    3. Select **Intelligent threat integration**
    4. In the tab, select the protection pack (web ACL) that you want to integrate with.
     The protection pack (web ACL) list includes only protection packs (web ACLs) that use the `AWSManagedRulesACFPRuleSet`
     managed rule group, the `AWSManagedRulesATPRuleSet`
     managed rule group, or the targeted protection level of the
     `AWSManagedRulesBotControlRuleSet` managed rule group.
    5. Open the **JavaScript SDK** pane, and copy the
     script tag for use in your integration.
    6. In your application page code, in the `<head>` section, insert
     the script tag that you copied for the protection pack (web ACL). This inclusion causes your client application to
     automatically retrieve a token in the background on page load.



    ```
    <head>
        <script type="text/javascript" src="`protection pack (web ACL) integration URL`/challenge.js” defer></script>
    <head>
    ```

    This `<script>` listing is configured with the `defer`
     attribute, but you can change the setting to `async` if you want
     a different behavior for your page.

2. **(Optional) Add domain configuration for the client's
   tokens** – By default, when AWS WAF creates a token, it
   uses the host domain of the resource that’s associated with the protection pack (web ACL). To
   provide additional domains for the JavaScript APIs, follow the guidance at
   [Providing domains for use in the
   tokens](waf-js-challenge-api-set-token-domain.md "waf-js-challenge-api-set-token-domain.md").
3. **Code your intelligent threat integration** – Write
   your code to ensure that token retrieval completes before the client sends
   its requests to your protected endpoints. If you are already using the
   `fetch` API to make your call, you can substitute the AWS WAF
   integration `fetch` wrapper. If you don't use the
   `fetch` API, you can use the AWS WAF integration
   `getToken` operation instead. For coding guidance, see the
   following sections.
4. **Add token verification in your protection pack (web ACL)** – Add at least one rule to your protection pack (web ACL) that checks for a valid challenge token in the
   web requests that your client sends. You can use rule groups that check and
   monitor challenge tokens, like the targeted level of the Bot Control managed rule group,
   and you can use
   the Challenge rule action to check, as
   described in [CAPTCHA and Challenge in
   AWS WAF](waf-captcha-and-challenge.md "waf-captcha-and-challenge.md").

The protection pack (web ACL) additions verify that requests to your protected endpoints include the
token that you've acquired in your client integration. Requests that include
a valid, unexpired token pass the Challenge
inspection and do not send another silent challenge to your client. 5. **(Optional) Block requests that are missing tokens** –
If you use the APIs with the ACFP managed rule group, the ATP managed rule group, or the
targeted rules of the Bot Control rule group, these rules don't block requests
that are missing tokens. To block requests that are missing tokens, follow
the guidance at [Blocking requests that don't have a valid
AWS WAF token](waf-tokens-block-missing-tokens.md "waf-tokens-block-missing-tokens.md").

###### Topics

- [Intelligent threat API
  specification](waf-js-challenge-api-specification.md "waf-js-challenge-api-specification.md")
- [How to use the integration fetch wrapper](waf-js-challenge-api-fetch-wrapper.md "waf-js-challenge-api-fetch-wrapper.md")
- [How to use
  the integration getToken](waf-js-challenge-api-get-token.md "waf-js-challenge-api-get-token.md")
