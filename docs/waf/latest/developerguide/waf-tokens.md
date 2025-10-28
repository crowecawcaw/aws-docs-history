**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Token use in AWS WAF intelligent threat mitigation

This section explains what AWS WAF tokens do.

AWS WAF tokens are an integral part of the enhanced protections offered by AWS WAF intelligent threat mitigation. A
token, sometimes called a fingerprint, is a collection of information about a single client
session that the client stores and provides with every web request that it sends. AWS WAF uses tokens to
identify and separate malicious client sessions from legitimate sessions, even when both
originate from a single IP address. Token use imposes costs that are negligible for
legitimate users, but expensive at scale for botnets.

AWS WAF uses tokens to support its browser and end user challenge functionality, which is
provided by the application integration SDKs and by the rule actions Challenge and
CAPTCHA. Additionally, tokens enable features of the AWS WAF Bot Control and account takeover
prevention managed rule groups.

AWS WAF creates, updates, and encrypts tokens for clients that successfully respond to
silent challenges and CAPTCHA puzzles. When a client with a token sends a web request, it
includes the encrypted token, and AWS WAF decrypts the token and verifies its contents.

###### Topics

- [How AWS WAF uses tokens](waf-tokens-usage.md "waf-tokens-usage.md")
- [AWS WAF token characteristics](waf-tokens-details.md "waf-tokens-details.md")
- [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md")
- [Specifying token domains and domain lists in AWS WAF](waf-tokens-domains.md "waf-tokens-domains.md")
- [Types of token labels in AWS WAF](waf-tokens-labeling.md "waf-tokens-labeling.md")
- [Blocking requests that don't have a valid
  AWS WAF token](waf-tokens-block-missing-tokens.md "waf-tokens-block-missing-tokens.md")
- [Required configuration for Application Load Balancers that are CloudFront origins](waf-tokens-with-alb-and-cf.md "waf-tokens-with-alb-and-cf.md")
