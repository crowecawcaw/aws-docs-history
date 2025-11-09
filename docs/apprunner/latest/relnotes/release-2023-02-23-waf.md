# Release: App Runner adds supports for AWS WAF web ACLs on February 23, 2023

AWS App Runner now supports using web ACLs created in AWS WAF.

**Release date:** February 23, 2023

## Changes

AWS App Runner now supports web access control lists (Web ACLs) created in AWS WAF. AWS WAF is a web application firewall that helps you monitor and control the
web requests reaching your web applications.

Use AWS WAF web ACLs to define rules that dictate how incoming web requests are handled. This integration
provides enhanced security to your web applications and APIs on App Runner, protecting them from common web exploits and unwanted bots.

After you create a web ACL in AWS WAF, you can associate it with your App Runner service when creating or updating your service. For more information, see
[Associating an AWS WAF web ACL with your service](../dg/waf.md "../dg/waf.md") in the _AWS App Runner Developer Guide_.

App Runner doesn't charge you extra for using AWS WAF web ACLs. You pay standard AWS WAF pricing. For more information about pricing, see  [AWS WAF Pricing](https://aws.amazon.com/waf/pricing "https://aws.amazon.com/waf/pricing").
