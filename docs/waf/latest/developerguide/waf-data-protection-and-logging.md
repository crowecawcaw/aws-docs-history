**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Data protection and logging for AWS WAF protection pack (web ACL) traffic

This section explains the data logging, collection, and protection options that you can use with AWS WAF. The options are the following:

- **Logging** – You can configure your protection pack (web ACL) to send logs for
  web request traffic to a logging destination of your choice. You can configure field redaction and filtering for this choice.
  Logging uses the data that's available after any data protection setting are applied.

For information about this option, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").

- **Request sampling** – You can configure your protection pack (web ACL) to sample the web requests
  that it evaluates, to get an idea of the type of traffic that your application is receiving.
  Request sampling uses the data that's available after any data protection settings are applied.

For information about this option, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

- **Amazon Security Lake** – You can configure Security Lake to collect protection pack (web ACL) data.
  Security Lake collects log and event data from various AWS sources for normalization, analysis, and management.
  Security Lake collects from the data that's available after any data protection settings are applied.

For information about this option,
see [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md")
and [Collecting data from AWS services](../../../security-lake/latest/userguide/internal-sources.md "../../../security-lake/latest/userguide/internal-sources.md")
in the _Amazon Security Lake user guide_.

AWS WAF doesn't charge you for using this option. For pricing information, see [Security Lake Pricing](https://aws.amazon.com/security-lake/pricing/ "https://aws.amazon.com/security-lake/pricing/") and
[How Security Lake pricing is determined](../../../security-lake/latest/userguide/estimating-costs.md "../../../security-lake/latest/userguide/estimating-costs.md") in the _Amazon Security Lake user guide_.

- **Data protection** – You can configure data protections for web traffic data at two levels:
  - **Data protection for the protection pack (web ACL)** – You can configure data protection for each protection pack (web ACL), which enables you to substitute certain web traffic data with static strings or cryptographic hashing. Data protection at this level can be configured centrally, and applies across all logging and data collection options.

  For information about this option, see [Data protection](data-protection-masking.md "data-protection-masking.md").
  - **Logging redaction and filtering** – For logging only, you can configure
    some of the web traffic data for redaction from the logs, and you can filter the data that you log. This option is in addition to any data protection setting you've configured, and it only affects the data that AWS WAF sends to the configured logging destination.

###### Topics

- [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md")
- [Data protection](data-protection-masking.md "data-protection-masking.md")
