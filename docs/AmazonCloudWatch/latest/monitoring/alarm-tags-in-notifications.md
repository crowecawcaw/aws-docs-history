

# Alarm tags in action payloads
<a name="alarm-tags-in-notifications"></a>

With CloudWatch, you can include an alarm's tags in the payloads it sends when the alarm changes state. You can then route, filter, or add context to notifications by using tags such as team, environment, or cost center.

You can use alarm tags with the following destinations: Amazon SNS notifications, Lambda function invocations, and the alarm state change events that CloudWatch sends to EventBridge.

CloudWatch sends alarm state change events to EventBridge by default, so configured tags appear in those events even when you don't configure an action on the alarm. For Amazon SNS and Lambda, tags appear only when you configure that action for the alarm. For Amazon SNS, CloudWatch includes the tags in the notification message that it delivers to the topic's subscribers, including those that use the HTTP/HTTPS and email protocols.

**Note**  
CloudWatch doesn't support alarm tags for other actions, such as Systems Manager OpsItems, Systems Manager Incident Manager incidents, Amazon EC2 actions, Amazon EC2 Auto Scaling and Application Auto Scaling actions, or CloudWatch investigations.

Tag keys that begin with `aws:` are reserved for AWS and are never propagated.

Each payload includes a status field (`AlarmTagsStatus` for Amazon SNS, and `alarmTagsStatus` for Lambda and EventBridge) with one of the following values:
+ `SUCCESS` – The tags were retrieved and any key filter was applied. The list can be empty if the filter excluded all tags.
+ `NO_TAGS` – The alarm has no tags.
+ `TRUNCATED` – Some tags were omitted to keep the payload within its size limit. If your tags are truncated, narrow the set of tags that CloudWatch includes by using the include or exclude tag key options.
+ `FAILURE` – The tags couldn't be retrieved when the notification was sent. CloudWatch still delivers the notification or event, with no tags.

The representation of the tags differs by destination. Amazon SNS and Lambda include the tags as a list of key-value objects, and EventBridge includes them as key-value pairs to make event pattern filtering easier. For the Amazon SNS schema, see [Schema of Amazon SNS notifications when alarms change state](Notify_Users_Alarm_Changes.md#alarm-sns-schema). For Lambda, see [Invoke a Lambda function from an alarm](alarms-and-actions-Lambda.md). For EventBridge, see [Alarm events and EventBridge](cloudwatch-and-eventbridge.md).

Each notification or event reflects the alarm's tags at the time of the state change, including tag changes that you make after you create the alarm.

By default, when tag propagation is enabled, CloudWatch includes all of the alarm's tags (future tags as well if they are added later). To include only the relevant tags, or to exclude sensitive tags that you don't want to send in the payload, provide an include or exclude tag key list:
+ Exclude tag keys – CloudWatch includes all of the alarm's tags except the keys that you specify. Any tags that you add later are also included, unless their keys are in the exclude list.
+ Include tag keys – CloudWatch includes only the keys that you specify. If you add a new tag later and want it in the payload, you must add its key to the include list.

## Prerequisites
<a name="alarm-tags-prerequisites"></a>

A principal that creates or updates an alarm to enable this configuration must have the `cloudwatch:ListTagsForResource` permission for that alarm. CloudWatch also provides the `cloudwatch:AlarmTagsPropagationEnabled` condition key to control whether principals can enable tag propagation.

## Enable alarm tag propagation using the console
<a name="alarm-tags-console"></a>

You enable tag propagation while you create or edit an alarm in the CloudWatch console.

**To enable alarm tag propagation**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/), and then start creating an alarm, or edit an existing alarm.

1. On the **Add alarm details** step, under the tag editor, select **Include this alarm's tags in action and event payloads**.

1. To set which tags to include, select **All tags** to include all of the alarm's tags, or select **Select tags** to specify tag keys.

1. If you selected **Select tags**, select **Include tags** to include only the keys that you specify, or select **Exclude tags** to include all tags except the keys that you specify.

1. If you selected **Include tags** or **Exclude tags**, enter the tag keys in **Tag keys to include** or **Tag keys to exclude**.

1. Choose **Preview and create** to review your choice.

1. Finish creating or saving the alarm.

After you complete these steps, the alarm includes its tags in its notifications and events when its state changes.

To view the setting later, open the alarm's **Tags** tab on the alarm details page. To change the setting without the wizard, choose **Manage tags**.

## Enable alarm tag propagation using the API
<a name="alarm-tags-api"></a>

To enable tag propagation with the API, set the `AlarmTagsPropagation` configuration within the `ActionConfiguration` parameter on `PutMetricAlarm`, `PutCompositeAlarm`, or `PutLogAlarm`, and set `Enabled` to `true`. `DescribeAlarms` returns the current configuration.

To include all of the alarm's tags, omit both of the following mutually exclusive lists. To narrow the set of tags, use one of them:
+ `IncludedTagKeys` – Include only the listed keys.
+ `ExcludedTagKeys` – Include all keys except those listed.

Each list can contain from 1 to 50 tag keys, and each tag key can be from 1 to 128 characters.

For more information, see [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html), [PutCompositeAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html), [PutLogAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutLogAlarm.html), and [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) in the *Amazon CloudWatch API Reference*.