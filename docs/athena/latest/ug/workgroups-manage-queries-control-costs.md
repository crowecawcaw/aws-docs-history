# Use workgroups to control query access and costs

You can use Athena workgroups to separate workloads, control team access, enforce
configuration, and track query metrics and control costs.

###### Separate your workloads

You can use workgroups to separate workloads. For example, you can create two
independent workgroups, one for automated scheduled applications, such as report
generation, and another for ad-hoc usage by analysts.

###### Control access by teams

Because workgroups act as IAM resources, you can use resource-level identity-based
policies to control who can access a workgroup and run queries in it. To isolate queries
for two different teams in your organization, you can create a separate workgroup for
each team. Each workgroup has its own query history and a list of saved queries for the
queries in that workgroup, and not for all queries in the account. For more information,
see [Use IAM policies to control workgroup access](workgroups-iam-policy.md "workgroups-iam-policy.md").

###### Enforce configuration

You can optionally enforce the same workgroup-wide settings for all queries that run
in the workgroup. These settings include query results location in Amazon S3, expected bucket
owner, encryption, and control of objects written to the query results bucket. For more
information, see [Override client-side settings](workgroups-settings-override.md "workgroups-settings-override.md").

###### Track query metrics, query events, and control costs

To track query metrics, query events, and control costs for each Athena workgroup, you
can use the following features:

- Publish query metrics – Publish the query
  metrics for your workgroup to CloudWatch. In the Athena console, you can view query metrics
  for each workgroup. In CloudWatch, you can create custom dashboards, and set thresholds
  and alarms on these metrics. For more information, see [Enable CloudWatch query metrics in Athena](athena-cloudwatch-metrics-enable.md "athena-cloudwatch-metrics-enable.md") and [Monitor Athena query metrics with CloudWatch](query-metrics-viewing.md "query-metrics-viewing.md").
- Monitor Athena usage metrics – See how your
  account uses resources by displaying your current service usage through CloudWatch graphs
  and dashboards. For more information, see [Monitor Athena usage metrics with CloudWatch](monitoring-athena-usage-metrics.md "monitoring-athena-usage-metrics.md")
- Monitor query events – Use Amazon EventBridge to
  receive real-time notifications regarding the state of your queries. For more
  information, see [Monitor Athena query events with EventBridge](athena-events.md "athena-events.md").
- Create data usage controls – In Athena, you
  can configure per-query and per-workgroup data usage controls. Athena cancels queries
  when they exceed the specified threshold or activates an Amazon SNS alarm when a
  workgroup threshold is breached. For more information, see [Configure per-query and per-workgroup data usage controls](workgroups-setting-control-limits-cloudwatch.md "workgroups-setting-control-limits-cloudwatch.md").
- Use cost allocation tags – Use the Billing
  and Cost Management console to tag workgroups with cost allocation tags. The costs
  associated with running queries in the workgroup appear in your Cost and Usage
  Reports with the corresponding cost allocation tag. For more information, see [Using user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md") in the
  _AWS Billing User Guide_.
- Use capacity reservations – You can create
  capacity reservations with the number of data processing units that you specify and
  add one or more workgroups to the reservation. For more information, see [Manage query processing capacity](capacity-management.md "capacity-management.md").
  For additional information about using Athena workgroups to separate workloads, control
  user access, and manage query usage and costs, see the AWS Big Data Blog post [Separate queries and managing costs using Amazon Athena workgroups](https://aws.amazon.com/blogs/big-data/separating-queries-and-managing-costs-using-amazon-athena-workgroups/ "https://aws.amazon.com/blogs/big-data/separating-queries-and-managing-costs-using-amazon-athena-workgroups/").

###### Note

Amazon Athena resources can now be accessed within Amazon SageMaker Unified Studio
(Preview), which helps you access your organization's data and act on it with the best tools. You can migrate saved queries from an Athena workgroup to a SageMaker Unified
Studio project, configure projects with existing Athena workgroups, and maintain
necessary permissions through IAM role updates. For more information, see [Migrating Amazon Athena resources to Amazon SageMaker Unified Studio
(Preview)](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena").

## Considerations and limitations

When you use workgroups in Athena, keep in mind the following points:

- Each account has a primary workgroup. By default, if you have not created any
  workgroups, all queries in your account run in the primary workgroup. The primary
  workgroup cannot be deleted. The default permissions allow all authenticated users
  access to this workgroup.
- When you have access to a workgroup, you can view the workgroup's settings,
  metrics, and data usage control limits. With additional permissions, you can edit
  the settings and data usage control limits.
- When you run queries, they run in the current workgroup. You can run queries in
  the context of a workgroup in the console, through API operations, through the
  command line interface, or through a client application by using a JDBC or ODBC
  driver.
- In the Athena console query editor, you can open up to ten query tabs within each
  workgroup. When you switch between workgroups, your query tabs remain open for a
  maximum of three workgroups.
- You can create up to 1000 workgroups per AWS Region in your account.
- Workgroups can be disabled. Disabling a workgroup prevents queries from running in
  the workgroup until you re-enable the workgroup.
- Athena warns you if you attempt to delete a workgroup that contains saved queries.
  Before you delete a workgroup to which other users have access, make sure they have
  access to another workgroup that they can use to run queries.

###### Topics

- [Create a workgroup](creating-workgroups.md "creating-workgroups.md")
- [Manage workgroups](workgroups-create-update-delete.md "workgroups-create-update-delete.md")
- [Use CloudWatch and EventBridge to monitor queries](workgroups-control-limits.md "workgroups-control-limits.md")
- [Use Athena workgroup APIs](workgroups-api-list.md "workgroups-api-list.md")
- [Troubleshoot workgroups](workgroups-troubleshooting.md "workgroups-troubleshooting.md")
