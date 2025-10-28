**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Logging for an AWS WAF policy

You can enable centralized logging for your AWS WAF policies to get detailed information about traffic that's
analyzed by your web ACL within your organization. AWS Firewall Manager supports this option for AWS WAFV2, not for AWS WAF Classic.

The information in the logs includes the time that AWS WAF received the request from your protected AWS resource,
detailed information about the request, and the action for the rule that each request matched from all in-scope accounts.
For information about AWS WAF logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md") in the _AWS WAF Developer Guide_.

You can send your logs to an Amazon Data Firehose data stream or Amazon Simple Storage Service (S3) bucket. Each destination type requires
some additional configuration in order for Firewall Manager to be able to manage the AWS WAF logging across your in-scope resources and accounts. The
sections that follow provide details.

If the policy has web ACL retrofitting enabled, Firewall Manager doesn't override any logging configuration that's in place in
existing web ACLs. For information about retrofitting,
see the web ACL source configuration information at [Web ACL management for AWS WAF policies](how-fms-manages-web-acls.md "how-fms-manages-web-acls.md").

###### Note

Only modify or disable logging for Firewall Manager policies through the Firewall Manager interface. If you use AWS WAF to update or delete
the logging configuration of a web ACL that's managed by Firewall Manager, Firewall Manager won't detect the change automatically.
If you have used AWS WAF, you can manually prompt an update to the Firewall Manager AWS WAF policy by re-evaluating the policy's
rule in AWS Config. To do this, in the AWS Config console, locate the AWS Config rule for the Firewall Manager policy and select the re-evaluate action.

###### Topics

- [Logging destinations](waf-policies-logging-destinations.md "waf-policies-logging-destinations.md")
- [Enabling logging for an AWS WAF policy in Firewall Manager](waf-policies-enabling-logging.md "waf-policies-enabling-logging.md")
- [Disabling logging for an AWS WAF policy in Firewall Manager](waf-policies-disabling-logging.md "waf-policies-disabling-logging.md")
