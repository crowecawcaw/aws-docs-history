**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Enabling logging for an AWS WAF policy in Firewall Manager

The following procedure describes how to enable logging for an AWS WAF policy in the Firewall Manager console.

###### To enable logging for an AWS WAF policy

1. Before you can enable logging, you must configure your logging destination resources as the following:
   - **Amazon Kinesis Data Streams** - Create an Amazon Data Firehose using your Firewall Manager administrator account. Use a name starting with the prefix `aws-waf-logs-`. For example, `aws-waf-logs-firewall-manager-central`.
     Create the data firehose with a `PUT` source and in the Region that you
     are operating. If you are capturing logs for Amazon CloudFront, create the firehose in
     US East (N. Virginia).
     Before you use it, test your delivery stream to be sure that it has enough throughput to accommodate your organization's logs.
     For more information, see
     [Creating
     an Amazon Data Firehose delivery stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").
   - **Amazon Simple Storage Service buckets** - Create an Amazon S3 bucket according to the guidelines in the [Amazon Simple Storage Service](logging-s3.md "logging-s3.md") topic in the _AWS WAF Developer Guide_. You must also configure your Amazon S3 bucket with the permissions listed in [Permissions to publish logs to an Amazon S3 bucket](waf-policies-logging-destinations.md#waf-policies-logging-s3-permissions "waf-policies-logging-destinations.md#waf-policies-logging-s3-permissions") .

2. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 3. In the navigation pane, choose **Security Policies**. 4. Choose the AWS WAF policy that you want to enable logging for. For more information about AWS WAF
logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md"). 5. On the **Policy details** tab, in the **Policy rules** section, choose **Edit**. 6. For **Logging configuration**, choose **Enable logging** to turn on logging.
Logging provides detailed information about traffic that is analyzed by your web ACL.
Choose the **Logging destination**, and then choose the logging destination that you configured.
You must choose a logging destination whose name begins with `aws-waf-logs-`.
For information about configuring an AWS WAF logging destination, see [Using AWS WAF policies with Firewall Manager](waf-policies.md "waf-policies.md"). 7. (Optional) If you don't want certain fields and their values included in the logs, redact
those fields. Choose the field to redact, and then choose **Add**.
Repeat as necessary to redact additional fields. The redacted fields appear as
`REDACTED` in the logs. For example, if you redact the
**URI** field, the **URI** field in the
logs will be `REDACTED`. 8. (Optional) If you don't want to send all requests to the logs, add your filtering criteria
and behavior. Under **Filter logs**, for each filter that you
want to apply, choose **Add filter**, then choose your
filtering criteria and specify whether you want to keep or drop requests that
match the criteria. When you finish adding filters, if needed, modify the
**Default logging behavior**. For more information, see [Finding your protection pack (web ACL) records](logging-management.md "logging-management.md") in the _AWS WAF Developer Guide_. 9. Choose **Next**. 10. Review your settings, then choose **Save** to save your changes to the policy.
