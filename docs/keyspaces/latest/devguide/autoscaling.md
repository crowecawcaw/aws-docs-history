# Manage throughput capacity automatically with Amazon Keyspaces auto scaling

Many database workloads are cyclical in nature or are difficult to predict in advance. For
example, consider a social networking app where most of the users are active during daytime
hours. The database must be able to handle the daytime activity, but there's no need for the
same levels of throughput at night.

Another example might be a new mobile gaming app that is
experiencing rapid adoption. If the game becomes very popular, it could exceed the available
database resources, which would result in slow performance and unhappy customers. These
kinds of workloads often require manual intervention to scale database resources up or down
in response to varying usage levels.

Amazon Keyspaces (for Apache Cassandra) helps you provision throughput capacity efficiently for variable workloads by
adjusting throughput capacity automatically in response to actual application traffic. Amazon Keyspaces
uses the Application Auto Scaling service to increase and decrease a table's read and write capacity on
your behalf. For more information about Application Auto Scaling, see the [Application Auto Scaling User Guide](../../../autoscaling/application/userguide.md "../../../autoscaling/application/userguide.md").

###### Note

To get started with Amazon Keyspaces automatic scaling quickly, see [Configure and update Amazon Keyspaces automatic scaling policies](autoscaling.md "autoscaling.md").

## How Amazon Keyspaces automatic scaling works

The following diagram provides a high-level overview of how Amazon Keyspaces automatic scaling
manages throughput capacity for a table.

![A diagram showing the different services involved when a user makes a change to an Amazon Keyspaces table. The services are Amazon CloudWatch, Amazon SNS, and Application Auto Scaling, which issues the ALTER TABLE statement to change the capacity based on the users read or write usage.](images/keyspaces_auto-scaling.png)

To enable automatic scaling for a table, you create a _scaling
policy_. The scaling policy specifies whether you want to scale read
capacity or write capacity (or both), and the minimum and maximum provisioned capacity
unit settings for the table.

The scaling policy also defines a _target utilization_. Target
utilization is the ratio of consumed capacity units to provisioned capacity units at a
point in time, expressed as a percentage. Automatic scaling uses a _target
tracking_ algorithm to adjust the provisioned throughput of the table
upward or downward in response to actual workloads. It does this so that the actual
capacity utilization remains at or near your target utilization.

You can set the automatic scaling target utilization values between 20 and 90 percent
for your read and write capacity. The default target utilization rate is 70 percent. You
can set the target utilization to be a lower percentage if your traffic changes quickly
and you want capacity to begin scaling up sooner. You can also set the target
utilization rate to a higher rate if your application traffic changes more slowly and
you want to reduce the cost of throughput.

For more information about scaling policies, see [Target tracking
scaling policies for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md "../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md") in the [_Application Auto Scaling User Guide_](../../../autoscaling/application/userguide.md "../../../autoscaling/application/userguide.md").

When you create a scaling policy, Amazon Keyspaces creates two pairs of Amazon CloudWatch alarms on your
behalf. Each pair represents your upper and lower boundaries for provisioned and
consumed throughput settings. These CloudWatch alarms are triggered when the table's actual
utilization deviates from your target utilization for a sustained period of time. To
learn more about Amazon CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

When one of the CloudWatch alarms is triggered, Amazon Simple Notification Service (Amazon SNS) sends you a notification
(if you have enabled it). The CloudWatch alarm then invokes Application Auto Scaling to evaluate your scaling
policy. This in turn issues an Alter Table request to Amazon Keyspaces to adjust the table's
provisioned capacity upward or downward as appropriate. To learn more about Amazon SNS
notifications, see [Setting up Amazon SNS
notifications](../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md "../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md").

Amazon Keyspaces processes the Alter Table request by increasing (or decreasing) the table's
provisioned throughput capacity so that it approaches your target utilization.

###### Note

Amazon Keyspaces auto scaling modifies provisioned throughput settings only when the actual
workload stays elevated (or depressed) for a sustained period of several minutes.
The target tracking algorithm seeks to keep the target utilization at or near your
chosen value over the long term. Sudden, short-duration spikes of activity are
accommodated by the table's built-in burst capacity.

## How auto scaling works for multi-Region

tables

To ensure that there's always enough read and write capacity for all table replicas in
all AWS Regions of a multi-Region table in provisioned capacity mode, we recommend
that you configure Amazon Keyspaces auto scaling.

When you use a multi-Region table in provisioned mode with auto scaling, you can't
disable auto scaling for a single table replica. But you can adjust the table's read
auto scaling settings for different Regions. For example, you can specify different read
capacity and read auto scaling settings for each Region that the table is replicated in.

The read auto scaling settings that you configure for a table replica in a specified
Region overwrite the general auto scaling settings of the table. The write capacity,
however, has to remain synchronized across all table replicas to ensure that there's
enough capacity to replicate writes in all Regions.

Amazon Keyspaces auto scaling independently updates the provisioned capacity of the table in each
AWS Region based on the usage in that Region. As a result, the provisioned capacity in
each Region for a multi-Region table might be different when auto scaling is
active.

You can configure the auto scaling settings of a multi-Region table and its replicas
using the Amazon Keyspaces console, API, AWS CLI, or CQL. For more information on how to create and
update auto scaling settings for multi-Region tables, see [Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md "tables-mrr-autoscaling.md").

###### Note

If you use auto scaling for multi-Region tables, you must always use Amazon Keyspaces API
operations to configure auto scaling settings. If you use Application Auto Scaling API operations
directly to configure auto scaling settings, you don't have the ability to specify
the AWS Regions of the multi-Region table. This can result in unsupported
configurations.

## Usage notes

Before you begin using Amazon Keyspaces automatic scaling, you should be aware of the
following:

- Amazon Keyspaces automatic scaling is not available in the Middle East (UAE) Region.
- Amazon Keyspaces automatic scaling can increase read capacity or write capacity as often
  as necessary, in accordance with your scaling policy. All Amazon Keyspaces quotas remain in
  effect, as described in [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").
- Amazon Keyspaces automatic scaling doesn't prevent you from manually modifying
  provisioned throughput settings. These manual adjustments don't affect any
  existing CloudWatch alarms that are attached to the scaling policy.
- If you use the console to create a table with provisioned throughput capacity,
  Amazon Keyspaces automatic scaling is enabled by default. You can modify your automatic
  scaling settings at any time. For more information, see [Turn off Amazon Keyspaces auto scaling for a table](autoscaling.md "autoscaling.md").
- If you're using CloudFormation to create scaling policies, you should manage the scaling policies from
  CloudFormation so that the stack is in sync with the stack template. If you change
  scaling policies from Amazon Keyspaces, they will get overwritten with the original values
  from the CloudFormation stack template when the stack is reset.
- If you use CloudTrail to monitor Amazon Keyspaces automatic scaling, you might see alerts for calls made by Application Auto Scaling
  as part of its configuration validation process. You can filter out these alerts by using the `invokedBy`
  field, which contains `application-autoscaling.amazonaws.com` for these validation checks.
