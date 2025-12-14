**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Configuring logging for a protection pack (web ACL)

This section provides instructions for configuring data protection for a protection pack (web ACL).

###### Note

You are charged for logging in addition to the charges for using AWS WAF.
For information, see [Pricing for logging protection pack (web ACL) traffic information](logging-pricing.md "logging-pricing.md").

To enable logging for a protection pack (web ACL), you must have already configured the logging destination that you're
going to use. For information about
your destination choices and the requirements for each, see [AWS WAF logging destinations](logging-destinations.md "logging-destinations.md").

###### To configure logging for a protection pack (web ACL)

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **protection packs (web ACLs)**.
3. Choose the name of the protection pack (web ACL) that you want to enable logging for. The console takes you to the protection pack (web ACL)'s description, where you can edit it.
4. On the **Logging and metrics** tab, choose **Enable logging**.
5. Choose the logging destination type, and then choose the logging destination that you
   configured. You must choose a logging destination whose name begins with
   `aws-waf-logs-`.
6. (Optional) If you don't want some fields included in the logs, redact
   them. Choose the field to redact, and then choose
   **Add**. Repeat as necessary to redact additional fields. Redacted fields appear in the logs as `xxx`.

###### Note

This setting has no impact on request sampling. You can exclude fields from request sampling
by configuring protection pack (web ACL) data protection or by disabling sampling for the protection pack (web ACL). 7. (Optional) If you don't want to send all requests to the logs, add your filtering criteria
and behavior. Under **Filter logs**, for each filter that you
want to apply, choose **Add filter**, then choose your
filtering criteria and specify whether you want to keep or drop requests that
match the criteria. When you finish adding filters, if needed, modify the
**Default logging behavior**.

###### Note

If you add multiple filters, AWS WAF evaluates them starting from the
top. 8. Choose **Enable logging**.

###### Note

When you successfully enable logging, AWS WAF will create a service-linked role with the
necessary permissions to write logs to the logging destination. For more
information, see [Using service-linked roles for AWS WAF](using-service-linked-roles.md "using-service-linked-roles.md").
