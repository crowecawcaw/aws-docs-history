# Query AWS WAF logs

AWS WAF is a web application firewall that lets you monitor and control the HTTP and
HTTPS requests that your protected web applications receive from clients. You define how to
handle the web requests by configuring rules inside an AWS WAF web access control list (ACL).
You then protect a web application by associating a web ACL to it. Examples of web
application resources that you can protect with AWS WAF include Amazon CloudFront distributions,
Amazon API Gateway REST APIs, and Application Load Balancers. For more information about AWS WAF, see [AWS WAF](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md")
in the _AWS WAF developer guide_.

AWS WAF logs include information about the traffic that is analyzed by your web ACL,
such as the time that AWS WAF received the request from your AWS resource, detailed
information about the request, and the action for the rule that each request matched.

You can configure an AWS WAF web ACL to publish logs to one of several destinations, where
you can query and view them. For more information about configuring web ACL logging and the
contents of the AWS WAF logs, see [Logging AWS WAF web ACL traffic](../../../waf/latest/developerguide/logging.md "../../../waf/latest/developerguide/logging.md")
in the _AWS WAF developer guide_.

For information on how to use Athena to analyze AWS WAF logs for insights into threat
detection and potential security attacks, see the AWS Networking & Content Delivery
Blog post [How to use Amazon Athena queries to analyze AWS WAF logs and provide the visibility
needed for threat detection](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-use-amazon-athena-queries-to-analyze-aws-waf-logs-and-provide-the-visibility-needed-for-threat-detection/ "https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-use-amazon-athena-queries-to-analyze-aws-waf-logs-and-provide-the-visibility-needed-for-threat-detection/").

For an example of how to aggregate AWS WAF logs into a central data lake repository and
query them with Athena, see the AWS Big Data Blog post [Analyzing AWS WAF logs with OpenSearch Service, Amazon Athena, and Quick](https://aws.amazon.com/blogs/big-data/analyzing-aws-waf-logs-with-amazon-es-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/big-data/analyzing-aws-waf-logs-with-amazon-es-amazon-athena-and-amazon-quicksight/").

This topic provides example `CREATE TABLE` statements for partition projection,
manual partitioning, and one that does not uses any partitioning.

###### Note

The `CREATE TABLE` statements in this topic can be used for both v1 and v2
AWS WAF logs. In v1, the `webaclid` field contains an ID. In v2, the
`webaclid` field contains a full ARN. The `CREATE TABLE`
statements here treat this content agnostically by using the `string` data
type.

###### Topics

- [Create a table for AWS WAF S3 logs in Athena using partition projection](create-waf-table-partition-projection.md "create-waf-table-partition-projection.md")
- [Create a table for AWS WAF S3 logs in Athena using manual partition](create-waf-table-manual-partition.md "create-waf-table-manual-partition.md")
- [Create a table for AWS WAF logs without partitioning](create-waf-table.md "create-waf-table.md")
- [Example queries for AWS WAF logs](query-examples-waf-logs.md "query-examples-waf-logs.md")
