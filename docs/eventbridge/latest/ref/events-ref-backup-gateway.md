

# AWS Backup gateway events
<a name="events-ref-backup-gateway"></a>

Backup gateway sends service events to EventBridge via AWS CloudTrail.

## Backup gateway events delivered via AWS CloudTrail
<a name="event-ref-backup-gateway-events-via-CT"></a>

AWS CloudTrail sends events originating from Backup gateway to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.backup-gateway
+ `eventSource`: backup-gateway.amazonaws.com

```
{
  "source": ["aws.backup-gateway"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["backup-gateway.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.backup-gateway"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["backup-gateway.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```