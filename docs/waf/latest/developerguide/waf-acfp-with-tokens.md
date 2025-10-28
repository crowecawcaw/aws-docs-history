**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using application integration SDKs with ACFP

We highly recommend implementing the application integration SDKs, for the most efficient
use of the ACFP rule group.

- **Complete rule group functionality** –
  The ACFP rule `SignalClientHumanInteractivityAbsentLow` only works
  with tokens that are populated by the application integrations. This rule
  detects and manages abnormal human interactivity with the application page. The
  application integration SDKs can detect normal human interactivity through mouse
  movements, key presses, and other measurements. The interstitials that are sent
  by the rule actions CAPTCHA and Challenge can't provide this
  type of data.
- **Reduced latency** – The rule group rule
  `AllRequests` applies the Challenge rule action to any
  request that doesn't already have a challenge token. When this happens, the
  request is evaluated by the rule group twice: once without the token, and then a
  second time after the token is acquired by means of the Challenge action
  interstitial. You aren't charged any added fees for only using the
  `AllRequests` rule, but this approach adds overhead to your web
  traffic and adds latency to your end user experience. If you acquire the token
  client-side using the application integrations, before sending the account
  creation request, the ACFP rule group evaluates the request once.
  For more information about the rule group capabilities see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md").

For information about the SDKs, see [Client application
integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md"). For information about AWS WAF tokens,
see [Token use in AWS WAF intelligent threat mitigation](waf-tokens.md "waf-tokens.md"). For information about the
rule actions, see [CAPTCHA and Challenge in
AWS WAF](waf-captcha-and-challenge.md "waf-captcha-and-challenge.md").
