

# AWS Payment Encryption Service events
<a name="events-ref-aws-payment-encryption"></a>

AWS Payment Encryption Service sends service events to EventBridge via AWS CloudTrail.

## AWS Payment Encryption Service events delivered via AWS CloudTrail
<a name="event-ref-aws-payment-encryption-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Payment Encryption Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.aws-payment-encryption
+ `eventSource`: aws-payment-encryption.amazonaws.com

```
{
  "source": ["aws.aws-payment-encryption"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["aws-payment-encryption.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.aws-payment-encryption"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["aws-payment-encryption.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```