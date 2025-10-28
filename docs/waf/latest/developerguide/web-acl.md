**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Configuring protection in AWS WAF

This page explains what protection packs (web ACLs) are and how they work.

A protection pack (web ACL) gives you fine-grained control over all of the HTTP(S) web requests that
your protected resource responds to. You can protect Amazon CloudFront, Amazon API Gateway, Application Load Balancer, AWS AppSync, Amazon Cognito, AWS App Runner, AWS Amplify, and AWS Verified Access resources.

You can use criteria like the following to allow or block requests:

- IP address origin of the request
- Country of origin of the request
- String match or regular expression (regex) match in a part of the request
- Size of a particular part of the request
- Detection of malicious SQL code or scripting
  You can also test for any combination of these conditions. You can block or count web
  requests that not only meet the specified conditions, but also exceed a specified number of
  requests in a single minute. You can combine conditions using logical operators.
  You can also run CAPTCHA puzzles and silent client session challenges against requests.

You provide your matching criteria and the action to take on matches in AWS WAF rule statements. You can
define rule statements directly inside your protection pack (web ACL) and in reusable rule
groups that you use in your protection pack (web ACL). For a full list of
the options, see [Using rule statements in AWS WAF](waf-rule-statements.md "waf-rule-statements.md") and
[Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

When you create a protection pack (web ACL), you specify the types of resources that you want to use it with.
For information, see [Creating a protection pack (web ACL) in AWS WAF](web-acl-creating.md "web-acl-creating.md").
After you define a protection pack (web ACL), you can associate it with your
resources to begin providing protection for them. For more information,
see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md").

###### Note

On some occasions, AWS WAF might encounter an internal error that delays the response to
associated AWS resources about whether to allow or block a request. On those
occasions, CloudFront typically allows the request or serves the content, while the Regional
services typically deny the request and don't serve the content.

###### Production traffic risk

Before you deploy changes in your protection pack (web ACL) for production traffic, test and tune
them in a staging or testing environment until you are comfortable with the
potential impact to your traffic. Then test and tune your updated rules in count
mode with your production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

###### Topics

- [Creating a protection pack (web ACL) in AWS WAF](web-acl-creating.md "web-acl-creating.md")
- [Editing a protection pack (web ACL) in AWS WAF](web-acl-editing.md "web-acl-editing.md")
- [Managing rule group behavior](web-acl-rule-group-settings.md "web-acl-rule-group-settings.md")
- [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md")
- [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md")
- [Setting the protection pack (web ACL) default action in AWS WAF](web-acl-default-action.md "web-acl-default-action.md")
- [Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md "web-acl-setting-body-inspection-limit.md")
- [Configuring CAPTCHA, challenge, and tokens in AWS WAF](web-acl-captcha-challenge-token-domains.md "web-acl-captcha-challenge-token-domains.md")
- [Viewing web traffic metrics in AWS WAF](web-acl-working-with.md "web-acl-working-with.md")
- [Deleting a protection pack (web ACL)](web-acl-deleting.md "web-acl-deleting.md")
