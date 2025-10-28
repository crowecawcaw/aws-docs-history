# Creating EventBridge rules for AWS Region coverage

You must create an EventBridge rule for each Region that you want to
receive AWS Health events for. If you don’t create a rule, you won’t receive events. For
example, to receive events from the US West (Oregon) Region, you must create a rule for this
Region.

Setting up an additional rule in a backup Region adds an extra
layer of resilience to your workflows, should your primary rule be affected by an ongoing
event. Public events for AWS Health are sent simultaneously to both the impacted Region and
to a backup Region. See [About public events for AWS Health](cloudwatch-events-health.md#about-public-events "cloudwatch-events-health.md#about-public-events") for more information. For
all Regions in the standard AWS partition, you can setup a rule in US West (Oregon) as a
backup to continue receiving events even if your primary Region is affected by an ongoing
issue. The backup Region for the US West (Oregon) Region is US East (N. Virginia) Region.

For example, if you're monitoring events in the Europe (Frankfurt) Region
and that Region is temporarily unavailable, then AWS Health will also deliver that event to
the US West (Oregon) Region. Next, your back up EventBridge rule sends the event to the targets that
you specified. To create a backup rule, follow the procedure below for [Configuring an EventBridge rule to
send notifications about events in AWS Health](creating-event-bridge-events-rule-for-aws-health.md "creating-event-bridge-events-rule-for-aws-health.md") and use the
US West (Oregon) Region.

Some AWS Health events are not Region-specific. Events that
aren't specific to a Region are called global events. These include events sent for AWS Identity and Access Management
(IAM). To receive global events, you must create a rule for the US East (N. Virginia) Region
for the primary Region and US West (Oregon) Region as the backup Region.

To receive global events in the AWS GovCloud (US), you must create a
rule in the AWS GovCloud (US-West) Region.
