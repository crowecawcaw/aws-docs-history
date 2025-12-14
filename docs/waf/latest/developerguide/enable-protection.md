**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Enabling data protection

This section explains the data protection and log configuration options you can select from the console. You can protect data that appears in logs by enabling data protection on certain fields.
Data protection can be applied to transform sensitive information in various types of outputs, including full logs, sample requests, and Security Lake.

**To enable data protection in the AWS WAF console**

Navigate to the **protection packs (web ACLs)** page in the console to **enable protection settings**.
To enable data protection for your logs, choose whether to apply it to all logs or to a specific logging destination.
For information, see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").

###### Note

You don't need to enable logging to apply data protection on all logging.
Data protection will be applied across all output destinations, regardless of whether logging is enabled.

At the bottom of the **Enable protection settings** page,
select the **Add field** button on the **Data protection
fields** panel. Select the field type from the drop down menu. For
information about how each field's data is protected with data protection, see the
table below.

| Field type              | Details                                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Single header`         | Permanently transform the specified header key value according to the specified option (hashing or subsitution). The transformed value will also be reflected in full Logs. |
| `Body`                  | Permanently transforms the body value. Only applicable for `RuleMatchDetails` in the log.                                                                                   |
| `Query string`          | Permanently transform the query string according to the specified option (hashing or subsitution). The transformed value will also be reflected in full Logs.               |
| `Single query argument` | Permanently transform the specified query arg value according to the specified option (hashing or subsitution). The transformed value will also be reflected in full Logs.  |
| `Single cookie`         | Permanently transform the cookie value according to the specified option (hashing or subsitution). The transformed value will also be reflected in full Logs.               |
