

# Amazon API Gateway events
<a name="events-ref-apigateway"></a>

API Gateway sends service events directly to EventBridge, as well as via AWS CloudTrail.

## API Gateway service events
<a name="events-ref-apigateway-events"></a>

API Gateway sends the following events directly to EventBridge: 
+ APIGateway CRL Processing

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.apigateway

```
{
  "source": ["aws.apigateway"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.apigateway"],
  "detail-type": ["{{APIGateway CRL Processing}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## API Gateway events delivered via AWS CloudTrail
<a name="event-ref-apigateway-events-via-CT"></a>

AWS CloudTrail sends events originating from API Gateway to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.apigateway
+ `eventSource`: apigateway.amazonaws.com

```
{
  "source": ["aws.apigateway"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["apigateway.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.apigateway"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["apigateway.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```