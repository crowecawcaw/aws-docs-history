

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds supports for AWS WAF web ACLs on February 23, 2023
<a name="release-2023-02-23-waf"></a>

AWS App Runner now supports using web ACLs created in AWS WAF.

**Release date:** February 23, 2023

## Changes
<a name="release-2023-02-23-waf.changes"></a>

AWS App Runner now supports web access control lists (Web ACLs) created in AWS WAF. AWS WAF is a web application firewall that helps you monitor and control the web requests reaching your web applications. 

Use AWS WAF web ACLs to define rules that dictate how incoming web requests are handled. This integration provides enhanced security to your web applications and APIs on App Runner, protecting them from common web exploits and unwanted bots. 

After you create a web ACL in AWS WAF, you can associate it with your App Runner service when creating or updating your service. For more information, see [Associating an AWS WAF web ACL with your service](https://docs.aws.amazon.com/apprunner/latest/dg/waf.html) in the *AWS App Runner Developer Guide*. 

App Runner doesn't charge you extra for using AWS WAF web ACLs. You pay standard AWS WAF pricing. For more information about pricing, see  [AWS WAF Pricing](https://aws.amazon.com/waf/pricing). 