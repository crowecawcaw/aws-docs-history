

# Amazon EC2 Systems Manager Contacts events
<a name="events-ref-ssm-contacts"></a>

SSM Contacts sends service events to EventBridge via AWS CloudTrail.

## SSM Contacts events delivered via AWS CloudTrail
<a name="event-ref-ssm-contacts-events-via-CT"></a>

AWS CloudTrail sends events originating from SSM Contacts to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ssm-contacts
+ `eventSource`: ssm-contacts.amazonaws.com

```
{
  "source": ["aws.ssm-contacts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm-contacts.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ssm-contacts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm-contacts.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```