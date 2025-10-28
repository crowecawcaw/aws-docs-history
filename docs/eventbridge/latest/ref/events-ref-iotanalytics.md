# AWS IoT Analytics events

AWS IoT Analytics sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS IoT Analytics service events

AWS IoT Analytics sends the following events directly to EventBridge:

- IoTAnalytics DataSet Life Cycle Notification
- IoT Analytics Dataset Lifecycle Notification
- IoT Analytics Pipeline Failure Notification

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.iotanalytics

```
{
  "source": ["aws.iotanalytics"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.iotanalytics"],
  "detail-type": ["`IoTAnalytics DataSet Life Cycle Notification`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS IoT Analytics events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS IoT Analytics to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.iotanalytics
- `eventSource`: iotanalytics.amazonaws.com

```
{
  "source": ["aws.iotanalytics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["iotanalytics.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.iotanalytics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["iotanalytics.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
