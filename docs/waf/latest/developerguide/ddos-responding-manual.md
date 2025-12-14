**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Manually mitigating an application layer DDoS attack

This page provides instructions for manually mitigating an application layer DDoS attack.

If you determine that the activity in the events page for your resource represents a DDoS
attack, you can create your own AWS WAF rules in your web ACL to mitigate the attack. This
is the only option available if you aren't a Shield Advanced customer. AWS WAF is included with AWS Shield Advanced at no additional cost.
For information about
creating rules in your web ACL, see [Configuring protection in AWS WAF](web-acl.md "web-acl.md").

If you use AWS Firewall Manager, you can add your AWS WAF rules to a Firewall Manager AWS WAF policy.

###### To manually mitigate a potential

application layer DDoS attack

1. Create rule statements in your web ACL with criteria that matches the unusual behavior. To
   start with, configure them to count matching requests. For information about
   configuring your web ACL and rule statements, see [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md") and [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Always test your rules first by initially using the rule action Count instead of
Block. After you're comfortable that your new rules are identifying
the correct requests, you can modify them to block the requests. 2. Monitor the request counts to determine whether you want to block the matching
requests. If the volume of requests continues to be unusually high and you're
confident that your rules are capturing the requests that are causing the high
volume, change the rules in your web ACL to block the
requests. 3. Continue monitoring the events page to ensure that your traffic is being handled as you want it to
be.
AWS provides preconfigured templates to get you started quickly. The templates include a
set of AWS WAF rules that you can customize and use to block common web-based attacks. For
more information, see [AWS WAF Security Automations](https://aws.amazon.com/solutions/aws-waf-security-automations/ "https://aws.amazon.com/solutions/aws-waf-security-automations/").
