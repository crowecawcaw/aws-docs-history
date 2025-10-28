# Log and monitor Athena

To detect incidents, receive alerts when incidents occur, and respond to them, use these
options with Amazon Athena:

- Monitor Athena with AWS CloudTrail – [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") provides a record of actions taken by a
  user, role, or an AWS service in Athena. It captures calls from the Athena console
  and code calls to the Athena API operations as events. This allow you to determine
  the request that was made to Athena, the IP address from which the request was made,
  who made the request, when it was made, and additional details. For more
  information, see [Log Amazon Athena API calls with AWS CloudTrail](monitor-with-cloudtrail.md "monitor-with-cloudtrail.md").

You can also use Athena to query the CloudTrail log files not only for Athena, but for
other AWS services. For more information, see [Query AWS CloudTrail logs](cloudtrail-logs.md "cloudtrail-logs.md").

- Monitor Athena usage with CloudTrail and Amazon Quick Suite –
  [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") is a fully managed,
  cloud-powered business intelligence service that lets you create interactive
  dashboards your organization can access from any device. For an example of a
  solution that uses CloudTrail and Amazon Quick Suite to monitor Athena usage, see the AWS Big Data
  blog post [How Realtor.com monitors Amazon Athena usage with AWS CloudTrail and Quick Suite](https://aws.amazon.com/blogs/big-data/analyzing-amazon-athena-usage-by-teams-within-a-real-estate-company/ "https://aws.amazon.com/blogs/big-data/analyzing-amazon-athena-usage-by-teams-within-a-real-estate-company/").
- Use EventBridge with Athena – Amazon EventBridge delivers a
  near real-time stream of system events that describe changes in AWS resources.
  EventBridge becomes aware of operational changes as they occur, responds to them, and takes
  corrective action as necessary, by sending messages to respond to the environment,
  activating functions, making changes, and capturing state information. Events are
  emitted on a best effort basis. For more information, see [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the
  _Amazon EventBridge User Guide_.
- Use workgroups to separate users, teams, applications, or
  workloads, and to set query limits and control query costs – You
  can view query-related metrics in Amazon CloudWatch, control query costs by configuring
  limits on the amount of data scanned, create thresholds, and trigger actions, such
  as Amazon SNS alarms, when these thresholds are breached. For more information, see [Use workgroups to control query
  access and costs](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md"). Use
  resource-level IAM permissions to control access to a specific workgroup. For more
  information, see [Use IAM policies to control workgroup
  access](workgroups-iam-policy.md "workgroups-iam-policy.md") and [Use CloudWatch and EventBridge to monitor queries and control
  costs](workgroups-control-limits.md "workgroups-control-limits.md").

###### Topics

- [Log Amazon Athena API calls with AWS CloudTrail](monitor-with-cloudtrail.md "monitor-with-cloudtrail.md")
