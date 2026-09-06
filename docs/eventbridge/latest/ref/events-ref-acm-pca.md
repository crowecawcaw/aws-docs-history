

# AWS Private Certificate Authority events
<a name="events-ref-acm-pca"></a>

AWS Private CA sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Private CA service events
<a name="events-ref-acm-pca-events"></a>

AWS Private CA sends the following events directly to EventBridge: 
+ ACM Private CA Creation
+ ACM Private CA Certificate Issuance
+ ACM Private CA CRL Generation
+ ACM Private CA Audit Report Generation
+ ACM Private CA Certificate Revocation

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.acm-pca

```
{
  "source": ["aws.acm-pca"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.acm-pca"],
  "detail-type": ["{{ACM Private CA Creation}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Private CA events delivered via AWS CloudTrail
<a name="event-ref-acm-pca-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Private CA to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.acm-pca
+ `eventSource`: acm-pca.amazonaws.com

```
{
  "source": ["aws.acm-pca"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm-pca.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.acm-pca"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm-pca.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```