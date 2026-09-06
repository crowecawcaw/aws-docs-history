

# AWS Lambda events
<a name="events-ref-lambda"></a>

Lambda sends service events to EventBridge via AWS CloudTrail.

## Lambda events delivered via AWS CloudTrail
<a name="event-ref-lambda-events-via-CT"></a>

AWS CloudTrail sends events originating from Lambda to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.lambda
+ `eventSource`: lambda.amazonaws.com

```
{
  "source": ["aws.lambda"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["lambda.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.lambda"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["lambda.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```