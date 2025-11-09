# Creating EventBridge rules for AWS Region coverage

You can create an EventBridge rule for each Region that you want to
receive AWS Health events for. For
example, to receive events from the Europe (Frankfurt) Region, you can create a rule for this
Region.

To enhance the reliability of AWS Health notifications, you can
set up rules in the dedicated backup regions. In the standard AWS partition, the
US West (Oregon) Region acts as the backup region for all other regions, while US East (N. Virginia) Region serves as
the backup for the US West (Oregon) Region. When health events occur, they are automatically sent to
both the primary region and its designated backup region. For example, if you're monitoring
events in the Europe (Frankfurt) Region, then any health events are delivered to both the
Europe (Frankfurt) Region and the US West (Oregon) Region. This system makes sure you'll continue to receive
health notifications even if your primary region experiences issues. To create a backup rule,
follow the procedure for [Configuring an EventBridge rule to
send notifications about events in AWS Health](creating-event-bridge-events-rule-for-aws-health.md "creating-event-bridge-events-rule-for-aws-health.md").

If you prefer not to use backup functionality, then you'll need to add a filter to your backup region rule. For example, implement a filter for `detail.backupEvent = False`. This prevents you from receiving backup events from other regions.

## High availability setup (optional)

If you want to create an EventBridge integration with high availability, make sure you have implemented rules in both the relevant and backup regions, and then implement de-duplication using `detail.communicationId`. This makes sure you receive all events while avoiding duplicates. For more information, see [Reference: AWS Health events
Amazon EventBridge schema](aws-health-events-eventbridge-schema.md "aws-health-events-eventbridge-schema.md").

## Simplified integration

If you want to capture events from multiple AWS Regions but prefer to configure only a
single rule, then simplified integration is the appropriate option. To receive Health events
from all Regions in the standard AWS partition, you can set up a central rule in the
US West (Oregon) Region. This single rule automatically aggregates events from all
standard partition regions where you are receiving Health events. However, you won't have
high availability configuration.

## Global events

Some AWS Health events are not Region-specific. Events that
aren't specific to a Region are called global events. These include events sent for AWS Identity and Access Management
(IAM). To receive global events, you must create a rule for the US East (N. Virginia) Region.
