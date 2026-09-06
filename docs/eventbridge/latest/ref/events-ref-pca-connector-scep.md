

# AWS Private CA Connector for SCEP events
<a name="events-ref-pca-connector-scep"></a>

Connector for SCEP sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Connector for SCEP service events
<a name="events-ref-pca-connector-scep-events"></a>

Connector for SCEP sends the following events directly to EventBridge: 
+ Certificate Authority Capabilities Retrieval Failed
+ Certificate Authority Capabilities Retrieval Succeeded
+ Certificate Authority Certificate Retrieval Failed
+ Certificate Authority Certificate Retrieval Succeeded
+ Certificate Issuance Failed
+ Certificate Issuance Succeeded
+ Unsupported Operation Invoked

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.pca-connector-scep

```
{
  "source": ["aws.pca-connector-scep"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.pca-connector-scep"],
  "detail-type": ["{{Certificate Authority Capabilities Retrieval Failed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Connector for SCEP events delivered via AWS CloudTrail
<a name="event-ref-pca-connector-scep-events-via-CT"></a>

AWS CloudTrail sends events originating from Connector for SCEP to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.pca-connector-scep
+ `eventSource`: pca-connector-scep.amazonaws.com

```
{
  "source": ["aws.pca-connector-scep"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["pca-connector-scep.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.pca-connector-scep"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["pca-connector-scep.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```