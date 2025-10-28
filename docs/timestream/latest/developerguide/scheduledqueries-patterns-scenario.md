For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Scenario

The following examples use a DevOps monitoring scenario which is outlined in [Scheduled queries sample
schema](scheduledqueries-common-schema-example.md "scheduledqueries-common-schema-example.md").

The examples provide the scheduled query definition where you can plug in the
appropriate configurations for where to receive execution status notifications for
scheduled queries, where to receive reports for errors encountered during execution
of a scheduled query, and the IAM role the scheduled query uses to perform its
operations.

You can create these scheduled queries after filling in the preceding options,
[creating
the target](code-samples.md "code-samples.md") (or derived) table, and executing the through the AWS CLI.
For example, assume that a scheduled query definition is stored in a file,
`scheduled_query_example.json`. You can create the query using the
CLI command.

```
aws timestream-query create-scheduled-query --cli-input-json  file://scheduled_query_example.json --profile aws_profile --region us-east-1
```

In the preceding command, the profile passed using the --profile option must have
the appropriate permissions to create scheduled queries. See [Identity-based policies for Scheduled Queries](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-sheduledqueries "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-sheduledqueries") for detailed instructions
for the policies and permissions.
