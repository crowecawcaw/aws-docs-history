

# AWS Backup events
<a name="events-ref-backup"></a>

AWS Backup sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Backup service events
<a name="events-ref-backup-events"></a>

AWS Backup sends the following events directly to EventBridge: 
+ Backup Vault State Change
+ Backup Plan State Change
+ Backup Job State Change
+ Copy Job State Change
+ Restore Job State Change
+ Recovery Point Change
+ Recovery Point State Change
+ Region Setting State Change
+ Recovery Point Index State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.backup

```
{
  "source": ["aws.backup"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.backup"],
  "detail-type": ["{{Backup Vault State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Backup events delivered via AWS CloudTrail
<a name="event-ref-backup-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Backup to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.backup
+ `eventSource`: backup.amazonaws.com

```
{
  "source": ["aws.backup"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["backup.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.backup"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["backup.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```