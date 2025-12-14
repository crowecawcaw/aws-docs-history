**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Client application

integrations in AWS WAF

This section explains how to use the intelligent threat integration APIs and JavaScript CAPTCHA
integration API with your AWS WAF features.

Use AWS WAF client application integration APIs to couple client-side protections with your
AWS server-side protection pack (web ACL) protections, to help verify that the client applications that send
web requests to your protected resources are the intended clients and that your end users are
human beings.

Use the client integrations to manage silent browser challenges and CAPTCHA puzzles, obtain tokens
with proof of successful browser and end user responses, and to include these tokens in requests to your
protected endpoints. For general information about AWS WAF tokens, see
[Token use in AWS WAF intelligent threat mitigation](waf-tokens.md "waf-tokens.md").

Combine your client integrations with protection pack (web ACL) protections that require valid tokens for access
to your resources. You
can use rule groups that check and monitor challenge tokens, like the ones listed in the
next section, at [Intelligent threat integration and
AWS Managed Rules](waf-application-integration-with-AMRs.md "waf-application-integration-with-AMRs.md"), and you can use the
CAPTCHA and Challenge rule actions to check, as described in [CAPTCHA and Challenge in
AWS WAF](waf-captcha-and-challenge.md "waf-captcha-and-challenge.md").

AWS WAF provides two levels of integration for JavaScript applications, and one for mobile
applications:

- **Intelligent threat integration** – Verify the client
  application and provide AWS token acquisition and management. This is similar to
  the functionality provided by the AWS WAF Challenge rule action. This
  functionality fully integrates your client application with the `AWSManagedRulesACFPRuleSet` managed
  rule group, the `AWSManagedRulesATPRuleSet` managed
  rule group, and the targeted protection level of the `AWSManagedRulesBotControlRuleSet` managed rule group.

The intelligent threat integration APIs use the AWS WAF silent browser challenge to help
ensure that login attempts and other calls to your protected resource are only
allowed after the client has acquired a valid token. The APIs manage token
authorization for your client application sessions and gather information about the
client to help determine whether it's being operated by a bot or by a human being.

###### Note

This is available for JavaScript and for Android and iOS mobile applications.

- **CAPTCHA integration** – Verify end users with
  customized CAPTCHA puzzle that you manage in your application. This is similar to the
  functionality provided by the AWS WAF CAPTCHA rule action, but with added control
  over the puzzle placement and behavior.

This integration
leverages the JavaScript intelligent threat integration to run silent challenges and
provide AWS WAF tokens to the customer's page.

###### Note

This is available for JavaScript applications.

###### Topics

- [Intelligent threat integration and
  AWS Managed Rules](waf-application-integration-with-AMRs.md "waf-application-integration-with-AMRs.md")
- [Accessing the AWS WAF client application integration APIs](waf-application-integration-location-in-console.md "waf-application-integration-location-in-console.md")
- [AWS WAF JavaScript integrations](waf-javascript-api.md "waf-javascript-api.md")
- [AWS WAF mobile application integration](waf-mobile-sdk.md "waf-mobile-sdk.md")
