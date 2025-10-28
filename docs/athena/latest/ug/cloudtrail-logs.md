# Query AWS CloudTrail logs

AWS CloudTrail is a service that records AWS API calls and events for Amazon Web Services accounts.

CloudTrail logs include details about any API calls made to your AWS services, including the
console. CloudTrail generates encrypted log files and stores them in Amazon S3. For more information,
see the [AWS CloudTrail
User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Note

If you want to perform SQL queries on CloudTrail event information across accounts, regions,
and dates, consider using CloudTrail Lake. CloudTrail Lake is an AWS alternative to creating
trails that aggregates information from an enterprise into a single, searchable event
data store. Instead of using Amazon S3 bucket storage, it stores events in a data lake, which
allows richer, faster queries. You can use it to create SQL queries that search events
across organizations, regions, and within custom time ranges. Because you perform CloudTrail
Lake queries within the CloudTrail console itself, using CloudTrail Lake does not require Athena. For
more information, see the [CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md")
documentation.

Using Athena with CloudTrail logs is a powerful way to enhance your analysis of AWS service
activity. For example, you can use queries to identify trends and further isolate activity
by attributes, such as source IP address or user.

A common application is to use CloudTrail logs to analyze operational activity for security and
compliance. For information about a detailed example, see the AWS Big Data Blog post,
[Analyze security, compliance, and operational activity using AWS CloudTrail and
Amazon Athena](https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/ "https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/").

You can use Athena to query these log files directly from Amazon S3, specifying the
`LOCATION` of log files. You can do this one of two ways:

- By creating tables for CloudTrail log files directly from the CloudTrail console.
- By manually creating tables for CloudTrail log files in the Athena console.

###### Topics

- [Understand CloudTrail logs and Athena
  tables](create-cloudtrail-table-understanding.md "create-cloudtrail-table-understanding.md")
- [Use the CloudTrail console to create an Athena
  table for CloudTrail logs](create-cloudtrail-table-ct.md "create-cloudtrail-table-ct.md")
- [Create a table for CloudTrail logs in Athena using
  manual partitioning](create-cloudtrail-table.md "create-cloudtrail-table.md")
- [Create a table for an
  organization wide trail using manual partitioning](create-cloudtrail-table-org-wide-trail.md "create-cloudtrail-table-org-wide-trail.md")
- [Create the table for CloudTrail
  logs in Athena using partition projection](create-cloudtrail-table-partition-projection.md "create-cloudtrail-table-partition-projection.md")
- [Example CloudTrail log queries](query-examples-cloudtrail-logs.md "query-examples-cloudtrail-logs.md")
