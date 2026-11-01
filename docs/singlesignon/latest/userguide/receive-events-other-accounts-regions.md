

# Receive events in other accounts and Regions
<a name="receive-events-other-accounts-regions"></a>

By default, you receive event notifications on the default event bus in the account and AWS Region where your IAM Identity Center instance is enabled. If you want a central security team to monitor identity changes, or if your instance is replicated to additional AWS Regions, you can process the events in a different AWS account or Region.

## Send events to another AWS account
<a name="receive-events-another-account"></a>

To process events in another account, such as a central security account, add a target to your rule that sends the events to an event bus in that account. The receiving event bus must allow your account to send events to it. For more information, see [Sending and receiving events between AWS accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html) in the Amazon EventBridge User Guide.

## Events in multiple AWS Regions
<a name="receive-events-multiple-regions"></a>

To receive events in more than one AWS Region, you must enable multi-Region replication for your IAM Identity Center instance. IAM Identity Center emits events only in Regions where your instance is replicated; without multi-Region replication, you receive events only in the AWS Region where you enabled your instance.

After you replicate your IAM Identity Center instance to additional AWS Regions, you receive events on the default event bus in each AWS Region where your instance is available. A single change results in an event in each of these Regions. To process each change once, create your rule in one Region. To keep receiving events when that Region is unavailable, create rules in more than one Region and handle the duplicate events in your workflow. For more information, see [Using IAM Identity Center across multiple AWS Regions](multi-region-iam-identity-center.md).