

# Get notified about host events

 AWS Health tells you in advance when an EC2 instance that runs one of your Amazon Elastic VMware Service hosts is scheduled for maintenance or retirement. You can route these events with Amazon EventBridge to an Amazon SNS topic, so that your operations team gets them by email or another channel. You can set up the rule with the EventBridge console or the AWS CLI.

## Events that affect your environment
<a name="monitor-notifications-events"></a>

 AWS sends you the following notifications for an Amazon EVS environment.

 **EC2 scheduled events**   
If an instance that runs one of your hosts is affected by a scheduled event, AWS notifies you in advance. AWS sends an email to the address that’s associated with your AWS account, and sends an AWS Health event. The events include `system-maintenance` and `instance-retirement` events. For what to do when you get one, see [Host maintenance and retirement events](evs-host-maintenance.md).

 **Impaired environment health**   
If a required connector is not created or becomes unreachable, Amazon EVS reports impaired environment health through AWS Health. For more information, see [Monitor environment status](evs-env-status-check.md).

 **Windows Server entitlements**   
If the connection to vCenter Server is not restored within the 8-hour grace period, Amazon EVS removes the entitlements and sends you an AWS Health notification. For more information, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

 AWS Health events identify the affected EC2 instance. To find the host that runs on an instance, compare the instance ID with the `ec2InstanceId` value that `aws evs list-environment-hosts` returns.

## Before you begin
<a name="monitor-notifications-before"></a>

Before you create the rule, complete the following tasks.
+ Create an Amazon SNS topic and subscribe your email address or another endpoint to it. For more information, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the *Amazon Simple Notification Service Developer Guide*.
+ Make sure that the access policy of the topic allows EventBridge to publish to it. For more information, see [Amazon SNS permissions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html#eb-sns-permissions) in the *Amazon EventBridge User Guide*.
+ Create the rule in each AWS Region where you have an Amazon EVS environment. EventBridge rules receive events for your own AWS account only.

## Event pattern
<a name="monitor-notifications-pattern"></a>

The following event pattern matches AWS Health scheduled change events for Amazon EC2. This includes maintenance and retirement events for the instances that run your hosts.

```json
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "service": ["EC2"],
    "eventTypeCategory": ["scheduledChange"]
  }
}
```

To also receive EC2 issue events, add `issue` to the `eventTypeCategory` list. For the fields that you can match, see [Reference: AWS Health events Amazon EventBridge schema](https://docs.aws.amazon.com/health/latest/ug/aws-health-events-eventbridge-schema.html) in the * AWS Health User Guide*.

The pattern matches events for every EC2 instance in your account, not only your Amazon EVS hosts.

## Create the rule
<a name="monitor-notifications-create"></a>

To create the rule in the Amazon EventBridge console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EventBridge console](https://console.aws.amazon.com/events).

1. Create a rule on the default event bus with the event pattern from the previous section. For the steps, see [Creating rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-visual.html) in the *Amazon EventBridge User Guide*.

1. For the target, choose your Amazon SNS topic.

1. Create the rule.

1. Save the event pattern from the previous section in a file named `evs-host-events.json`.

1. Create the rule. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws events put-rule \
       --name evs-host-events \
       --event-pattern file://evs-host-events.json \
       --region <region-code>
   ```

1. Add your Amazon SNS topic as the target of the rule. Replace `<region-code>` with the Region where you created the environment. Replace the example account ID with your own value.

   ```bash
   aws events put-targets \
       --rule evs-host-events \
       --targets 'Id=1,Arn=arn:aws:sns:<region-code>:111122223333:evs-host-events' \
       --region <region-code>
   ```

   In other partitions, such as AWS GovCloud (US), replace `arn:aws` with the partition of your account, for example `arn:aws-us-gov`.

1. Confirm that the rule exists. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws events describe-rule \
       --name evs-host-events \
       --region <region-code>
   ```

You have created a rule that sends EC2 scheduled change events to your Amazon SNS topic. To check the pattern without waiting for an event, use the sample events in the EventBridge console. For more information, see [Configuring an EventBridge rule to send notifications about events in AWS Health](https://docs.aws.amazon.com/health/latest/ug/creating-event-bridge-events-rule-for-aws-health.html) in the * AWS Health User Guide*.

To receive events from all accounts in an organization, see [Aggregating AWS Health events](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html) in the * AWS Health User Guide*.

Next step: Plan how you respond to each event type. For more information, see [Host maintenance and retirement events](evs-host-maintenance.md).