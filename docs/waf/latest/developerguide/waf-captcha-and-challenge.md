**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# CAPTCHA and Challenge in

AWS WAF

This section explains how CAPTCHA and Challenge work with AWS WAF.

You can configure your AWS WAF rules to run a CAPTCHA or Challenge action
against web requests that match your rule's inspection criteria. You can also program your JavaScript
client applications to run CAPTCHA puzzles and browser challenges locally.

CAPTCHA puzzles and silent
challenges can only run when browsers are accessing HTTPS endpoints. Browser
clients must be running in secure contexts in order to acquire tokens.

- **CAPTCHA** – Requires the end user to solve a CAPTCHA puzzle to prove that a human
  being is sending the request. CAPTCHA puzzles are intended to be fairly easy and quick for humans to complete
  successfully and hard for computers to either complete successfully or to randomly
  complete with any meaningful rate of success.

In protection pack (web ACL) rules, CAPTCHA is commonly used when a Block
action would stop too many legitimate requests, but letting all traffic through would
result in unacceptably high levels of unwanted requests, such as from bots. For information about
the rule action behavior, see [How the AWS WAFCAPTCHA and Challenge rule actions work](waf-captcha-and-challenge-how-it-works.md "waf-captcha-and-challenge-how-it-works.md").

You can also program a CAPTCHA puzzle implementation in your
client application integration APIs. When you do this, you can customize the behavior and
placement of the puzzle in your client application. For more
information, see [Client application
integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").

- **Challenge** – Runs a silent challenge that requires the client session to verify that
  it's a browser, and not a bot. The verification runs in the background without
  involving the end user. This is a good option for verifying clients that you suspect
  of being invalid without negatively impacting the end user experience with a
  CAPTCHA puzzle. For information about
  the rule action behavior, see [How the AWS WAFCAPTCHA and Challenge rule actions work](waf-captcha-and-challenge-how-it-works.md "waf-captcha-and-challenge-how-it-works.md").

The Challenge rule action is similar to the challenge run by the
client intelligent threat integration APIs, described at [Client application
integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").

###### Note

You are charged additional fees when you use the CAPTCHA or Challenge rule action in one of your rules or as a rule action override in a rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

For descriptions of all of the rule action options, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

###### Topics

- [AWS WAF CAPTCHA puzzles](waf-captcha-puzzle.md "waf-captcha-puzzle.md")
- [How the AWS WAFCAPTCHA and Challenge rule actions work](waf-captcha-and-challenge-how-it-works.md "waf-captcha-and-challenge-how-it-works.md")
- [Best practices for using the
  CAPTCHA and Challenge actions](waf-captcha-and-challenge-best-practices.md "waf-captcha-and-challenge-best-practices.md")
