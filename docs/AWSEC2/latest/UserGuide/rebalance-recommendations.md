# EC2 instance rebalance recommendations

An EC2 instance _rebalance recommendation_ is a signal that
notifies you when a Spot Instance is at elevated risk of interruption. The signal can arrive
sooner than the [two-minute Spot
Instance interruption notice](spot-instance-termination-notices.md "spot-instance-termination-notices.md"), giving you the opportunity to proactively
manage the Spot Instance. You can decide to rebalance your workload to new or existing Spot Instances that
are not at an elevated risk of interruption.

It is not always possible for Amazon EC2 to send the rebalance recommendation signal before the
two-minute Spot Instance interruption notice. Therefore, the rebalance recommendation
signal can arrive along with the two-minute interruption notice.

Rebalance recommendations are made available as a EventBridge event and as an item in
the [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") on the Spot Instance. Events are emitted on a best effort
basis.

###### Note

Rebalance recommendations are only supported for Spot Instances that are launched after November 5,
2020 00:00 UTC.

###### Contents

- [Rebalance actions you can take](#rebalancing-actions "#rebalancing-actions")
- [Monitor rebalance recommendation
  signals](#monitor-rebalance-recommendations "#monitor-rebalance-recommendations")
- [Services that use the rebalance recommendation
  signal](#services-using-rebalance-rec-signal "#services-using-rebalance-rec-signal")

## Rebalance actions you can take

These are some of the possible rebalancing actions that you can take:

Graceful shutdown

When you receive the rebalance recommendation signal for a Spot Instance, you can start your
instance shutdown procedures, which might include ensuring that
processes are completed before stopping them. For example, you can
upload system or application logs to Amazon Simple Storage Service (Amazon S3), you can shut down
Amazon SQS workers, or you can complete deregistration from the Domain
Name System (DNS). You can also save your work in external storage and
resume it at a later time.

Prevent new work from being scheduled

When you receive the rebalance recommendation signal for a Spot Instance, you can prevent new
work from being scheduled on the instance, while continuing to use the
instance until the scheduled work is completed.

Proactively launch new replacement instances

You can configure Auto Scaling groups, EC2 Fleet, or Spot Fleet to automatically launch replacement Spot Instances
when a rebalance recommendation signal is emitted. For more information,
see [Use Capacity
Rebalancing to handle Amazon EC2 Spot interruptions](../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md") in the _Amazon EC2 Auto Scaling User Guide_,
and [Use Capacity Rebalancing in EC2 Fleet and Spot Fleet
to replace at-risk Spot Instances](ec2-fleet-capacity-rebalance.md "ec2-fleet-capacity-rebalance.md")
in this user guide.

## Monitor rebalance recommendation

signals

You can monitor the rebalance recommendation signal so that, when it is emitted, you can
take the actions that are specified in the preceding section. The rebalance
recommendation signal is made available as an event that is sent to Amazon EventBridge
(formerly known as Amazon CloudWatch Events) and as instance metadata on the Spot Instance.

###### Monitor rebalance recommendation signals:

- [Use Amazon EventBridge](#cp-eventbridge "#cp-eventbridge")
- [Use instance metadata](#cp-instance-metadata "#cp-instance-metadata")

### Use Amazon EventBridge

When the rebalance recommendation signal is emitted for a Spot Instance, the event for the signal
is sent to Amazon EventBridge. If EventBridge detects an event pattern that matches a pattern
defined in a rule, EventBridge invokes a target (or targets) specified in the
rule.

The following is an example event for the rebalance recommendation signal.

```
{
    "version": "0",
    "id": "`12345678-1234-1234-1234-123456789012`",
    "detail-type": "EC2 Instance Rebalance Recommendation",
    "source": "aws.ec2",
    "account": "`123456789012`",
    "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "region": "`us-east-2`",
    "resources": ["arn:aws:ec2:`us-east-2`:`123456789012`:instance/`i-1234567890abcdef0`"],
    "detail": {
        "instance-id": "`i-1234567890abcdef0`"
    }
}
```

The following fields form the event pattern that is defined in the rule:

`"detail-type": "EC2 Instance Rebalance Recommendation"`

Identifies that the event is a rebalance recommendation event

`"source": "aws.ec2"`

Identifies that the event is from Amazon EC2

#### Create an EventBridge rule

You can write an EventBridge rule and automate what actions to take when the event pattern
matches the rule.

The following example creates an EventBridge rule to send an email, text message, or mobile push
notification every time Amazon EC2 emits a rebalance recommendation signal.
The signal is emitted as an `EC2 Instance Rebalance
 Recommendation` event, which triggers the action defined by the
rule.

Before creating the EventBridge rule, you must create the Amazon SNS topic for the
email, text message, or mobile push notification.

###### To create an EventBridge rule for a rebalance recommendation event

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  Choose **Create rule**.
3.  For **Define rule detail**, do the following:
    1. Enter a **Name** for the rule, and, optionally, a description.

    A rule can't have the same name as another rule in the same Region and on the same event bus. 2. For **Event bus**, choose **default**. When an AWS
    service in your account generates an event, it always goes to your
    account's default event bus. 3. For **Rule type**, choose **Rule with an event
    pattern**. 4. Choose **Next**.

4.  For **Build event pattern**, do the following:
    1. For **Event source**, choose **AWS events or EventBridge
       partner events**.
    2. For **Event pattern**, for this example you’ll specify the following
       event pattern to match the `EC2 Instance Rebalance
Recommendation` event, and then choose
       **Save**.

    ```
    {
     "source": ["aws.ec2"],
     "detail-type": ["EC2 Instance Rebalance Recommendation"]
    }
    ```

    To add the event pattern, you can either use a template by choosing **Event
    pattern form**, or specify your own pattern by choosing
    **Custom pattern (JSON editor)**, as
    follows:

        1. To use a template to create the event pattern, do the
         following:


        	1. Choose **Event pattern
        	 form**.
        	2. For **Event source**, choose
        	 **AWS services**.
        	3. For **AWS Service**, choose
        	 **EC2 Spot Fleet**.
        	4. For **Event type**, choose
        	 **EC2 Instance Rebalance Recommendation**.
        	5. To customize the template, choose **Edit
        	 pattern** and make your changes to match
        	 the example event pattern.
        2. (Alternative) To specify a custom event pattern, do
         the following:


        	1. Choose **Custom pattern (JSON editor)**.
        	2. In the **Event pattern** box, add the event pattern for this example.

    3. Choose **Next**.

5.  For **Select target(s)**, do the following:
    1. For **Target types**, choose **AWS service**.
    2. For **Select a target**, choose **SNS topic** to send an email, text message, or mobile push notification when the event occurs.
    3. For **Topic**, choose an existing topic. You first need to create an
       Amazon SNS topic using the Amazon SNS console. For more information, see
       [Using Amazon SNS for
       application-to-person (A2P) messaging](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md") in the _Amazon Simple Notification Service Developer Guide_.
    4. (Optional) Under **Additional settings**, you can optionally
       configure additional settings. For more information, see [Creating Amazon EventBridge rules that react
       to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") (step 16) in the _Amazon EventBridge User Guide_.
    5. Choose **Next**.

6.  (Optional) For **Tags**, you can optionally assign one or more tags to your rule, and then choose **Next**.
7.  For **Review and create**, do the following:
    1. Review the details of the rule and modify them as necessary.
    2. Choose **Create rule**.

For more information, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") and [Amazon EventBridge event
patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the _Amazon EventBridge User Guide_

### Use instance metadata

The instance metadata category `events/recommendations/rebalance` provides the approximate time, in
UTC, when the rebalance recommendation signal was emitted for a Spot
Instance.

We recommend that you check for rebalance recommendation signals every 5
seconds so that you don't miss an opportunity to act on the rebalance
recommendation.

If a Spot Instance receives a rebalance recommendation, the time that the signal was
emitted is present in the instance metadata. You can retrieve the time that the
signal was emitted as follows.

IMDSv2

###### Linux

Run the following command from your Linux instance.

**IMDSv2**

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/events/recommendations/rebalance
```

###### Windows

Run the following cmdlet from your Windows instance

```
[string]$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/events/recommendations/rebalance
```

IMDSv1

###### Linux

Run the following command from your Linux instance.

```
curl http://169.254.169.254/latest/meta-data/events/recommendations/rebalance
```

###### Windows

Run the following cmdlet from your Windows instance.

```
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/events/recommendations/rebalance
```

The following is example output, which indicates the time, in UTC, that the rebalance
recommendation signal was emitted for the Spot Instance.

```
{"noticeTime": "2020-10-27T08:22:00Z"}
```

If the signal has not been emitted for the instance,
`events/recommendations/rebalance` is not present and you receive
an HTTP 404 error when you try to retrieve it.

## Services that use the rebalance recommendation

signal

Amazon EC2 Auto Scaling, EC2 Fleet, and Spot Fleet use the rebalance recommendation signal to make it easy for you to
maintain workload availability by proactively augmenting your fleet with a new Spot Instance
before a running instance receives the two-minute Spot Instance interruption notice.
You can have these services monitor and respond proactively to changes affecting the
availability of your Spot Instances. For more information, see the following:

- [Use
  Capacity Rebalancing to handle Amazon EC2 Spot interruptions](../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md") in the
  _Amazon EC2 Auto Scaling User Guide_
- [Use Capacity Rebalancing in EC2 Fleet and Spot Fleet
  to replace at-risk Spot Instances](ec2-fleet-capacity-rebalance.md "ec2-fleet-capacity-rebalance.md") in the EC2 Fleet and Spot Fleet topic in
  this user guide
