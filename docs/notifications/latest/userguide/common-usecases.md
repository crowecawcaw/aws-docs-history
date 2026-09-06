

# Filtering event rules using customized JSON event patterns in AWS User Notifications
<a name="common-usecases"></a>

Event rules are used to receive notifications about specific events. To apply additional filters to your event rules, you can customize event patterns for those rules. Advanced filtering options include:
+  Suffix filtering - match against characters at the end of a value 
+  $or matching - use a single rule to check if conditions across several different fields are true 
+  Equals-ignore-case - ignore case sensitivity 

**Note**  
Wildcards aren't currently supported.

This topic includes JSON samples for commonly used event patterns and additional information on the EventBridge console's rule builder. For more event pattern examples, see [Content filtering in Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.html) in the *Amazon EventBridge User Guide*.

Managed rules include event patterns that are required by the service to manage your notifications.

**Note**  
 Additional filters you create for your notification preferences don't appear in the corresponding managed event rules in EventBridge. The managed rules created by User Notifications in EventBridge contain only the base event patterns necessary for routing notifications. For more information, see [Amazon EventBridge managed rules in AWS User Notifications](ev-managed-rules.md). 

**Tip**  
By default, User Notifications adds the service and event type to the event rule. You can include them in the **Advanced filter**, but they aren't required.  
For assistance while building your event patterns, you can use the [EventBridge console's rule builder](https://us-west-2.console.aws.amazon.com/events/home?region=us-east-1#/rules/create). Use the Event Pattern Builder and the in-place tester to try out your patterns. You aren't required to complete the **Create rule** workflow to use the rule builder.

**Topics**
+ [AWS Health events about specific services and event type categories](#specific-services)
+ [Amazon EC2 instance state changed to "terminated", "stopping", "stopped", or "shutting-down"](#ec2-solo)
+ [Specific Amazon CloudWatch alarm in alarm state](#root-user)
+ [Root user sign-in without multi-factor authentication](#root-user-mfa)
+ [Amazon GuardDuty findings with medium and high severity](#guardduty-event)

## AWS Health events about specific services and event type categories
<a name="specific-services"></a>

The following event pattern creates a rule to monitor events for the `issue`, `accountNotification`, and `scheduledChange` event type categories for Amazon EC2, Amazon EC2 Auto Scaling, and Amazon Virtual Private Cloud. For more information, see [Monitoring AWS Health events with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the *AWS Health User Guide*.

**To use the following JSON code:**

1. Create or edit a notification configuration in the [User Notifications console](https://console.aws.amazon.com/notifications/).

1. 

**Create an Event Rule:**

   1. For **AWS service name**, select **Health**.

   1. For **Event Type**, select **Specific Health Events**.

   1. For **Regions**, select the AWS Regions where your service data is located.

   1. In **Advanced filter**, paste the following JSON code.

```
{
  "detail": {
    "eventTypeCategory": [
      "issue",
      "accountNotification",
      "scheduledChange"
    ],
    "service": [
      "AUTOSCALING",
      "VPC",
      "EC2"
    ]
  }
}
```

## Amazon EC2 instance state changed to "terminated", "stopping", "stopped", or "shutting-down"
<a name="ec2-solo"></a>

The following event pattern matches `terminated`, `stopping`, `stopped`, and `shutting-down` state changes for all Amazon EC2 instances. For more information, see [State change events for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instance-state-changes.html) in the *Amazon EC2 User Guide*.

**To use the following JSON code:**

1. Create or edit a notification configuration in the [User Notifications console](https://console.aws.amazon.com/notifications/).

1. 

**Create an Event Rule:**

   1. For **AWS service name**, select **EC2**.

   1. For **Event Type**, select **EC2 Instance State-Change Notification**.

   1. For **Regions**, select the AWS Regions where your service data is located.

   1. In **Advanced filter**, paste the following JSON code.

```
{
  "detail": {
    "state": ["terminated", "stopping", "stopped", "shutting-down"]
  }
}
```

## Specific Amazon CloudWatch alarm in alarm state
<a name="root-user"></a>

The following event pattern allows you to specify CloudWatch alarms in the `ALARM` state by using resource ARNs. For more information, see [Alarm events and EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-eventbridge.html.html) in the *Amazon CloudWatch User Guide*.

**To use the following JSON code:**

1. Create or edit a notification configuration in the [User Notifications console](https://console.aws.amazon.com/notifications/).

1. 

**Create an Event Rule:**

   1. For **AWS service name**, select **CloudWatch**.

   1. For **Event Type**, select **CloudWatch alarm state change**.

   1. For **Regions**, select the AWS Regions where your service data is located.

   1. In **Advanced filter**, paste the following JSON code.

```
{
  "resources": [
    "arn:aws:cloudwatch:us-east-1:123456789012:alarm:BillingAlarm",
    "arn:aws:cloudwatch:us-east-1:123456789012:alarm:TestAlarm"
  ],
  "detail": {
    "state": {
      "value": [
        "ALARM"
      ]
    }
  }
}
```

## Root user sign-in without multi-factor authentication
<a name="root-user-mfa"></a>

The following event pattern allows you to monitor root user sign-in without multi-factor authentication (MFA). For more information, see [AWS Management Console sign-in events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html) in the *AWS CloudTrail User Guide*.

**To use the following JSON code:**

1. Create or edit a notification configuration in the [User Notifications console](https://console.aws.amazon.com/notifications/).

1. 

**Create an Event Rule:**

   1. For **AWS service name**, select **AWS Management Console Sign-in**.

   1. For **Event Type**, select **Sign-in events**.

   1. For **Regions**, select the AWS Regions where your service data is located.

   1. In **Advanced filter**, paste the following JSON code.

```
{
  "detail": {
    "userIdentity": {
      "type": ["Root"]
    },
    "additionalEventData": {
      "MFAUsed": ["No"]
    }
  }
}
```

## Amazon GuardDuty findings with medium and high severity
<a name="guardduty-event"></a>

The following event pattern allows you to monitor GuardDuty findings with medium and high severity. For more information, see [Severity levels for GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html#guardduty_findings-severity) in the *Amazon GuardDuty User Guide*.

**To use the following JSON code:**

1. Create or edit a notification configuration in the [User Notifications console](https://console.aws.amazon.com/notifications/).

1. 

**Create an Event Rule:**

   1. In **Event rule**, for **AWS service name**, select **GuardDuty**.

   1. For **Event Type**, select **GuardDuty Finding**.

   1. For **Regions**, select the AWS Regions where your service data is located.

   1. In **Advanced filter**, paste the following JSON code.

```
{
  "detail-type": [
    "GuardDuty Finding"
  ],
  "source": [
    "aws.guardduty"
  ],
  "detail": {
    "severity": [{
      "numeric": [">=", 4]
    }]
  }
}
```