# Monitor Capacity Reservation underutilization

You can monitor Capacity Reservation underutilization using the following:

###### Topics

- [Amazon EventBridge events](#cr-underutilization-events "#cr-underutilization-events")
- [Email and AWS Health Dashboard
  notifications](#monitor-cr-utilization "#monitor-cr-utilization")

## Amazon EventBridge events

AWS Health sends events to Amazon EventBridge when a Capacity Reservation in your account is below 20
percent usage over certain periods. With EventBridge, you can establish rules that trigger
programmatic actions in response to such events. For example, you can create a rule
that automatically cancels a Capacity Reservation when its utilization drops below 20 percent
utilization over a 7-day period.

Events in EventBridge are represented as JSON objects. The fields that are unique to the
event are contained in the "detail" section of the JSON object. The "event" field
contains the event name. The "result" field contains the completed status of the
action that triggered the event. For more information, see [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the
_Amazon EventBridge User Guide_.

For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

This feature is not supported in AWS GovCloud (US).

### Events

AWS Health sends the following events when capacity usage for a Capacity Reservation is below
20 percent.

- `AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION`

The following is an example of an event that is generated when a newly
created Capacity Reservation is below 20 percent capacity usage over a 24-hour
period.

```
{
    "version": "0",
    "id": "b3e00086-f271-12a1-a36c-55e8ddaa130a",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-03-10T12:03:38Z",
    "region": "ap-south-1",
    "resources": [
        "cr-01234567890abcdef"
    ],
    "detail": {
        "eventArn": "arn:aws:health:ap-south-1::event/EC2/AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION/AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_cr-01234567890abcdef-6211-4d50-9286-0c9fbc243f04",
        "service": "EC2",
        "eventTypeCode": "AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION",
        "eventTypeCategory": "accountNotification",
        "startTime": "Fri, 10 Mar 2023 12:03:38 GMT",
        "endTime": "Fri, 10 Mar 2023 12:03:38 GMT",
        "eventDescription": [
            {
                "language": "en_US",
                "latestDescription": "`A description of the event will be provided here`"
            }
        ],
        "affectedEntities": [
            {
                "entityValue": "cr-01234567890abcdef"
            }
        ]
    }
    }
```

- `AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY`

The following is an example of an event that is generated when one or
more Capacity Reservation is below 20 percent capacity usage over a 7-day period.

```
{
    "version": "0", "id":"7439d42b-3c7f-ad50-6a88-25e2a70977e2",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-03-07T06:06:01Z",
    "region": "us-east-1",
    "resources": [
        "cr-01234567890abcdef | us-east-1b | t3.medium | Linux/UNIX | 0.0%",
        "cr-09876543210fedcba | us-east-1a | t3.medium | Linux/UNIX | 0.0%"
    ],
    "detail": {
        "eventArn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY/AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY_726c1732-d6f6-4037-b9b8-bec3c2d3ba65",
        "service": "EC2",
        "eventTypeCode": "AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY",
        "eventTypeCategory": "accountNotification",
        "startTime": "Tue, 7 Mar 2023 06:06:01 GMT",
        "endTime": "Tue, 7 Mar 2023 06:06:01 GMT",
        "eventDescription": [
            {
                "language": "en_US",
                "latestDescription": "`A description of the event will be provided here`"
            }
        ],
        "affectedEntities": [
            {
                "entityValue": "cr-01234567890abcdef | us-east-1b | t3.medium | Linux/UNIX | 0.0%"
            },
            {
                "entityValue": "cr-09876543210fedcba | us-east-1a | t3.medium | Linux/UNIX | 0.0%"
            }
        ]
    }
}
```

### Create an EventBridge rule

To receive email notifications when your Capacity Reservation utilization drops below 20
percent, create an Amazon SNS topic, and then create an EventBridge rule for the
`AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION` event.

###### To create the Amazon SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**, and then
   choose **Create topic**.
3. For **Type**, choose
   **Standard**.
4. For **Name**, enter a name for the new topic.
5. Choose **Create topic**.
6. Choose **Create subscription**.
7. For **Protocol**, choose **Email**,
   and then for **Endpoint**, enter the email address that
   receives the notifications.
8. Choose **Create subscription**.
9. The email address entered above will receive email message with the
   following subject line: `AWS Notification - Subscription
Confirmation`. Follow the directions to confirm your
   subscription.

###### To create the EventBridge rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**, and then
   choose **Create rule**.
3. For **Name**, enter a name for the new rule.
4. For **Rule type**, choose **Rule with an
   event pattern**.
5. Choose **Next**.
6. In the **Event pattern**, do the following:
   1. For **Event source**, choose **AWS
      services**.
   2. For **AWS service**, choose
      **AWS Health**.
   3. For **Event type**, choose **EC2 ODCR
      Underutilization Notification**.

7. Choose **Next**.
8. For **Target 1**, do the following:
   1. For **Target types**, choose **AWS
      service**.
   2. For **Select a target**, choose **SNS
      topic**.
   3. For **Topic**, choose the topic that you
      created earlier.

9. Choose **Next** and then **Next**
   again.
10. Choose **Create rule**.

## Email and AWS Health Dashboard

notifications

AWS Health sends the following email and Health Dashboard notifications when capacity
utilization for Capacity Reservations in your account drops below 20 percent.

- Individual notifications for each newly created Capacity Reservation that has been below
  20 percent utilization over the last 24-hour period.
- A summary notification for all Capacity Reservations that have been below 20 percent
  utilization over the last 7-day period.

The email notifications and Health Dashboard notifications are sent to the email address
associated with the AWS account that owns the Capacity Reservations. The notifications include the
following information:

- The ID of the Capacity Reservation.
- The Availability Zone of the Capacity Reservation.
- The average utilization rate for the Capacity Reservation.
- The instance type and platform (operating system) of the Capacity Reservation.

Additionally, when capacity utilization for a Capacity Reservation in your account drops below 20
percent over a 24-hour and 7-day period, AWS Health sends events to EventBridge. With
EventBridge, you can create rules that activate automatic actions, such as sending email
notifications or triggering AWS Lambda functions, in response to such events. For
more information, see [Monitor Capacity Reservation underutilization](cr-eventbridge.md "cr-eventbridge.md").
