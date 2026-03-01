# Logging that requires additional permissions [V1]

Some AWS services use a common infrastructure to send their logs to CloudWatch Logs, Amazon S3, or
Firehose. To enable the AWS services listed in the preceding table to send their logs to
these destinations, you must be logged in as a user that has certain permissions.

Additionally, permissions must be granted to AWS to enable the logs to be sent.
AWS can automatically create those permissions when the logs are set up, or you can
create them yourself first before you set up the logging. For cross-account delivery,
you must manually create the permission policies yourself.

If you choose to have AWS automatically set up the necessary permissions and
resource policies when you or someone in your organization first sets up the sending of
logs, then the user who is setting up the sending of logs must have certain permissions,
as explained later in this section. Alternatively, you can create the resource policies
yourself, and then the users who set up the sending of logs do not need as many
permissions.

The following topics provide more details for each of these destinations.

###### Topics

- [Logs sent to CloudWatch Logs](AWS-logs-infrastructure-CWL.md "AWS-logs-infrastructure-CWL.md")
- [Logs sent to Amazon S3](AWS-logs-infrastructure-S3.md "AWS-logs-infrastructure-S3.md")
- [Logs sent to Firehose](AWS-logs-infrastructure-Firehose.md "AWS-logs-infrastructure-Firehose.md")
