**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How the AWS WAFCAPTCHA and Challenge rule actions work

This section explains how CAPTCHA and Challenge work.

AWS WAF CAPTCHA and Challenge are standard rule actions, so they're
relatively easy to implement. To use either of them, you create the inspection criteria
for your rule that identifies the requests that you want to inspect, and then specify
one of the two rule actions. For general information about rule action options, see
[Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

In addition to implementing silent challenges and CAPTCHA puzzles from the server side,
you can integrate silent challenges in your JavaScript and iOS and Android client
applications, and you can render CAPTCHA puzzles in your JavaScript clients. These
integrations allow you to provide your end users with better performance and CAPTCHA
puzzle experiences, and they can reduce costs associated with using the rule actions and
the intelligent threat mitigation rule groups. For more information about these options,
see [Client application
integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md"). For pricing information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Topics

- [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md "waf-captcha-and-challenge-actions.md")
- [CAPTCHA and Challenge actions in the logs and metrics](waf-captcha-and-challenge-logs-metrics.md "waf-captcha-and-challenge-logs-metrics.md")
